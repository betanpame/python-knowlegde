#!/usr/bin/env python3
"""Rollback migration: practices -> tests

This script attempts to reverse the actions of migrate_tests_to_practices.py.
It will:
  - Rename 'tests/' directory back to 'tests/' (if 'tests/' does not already exist)
  - Rename filenames beginning with 'practice-' back to 'test-'
  - Replace content terminology 'Practice(s)' back to 'Practice(s)' where unambiguous
  - Convert path references 'tests/' back to 'tests/'

Safety:
  - Use --dry-run to preview.
  - If a 'tests/' directory already exists, the root rename is skipped to avoid overwriting.
  - Does NOT touch the preserved phrase 'Test Cases' (already correct) but will avoid converting 'Practice Cases' back unless it exists erroneously.

Caveats:
  - If additional manual edits occurred after forward migration, perfect reversal cannot be guaranteed.
  - JSON historical field practices_per_topic is left as-is; we only restore tests_per_topic label usage for backward compatibility.
"""
from __future__ import annotations

import os
import re
import argparse
import shutil
from typing import List

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

PRACTICE_WORD_REPLACEMENTS = [
    # Order matters: plural before singular
    (re.compile(r'\bPractices Index\b'), 'Practices Index'),
    (re.compile(r'\bPractice Structure\b'), 'Practice Structure'),
    (re.compile(r'\bAvailable Practices\b'), 'Available Practices'),
    (re.compile(r'\bHow to Use These Practices\b'), 'How to Use These Practices'),
    (re.compile(r'\bpractices per topic\b', re.IGNORECASE), 'practices per topic'),
    (re.compile(r'\bPractices\b'), 'Practices'),
    (re.compile(r'\bPractice\b'), 'Practice'),
]

PATH_REPLACEMENTS = [
    (re.compile(r'tests/'), 'tests/'),
]

TEXT_FILE_EXTS = {'.md', '.py', '.txt', '.json', '.yml', '.yaml', '.csv'}

def is_text(path: str) -> bool:
    return os.path.splitext(path)[1].lower() in TEXT_FILE_EXTS

def rename_root(dry_run: bool, report: List[str]):
    prac = os.path.join(ROOT, 'practices')
    tests = os.path.join(ROOT, 'tests')
    if not os.path.isdir(prac):
        report.append('SKIP root rename (tests/ missing)')
        return
    if os.path.isdir(tests):
        report.append('SKIP root rename (tests/ already exists)')
        return
    report.append('RENAME dir tests/ -> tests/')
    if not dry_run:
        shutil.move(prac, tests)

def walk(base: str) -> List[str]:
    out: List[str] = []
    if not os.path.isdir(base):
        return out
    for d, _, files in os.walk(base):
        for f in files:
            out.append(os.path.join(d, f))
    return out

def rename_files(dry_run: bool, report: List[str]):
    base = os.path.join(ROOT, 'tests')
    for path in walk(base):
        dirn, basefn = os.path.split(path)
        if basefn.startswith('practice-'):
            new_name = 'test-' + basefn[len('practice-'):]
            new_path = os.path.join(dirn, new_name)
            report.append(f'RENAME file {path} -> {new_path}')
            if not dry_run:
                os.replace(path, new_path)

def update_content(dry_run: bool, report: List[str]):
    # After root rename, operate under tests/
    for path in walk(os.path.join(ROOT, 'tests')):
        if not is_text(path):
            continue
        try:
            with open(path, 'r', encoding='utf-8') as f:
                original = f.read()
        except Exception:
            continue
        updated = original
        changed = False
        for rx, repl in PRACTICE_WORD_REPLACEMENTS:
            # Skip any line containing 'Test Cases' so we don't corrupt structure
            new_lines = []
            local_change = False
            for ln in updated.splitlines():
                if 'Test Cases' in ln:
                    new_lines.append(ln)
                    continue
                new_ln = rx.sub(repl, ln)
                if new_ln != ln:
                    local_change = True
                new_lines.append(new_ln)
            if local_change:
                updated = '\n'.join(new_lines)
                changed = True
        for rx, repl in PATH_REPLACEMENTS:
            new_updated = rx.sub(repl, updated)
            if new_updated != updated:
                updated = new_updated
                changed = True
        if changed and updated != original:
            report.append(f'UPDATE content {path}')
            if not dry_run:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(updated)
    # Also handle docs & scripts outside tests
    for extra in ['doc', 'scripts']:
        base = os.path.join(ROOT, extra)
        for path in walk(base):
            if not is_text(path):
                continue
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    orig = f.read()
            except Exception:
                continue
            upd = orig
            changed_any = False
            for rx, repl in PATH_REPLACEMENTS:
                n = rx.sub(repl, upd)
                if n != upd:
                    upd = n
                    changed_any = True
            if changed_any and upd != orig:
                report.append(f'UPDATE path refs {path}')
                if not dry_run:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(upd)

def main():
    p = argparse.ArgumentParser(description='Rollback practices->tests migration.')
    p.add_argument('--dry-run', action='store_true', help='Preview actions only')
    args = p.parse_args()

    report: List[str] = []
    rename_root(args.dry_run, report)
    rename_files(args.dry_run, report)
    update_content(args.dry_run, report)

    print('\nRollback Plan:' if args.dry_run else '\nRollback Actions:')
    for r in report:
        print(' -', r)
    print(f'Total actions: {len(report)}')
    if args.dry_run:
        print('\n(Dry run only)')

if __name__ == '__main__':  # pragma: no cover
    main()