#!/usr/bin/env python3
"""Progress generation script.

Features:
- Scans the `tests/` tree to compute per-topic statistics.
- Distinguishes Created, Python File, Resolved (RESOLVED or VALIDATED), and Validated counts.
- Applies lightweight validation heuristics on RESOLVED / VALIDATED files.
- Emits:
  * Markdown report: doc/progressDD_MM_YYYY.md
  * JSON summary:   doc/progressDD_MM_YYYY.json
  * Shields.io style badge JSON: badges/validated.json & badges/resolved.json

Status keywords (first non-empty line of a .py file):
  # TODO:
  # RESOLVED:
  # VALIDATED:

Heuristics (initial version):
  - low_implementation_loc: RESOLVED/VALIDATED file has < 3 meaningful (non-comment) lines.
  - todo_leftover: RESOLVED/VALIDATED file still contains 'TODO'.
  - pass_leftover: RESOLVED/VALIDATED file still contains a lone 'pass' statement.
  - missing_status: Python file missing a recognized leading keyword.

You can extend heuristics later (e.g., run smoke tests, cyclomatic complexity checks, etc.).
"""
from __future__ import annotations

import argparse
import dataclasses
import datetime as _dt
import json
import os
import re
import sys
import csv
import ast
from typing import Dict, List, Optional, Tuple, Any, Set

TOTAL_PER_TOPIC = 20
STATUS_KEYWORDS = ("# TODO:", "# RESOLVED:", "# VALIDATED:")
VALID_STATUS_SET = {"TODO", "RESOLVED", "VALIDATED"}

# Configuration (set by CLI flags at runtime)
DOCSTRING_ENFORCE = False
COMPLEXITY_THRESHOLD = 15  # default cap; user can override

@dataclasses.dataclass
class FileStatus:
    path: str
    status: str  # TODO | RESOLVED | VALIDATED | UNCATEGORIZED
    meaningful_loc: int
    warnings: List[str]

@dataclasses.dataclass
class TestSlot:
    topic: str
    index: int
    created: bool
    python_files: List[str]
    file_status: Optional[FileStatus]  # primary status-bearing file (highest status)
    all_statuses: List[FileStatus]

@dataclasses.dataclass
class TopicStats:
    topic: str
    created: int
    python_files: int
    resolved: int
    validated: int
    remaining: int

@dataclasses.dataclass
class Aggregate:
    created: int
    python_files: int
    resolved: int
    validated: int

# --------------------------------- Utility ---------------------------------- #

def iter_topics(tests_root: str) -> List[str]:
    topics: List[str] = []
    for name in os.listdir(tests_root):
        full = os.path.join(tests_root, name)
        if not os.path.isdir(full):
            continue
        if name == 'README.md':
            continue
        topics.append(name)
    return sorted(topics)

_digit_dir_re = re.compile(r"^\d+$")

def iter_test_dirs(topic_path: str) -> List[Tuple[int, str]]:
    out = []
    for name in os.listdir(topic_path):
        if _digit_dir_re.match(name):
            out.append((int(name), os.path.join(topic_path, name)))
    return sorted(out, key=lambda x: x[0])

# ---------------------------- Status & Heuristics ---------------------------- #

def first_non_empty_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.rstrip()
    return ""

def count_meaningful_lines(text: str) -> int:
    count = 0
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith('#'):
            continue
        count += 1
    return count

STATUS_PREFIX_RE = re.compile(r"^#\s*(TODO|RESOLVED|VALIDATED):")

def determine_file_status(path: str) -> FileStatus:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:  # pragma: no cover - defensive
        return FileStatus(path=path, status="UNCATEGORIZED", meaningful_loc=0, warnings=[f"read_error:{e}"])

    leading = first_non_empty_line(content)
    match = STATUS_PREFIX_RE.match(leading)
    status = match.group(1) if match else "UNCATEGORIZED"
    meaningful = count_meaningful_lines(content)

    warnings: List[str] = []
    if status == "UNCATEGORIZED":
        warnings.append("missing_status")

    if status in {"RESOLVED", "VALIDATED"}:
        if meaningful < 3:
            warnings.append("low_implementation_loc")
        if 'TODO' in content:
            warnings.append("todo_leftover")
        # Lone 'pass' statements (not part of larger code) - simple heuristic
        if re.search(r"^\s*pass\s*$", content, re.MULTILINE):
            warnings.append("pass_leftover")

        # Optional docstring + complexity analysis
        try:
            tree = ast.parse(content, filename=path)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    doc = ast.get_docstring(node)
                    fn_name = node.name
                    if DOCSTRING_ENFORCE and not doc:
                        warnings.append(f"missing_docstring:{fn_name}")
                    # Cyclomatic complexity approximation
                    complexity = 1
                    for child in ast.walk(node):
                        if isinstance(child, (ast.If, ast.For, ast.While, ast.Try, ast.With, ast.IfExp)):
                            complexity += 1
                        elif isinstance(child, (ast.BoolOp, ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp, ast.ExceptHandler)):
                            complexity += 1
                    if complexity > COMPLEXITY_THRESHOLD:
                        warnings.append(f"high_complexity:{fn_name}:{complexity}")
        except SyntaxError as e:  # pragma: no cover
            warnings.append(f"syntax_error:{e.lineno}")

    return FileStatus(path=path, status=status, meaningful_loc=meaningful, warnings=warnings)

def smoke_execute(path: str) -> Optional[str]:
    """Attempt to import/execute a python file in isolation without running its __main__ guard.

    We simulate module execution by setting __name__ to a sentinel so that any
    `if __name__ == "__main__":` blocks are skipped.
    Returns an error string on failure, or None on success.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        code = compile(content, path, 'exec')
        g: Dict[str, Any] = {"__name__": "progress_smoke"}
        l: Dict[str, Any] = {}
        exec(code, g, l)  # noqa: S102 (explicit exec for controlled evaluation)
    except Exception as e:  # pragma: no cover - runtime dependent
        return f"runtime_error:{type(e).__name__}:{e}"
    return None

# ------------------------------ Collection Core ------------------------------ #

STATUS_RANK = {"UNCATEGORIZED": 0, "TODO": 1, "RESOLVED": 2, "VALIDATED": 3}

def collect(tests_root: str, do_smoke: bool = False, only_topic: Optional[str] = None) -> Tuple[List[TestSlot], Dict[str, TopicStats], Aggregate, List[FileStatus]]:
    test_slots: List[TestSlot] = []
    file_statuses: List[FileStatus] = []

    topics_iter = iter_topics(tests_root)
    if only_topic:
        topics_iter = [t for t in topics_iter if t == only_topic]
    for topic in topics_iter:
        topic_path = os.path.join(tests_root, topic)
        test_dirs = iter_test_dirs(topic_path)
        created_set = {idx for idx, _ in test_dirs}

        for idx in range(1, TOTAL_PER_TOPIC + 1):
            created = idx in created_set
            python_files: List[str] = []
            status_obj: Optional[FileStatus] = None
            statuses: List[FileStatus] = []
            if created:
                td_path = os.path.join(topic_path, str(idx))
                # gather python files
                for fname in sorted(os.listdir(td_path)):
                    if fname.endswith('.py'):
                        fpath = os.path.join(td_path, fname)
                        python_files.append(fpath)
                # evaluate all python files and choose highest status
                if python_files:
                    for pf in python_files:
                        fs = determine_file_status(pf)
                        statuses.append(fs)
                    # choose highest rank
                    if statuses:
                        status_obj = max(statuses, key=lambda s: STATUS_RANK.get(s.status, 0))
                        # conflicts: differing statuses across files
                        unique_statuses = {s.status for s in statuses if s.status != 'UNCATEGORIZED'}
                        if len(unique_statuses) > 1:
                            status_obj.warnings.append('multi_status_conflict')
                        # smoke only on chosen primary
                        if do_smoke and status_obj.status in {"RESOLVED", "VALIDATED"}:
                            smoke_issue = smoke_execute(status_obj.path)
                            if smoke_issue:
                                status_obj.warnings.append(smoke_issue)
                        # record all statuses for breakdown
                        file_statuses.extend(statuses)

            test_slots.append(TestSlot(
                topic=topic,
                index=idx,
                created=created,
                python_files=python_files,
                file_status=status_obj,
                all_statuses=statuses
            ))

    # Aggregate per topic
    topic_stats: Dict[str, TopicStats] = {}
    for topic in topics_iter:
        topic_slots = [s for s in test_slots if s.topic == topic]
        created_count = sum(1 for s in topic_slots if s.created)
        python_file_count = sum(1 for s in topic_slots if s.python_files)
        resolved_count = sum(1 for s in topic_slots if (s.file_status and s.file_status.status in {"RESOLVED", "VALIDATED"}))
        validated_count = sum(1 for s in topic_slots if (s.file_status and s.file_status.status == "VALIDATED"))
        remaining = TOTAL_PER_TOPIC - created_count
        topic_stats[topic] = TopicStats(
            topic=topic,
            created=created_count,
            python_files=python_file_count,
            resolved=resolved_count,
            validated=validated_count,
            remaining=remaining,
        )

    agg = Aggregate(
        created=sum(t.created for t in topic_stats.values()),
        python_files=sum(t.python_files for t in topic_stats.values()),
        resolved=sum(t.resolved for t in topic_stats.values()),
        validated=sum(t.validated for t in topic_stats.values()),
    )

    return test_slots, topic_stats, agg, file_statuses

# ------------------------------ Formatting ---------------------------------- #

def pct(part: int, total: int) -> str:
    if total == 0:
        return "0%"
    return f"{(part / total) * 100:.0f}%"

def pct_float(part: int, total: int) -> float:
    return (part / total * 100) if total else 0.0

MD_HEADER = """# Study Progress Report ({date})\n\nGenerated automatically by `generate_progress.py`.\n\n---\n\n## 1. Snapshot Summary\n"""

MD_DEFINITIONS = """Definitions:\n\n- Created Test: Folder with markdown created (counts toward curriculum build-out)\n- Python File: At least one `*.py` file exists for that test (implementation started)\n- Status Keywords (first non-empty line of primary `.py` file):\n    - `# TODO:` → Implementation not started / placeholder\n    - `# RESOLVED:` → Implementation written but not yet validated\n    - `# VALIDATED:` → Implementation written & validated\n- Resolved Test: Leading keyword is `# RESOLVED:` or `# VALIDATED:` (Validated is a subset)\n- Validated Test: Leading keyword is `# VALIDATED:` and passes heuristic checks (in future)\n"""

def build_markdown(date_str: str, topic_stats: Dict[str, TopicStats], agg: Aggregate, file_statuses: List[FileStatus]) -> str:
    total_possible = TOTAL_PER_TOPIC * len(topic_stats)
    # Status breakdown counts
    counts = {"TODO":0, "RESOLVED":0, "VALIDATED":0, "UNCATEGORIZED":0}
    for fs in file_statuses:
        counts[fs.status] = counts.get(fs.status, 0) + 1

    lines: List[str] = []
    lines.append(MD_HEADER.format(date=date_str))
    lines.append(MD_DEFINITIONS)
    lines.append("\n| Topic | Created | Python Files | Resolved | Validated | Remaining (Created) | Created % | Python File % | Resolved % | Validated % |")
    lines.append("|-------|---------|--------------|----------|-----------|---------------------|-----------|---------------|------------|-------------|")

    for topic in sorted(topic_stats):
        t = topic_stats[topic]
        lines.append(
            f"| {t.topic} | {t.created} | {t.python_files} | {t.resolved} | {t.validated} | {t.remaining} | "
            f"{pct(t.created, TOTAL_PER_TOPIC)} | {pct(t.python_files, TOTAL_PER_TOPIC)} | {pct(t.resolved, TOTAL_PER_TOPIC)} | {pct(t.validated, TOTAL_PER_TOPIC)} |"
        )

    lines.append(f"\n**Overall Created Progress:** {agg.created} / {total_possible} = **{agg.created/total_possible*100:.1f}%**")
    lines.append(f"\n**Overall Python File Coverage:** {agg.python_files} / {total_possible} = **{agg.python_files/total_possible*100:.1f}%**")
    lines.append(f"\n**Overall Resolved Progress:** {agg.resolved} / {total_possible} = **{agg.resolved/total_possible*100:.1f}%**")
    lines.append(f"\n**Overall Validated Progress:** {agg.validated} / {total_possible} = **{agg.validated/total_possible*100:.1f}%**")

    lines.append("\nStatus Breakdown (by leading keyword in primary `.py` files):\n")
    for key in ["TODO", "RESOLVED", "VALIDATED", "UNCATEGORIZED"]:
        lines.append(f"- {key}: {counts.get(key,0)}")

    lines.append(
        f"\nTransition Funnel (files): Created → Python File ({agg.python_files}) → Resolved ({agg.resolved}) → Validated ({agg.validated})\n"
    )

    # Heuristic issues summary
    issues = [fs for fs in file_statuses if fs.warnings]
    if issues:
        lines.append("\n### Heuristic Warnings\n")
        lines.append("| File | Status | Warnings | Meaningful LOC |")
        lines.append("|------|--------|----------|----------------|")
        for fs in sorted(issues, key=lambda x: (len(x.warnings), x.path), reverse=True):
            lines.append(f"| {fs.path} | {fs.status} | {', '.join(fs.warnings)} | {fs.meaningful_loc} |")
    else:
        lines.append("\n_No heuristic warnings._\n")

    lines.append("\n---\n\n*End of automated report.*\n")
    return "\n".join(lines)

# ------------------------------ JSON Output --------------------------------- #

def build_json(date_str: str, topic_stats: Dict[str, TopicStats], agg: Aggregate, file_statuses: List[FileStatus]) -> Dict:
    total_possible = TOTAL_PER_TOPIC * len(topic_stats)
    status_counts = {"TODO":0, "RESOLVED":0, "VALIDATED":0, "UNCATEGORIZED":0}
    for fs in file_statuses:
        status_counts[fs.status] = status_counts.get(fs.status, 0) + 1

    data = {
        "date": date_str,
        "totals": {
            "topics": len(topic_stats),
            "tests_per_topic": TOTAL_PER_TOPIC,
            "possible": total_possible,
            "created": agg.created,
            "python_files": agg.python_files,
            "resolved": agg.resolved,
            "validated": agg.validated,
            "percent_created": round(pct_float(agg.created, total_possible), 2),
            "percent_python_files": round(pct_float(agg.python_files, total_possible), 2),
            "percent_resolved": round(pct_float(agg.resolved, total_possible), 2),
            "percent_validated": round(pct_float(agg.validated, total_possible), 2),
        },
        "topics": [],
        "status_breakdown": status_counts,
        "files": [
            {
                "path": fs.path,
                "status": fs.status,
                "meaningful_loc": fs.meaningful_loc,
                "warnings": fs.warnings,
            }
            for fs in file_statuses
        ],
    }

    for topic in sorted(topic_stats):
        t = topic_stats[topic]
        data["topics"].append({
            "topic": t.topic,
            "created": t.created,
            "python_files": t.python_files,
            "resolved": t.resolved,
            "validated": t.validated,
            "remaining": t.remaining,
            "percent_created": round(pct_float(t.created, TOTAL_PER_TOPIC), 2),
            "percent_python": round(pct_float(t.python_files, TOTAL_PER_TOPIC), 2),
            "percent_resolved": round(pct_float(t.resolved, TOTAL_PER_TOPIC), 2),
            "percent_validated": round(pct_float(t.validated, TOTAL_PER_TOPIC), 2),
        })

    return data

# ------------------------------ Badges --------------------------------------- #

def badge_color(pct_value: float) -> str:
    if pct_value >= 90:
        return "brightgreen"
    if pct_value >= 75:
        return "green"
    if pct_value >= 50:
        return "yellowgreen"
    if pct_value >= 25:
        return "yellow"
    return "red"

BADGE_SCHEMA_VERSION = 1

def build_badge(label: str, message: str, pct_value: float) -> Dict:
    return {
        "schemaVersion": BADGE_SCHEMA_VERSION,
        "label": label,
        "message": message,
        "color": badge_color(pct_value),
    }

# ------------------------------ Main CLI ------------------------------------- #

def write_file(path: str, content: str, binary: bool = False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    mode = 'wb' if binary else 'w'
    with open(path, mode, encoding=None if binary else 'utf-8') as f:
        f.write(content)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Generate progress markdown, JSON summary, and badges.")
    parser.add_argument('--tests-root', default='tests', help='Root directory containing topic folders (default: tests)')
    parser.add_argument('--date', default=None, help='Override date (format DD-MM-YYYY); default: today')
    parser.add_argument('--no-md', action='store_true', help='Skip writing markdown file')
    parser.add_argument('--no-json', action='store_true', help='Skip writing JSON summary file')
    parser.add_argument('--no-badges', action='store_true', help='Skip writing badge files')
    parser.add_argument('--stdout', action='store_true', help='Print markdown to stdout')
    parser.add_argument('--smoke', action='store_true', help='Run smoke execution for RESOLVED/VALIDATED primary files')
    parser.add_argument('--only-topic', default=None, help='Limit scan to a single topic (speeds up incremental work)')
    parser.add_argument('--list-topics', action='store_true', help='List available topics and exit')
    parser.add_argument('--no-history', action='store_true', help='Skip resolved history tracking/delta generation')
    parser.add_argument('--export-csv', action='store_true', help='Also export a CSV summary file')
    parser.add_argument('--promote', action='store_true', help='Promote eligible TODO files to RESOLVED based on heuristics')
    parser.add_argument('--promote-threshold', type=int, default=3, help='Meaningful LOC threshold for promotion (default: 3)')
    parser.add_argument('--promote-allow-pass', type=int, default=0, help='Allow up to N pass statements during promotion (default: 0)')
    parser.add_argument('--generate-harness', default=None, help='Generate a harness file for a specific topic and exit')
    parser.add_argument('--enforce-docstrings', action='store_true', help='Enforce function docstrings for RESOLVED/VALIDATED')
    parser.add_argument('--complexity-threshold', type=int, default=15, help='Cyclomatic complexity threshold (default: 15)')
    parser.add_argument('--create-missing', action='store_true', help='Create missing test folders with starter markdown (and optional .py)')
    parser.add_argument('--create-with-py', action='store_true', help='When creating missing tests also add a starter .py file')
    args = parser.parse_args(argv)

    date_str = args.date or _dt.datetime.now().strftime('%d-%m-%Y')

    # Topic list support
    if args.list_topics:
        for t in iter_topics(args.tests_root):
            print(t)
        return 0

    # Apply config
    global DOCSTRING_ENFORCE, COMPLEXITY_THRESHOLD
    DOCSTRING_ENFORCE = args.enforce_docstrings
    COMPLEXITY_THRESHOLD = args.complexity_threshold

    # Optional creation of missing tests BEFORE collection
    if args.create_missing:
        def slugify(topic: str) -> str:
            return re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', topic).lower()
        topics_scope = iter_topics(args.tests_root)
        if args.only_topic:
            topics_scope = [t for t in topics_scope if t == args.only_topic]
        for topic in topics_scope:
            topic_path = os.path.join(args.tests_root, topic)
            existing_indices = {int(d) for d in os.listdir(topic_path) if d.isdigit()}
            for idx in range(1, TOTAL_PER_TOPIC + 1):
                if idx in existing_indices:
                    continue
                folder = os.path.join(topic_path, str(idx))
                os.makedirs(folder, exist_ok=True)
                slug = slugify(topic)
                md_name = f"test-{slug}-{idx}.md"
                md_path = os.path.join(folder, md_name)
                if not os.path.exists(md_path):
                    md_content = (
                        f"# {topic} Test {idx}\n\n"
                        "## Description\n\n<add description>\n\n"
                        "## Objectives\n\n- Objective 1\n- Objective 2\n\n"
                        "## Tasks\n\n1. Task one\n2. Task two\n\n"
                        "## Examples\n\n```python\n# examples here\n```\n\n"
                        "## Hints\n\n- Hint one\n\n"
                        "## Test Cases\n\n- Case 1\n\n"
                        "## Bonus\n\n- Stretch idea\n"
                    )
                    with open(md_path, 'w', encoding='utf-8') as mf:
                        mf.write(md_content)
                if args.create_with_py:
                    py_name = f"test-{slug}-{idx}.py"
                    py_path = os.path.join(folder, py_name)
                    if not os.path.exists(py_path):
                        with open(py_path, 'w', encoding='utf-8') as pf:
                            pf.write("# TODO: Implement solution for this test\n\n")
        print('[created] Missing test folders initialized.')

    test_slots, topic_stats, agg, file_statuses = collect(args.tests_root, do_smoke=args.smoke, only_topic=args.only_topic)

    # Harness generation (listing functions/classes) for a topic
    if args.generate_harness:
        harness_topic = args.generate_harness
        lines = [f"# Auto-generated Harness for {harness_topic}\n"]
        for slot in test_slots:
            if slot.topic != harness_topic:
                continue
            if not slot.python_files:
                continue
            for pf in slot.python_files:
                rel = os.path.relpath(pf)
                lines.append(f"# {rel}")
                try:
                    with open(pf, 'r', encoding='utf-8') as fh:
                        for cl in fh:
                            if cl.startswith('def ') or cl.startswith('class '):
                                lines.append(cl.rstrip())
                except Exception as e:  # pragma: no cover
                    lines.append(f"# error reading {rel}: {e}")
                lines.append("")
        harness_path = os.path.join('.progress_state', f'harness_{harness_topic}.txt')
        write_file(harness_path, "\n".join(lines))
        print(f'[written] {harness_path}')
        return 0

    # Promotion phase BEFORE writing artifacts if requested
    if args.promote:
        promoted: List[str] = []
        for slot in test_slots:
            fs = slot.file_status
            if not fs or fs.status != 'TODO':
                continue
            # re-read file content
            try:
                with open(fs.path, 'r', encoding='utf-8') as rf:
                    content = rf.read()
            except Exception:
                continue
            meaningful = count_meaningful_lines(content)
            if meaningful < args.promote_threshold:
                continue
            # Count pass lines
            pass_lines = len(re.findall(r"^\s*pass\s*$", content, re.MULTILINE))
            if pass_lines > args.promote_allow_pass:
                continue
            # ensure at least one def or class exists
            if not re.search(r"^(def |class )", content, re.MULTILINE):
                continue
            # ensure no lingering TODO lines beyond header
            lines_c = content.splitlines()
            header_index = None
            for i, ln in enumerate(lines_c):
                if ln.strip():
                    header_index = i
                    break
            if header_index is None:
                continue
            header_line = lines_c[header_index]
            m = STATUS_PREFIX_RE.match(header_line)
            if not m or m.group(1) != 'TODO':
                continue
            # check if later lines contain 'TODO'
            later = '\n'.join(lines_c[header_index+1:])
            if 'TODO' in later:
                continue
            # perform replacement
            lines_c[header_index] = header_line.replace('# TODO:', '# RESOLVED:')
            new_content = '\n'.join(lines_c)
            if not new_content.endswith('\n'):
                new_content += '\n'
            try:
                with open(fs.path, 'w', encoding='utf-8') as wf:
                    wf.write(new_content)
                promoted.append(fs.path)
            except Exception:
                continue
        if promoted:
            print(f"[promoted] {len(promoted)} files -> RESOLVED")
            # Re-collect to update stats
            test_slots, topic_stats, agg, file_statuses = collect(args.tests_root, do_smoke=args.smoke, only_topic=args.only_topic)
        else:
            print('[info] No eligible TODO files for promotion.')

    md = build_markdown(date_str, topic_stats, agg, file_statuses)
    summary_json = build_json(date_str, topic_stats, agg, file_statuses)

    date_token = date_str.replace('-', '_')

    if not args.no_md:
        md_path = os.path.join('doc', f'progress{date_token}.md')
        write_file(md_path, md)
        print(f'[written] {md_path}')
    if not args.no_json:
        json_path = os.path.join('doc', f'progress{date_token}.json')
        write_file(json_path, json.dumps(summary_json, indent=2, ensure_ascii=False) + '\n')
        print(f'[written] {json_path}')
    if args.export_csv:
        csv_path = os.path.join('doc', f'progress{date_token}.csv')
        with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
            writer = csv.writer(cf)
            writer.writerow(['Topic','Created','PythonFiles','Resolved','Validated','Remaining','Created%','PythonFile%','Resolved%','Validated%'])
            for topic in sorted(topic_stats):
                t = topic_stats[topic]
                writer.writerow([
                    t.topic, t.created, t.python_files, t.resolved, t.validated, t.remaining,
                    f"{pct_float(t.created, TOTAL_PER_TOPIC):.1f}",
                    f"{pct_float(t.python_files, TOTAL_PER_TOPIC):.1f}",
                    f"{pct_float(t.resolved, TOTAL_PER_TOPIC):.1f}",
                    f"{pct_float(t.validated, TOTAL_PER_TOPIC):.1f}",
                ])
        print(f'[written] {csv_path}')

    # -------------------- Resolved History / Delta Generation -------------------- #
    if not args.no_history:
        history_dir = os.path.join('.progress_state')
        os.makedirs(history_dir, exist_ok=True)
        history_path = os.path.join(history_dir, 'resolved_history.json')
        # Current resolved identifiers
        current_resolved: Set[str] = set(
            f"{slot.topic}/{slot.index}" for slot in test_slots
            if slot.file_status and slot.file_status.status in {"RESOLVED", "VALIDATED"}
        )
        # Load existing history
        history_data: Dict[str, str] = {}
        if os.path.exists(history_path):
            try:
                with open(history_path, 'r', encoding='utf-8') as hf:
                    history_data = json.load(hf)
            except Exception as e:  # pragma: no cover
                print(f'[warn] Could not read history file: {e}', file=sys.stderr)
        previous_set = set(history_data.keys())
        new_items = sorted(current_resolved - previous_set)
        # Add new items with first-seen date
        for ident in new_items:
            history_data[ident] = date_str
        # Write updated history
        write_file(history_path, json.dumps(history_data, indent=2, ensure_ascii=False) + '\n')
        print(f'[updated] {history_path} (total resolved tracked: {len(history_data)})')

        # Delta markdown (only if there are new items)
        if new_items:
            delta_md_lines = [f"# Newly Completed Tests ({date_str})\n", f"Generated by generate_progress.py\n", "", "## New Resolved / Validated", ""]
            for ident in new_items:
                delta_md_lines.append(f"- {ident}")
            delta_md_lines.append("")
            delta_path = os.path.join('doc', f'completed_delta_{date_token}.md')
            write_file(delta_path, "\n".join(delta_md_lines))
            print(f'[written] {delta_path}')
        else:
            print('[info] No newly resolved tests this run.')

        # Cumulative markdown (always overwrite)
        cumulative_lines = ["# All Completed (Resolved or Validated) Tests\n", "| Test | First Seen |", "|------|------------|"]
        for ident in sorted(history_data.keys(), key=lambda k: (history_data[k], k)):
            cumulative_lines.append(f"| {ident} | {history_data[ident]} |")
        cumulative_lines.append("")
        cumulative_path = os.path.join('doc', 'completed_all.md')
        write_file(cumulative_path, "\n".join(cumulative_lines))
        print(f'[written] {cumulative_path}')
    if not args.no_badges:
        # Build badges directory
        validated_pct = summary_json['totals']['percent_validated']
        resolved_pct = summary_json['totals']['percent_resolved']
        badge_validated = build_badge('validated', f"{agg.validated}/{summary_json['totals']['possible']} ({validated_pct:.1f}%)", validated_pct)
        badge_resolved = build_badge('resolved', f"{agg.resolved}/{summary_json['totals']['possible']} ({resolved_pct:.1f}%)", resolved_pct)
        write_file(os.path.join('badges', 'validated.json'), json.dumps(badge_validated, indent=2) + '\n')
        write_file(os.path.join('badges', 'resolved.json'), json.dumps(badge_resolved, indent=2) + '\n')
        print('[written] badges/validated.json')
        print('[written] badges/resolved.json')

    if args.stdout:
        print('\n' + md)

    return 0

if __name__ == '__main__':  # pragma: no cover
    raise SystemExit(main())
