#!/usr/bin/env python3
"""Repository migration script: tests -> practices.

Purpose:
  - Rename root directory 'tests/' to 'tests/' (unless tests/ already exists)
  - Rename files whose basename starts with 'test-' to 'practice-'
  - Update internal content references (headings, section titles, narrative) from Test(s) to Practice(s)
  - Update doc & script references pointing to 'tests/' paths

Safety:
  - Idempotent-ish: If already migrated, it will skip renames and only attempt content normalization.
  - Provides --dry-run to preview operations without applying changes.

Usage:
  python scripts/migrate_tests_to_practices.py --dry-run   # preview
  python scripts/migrate_tests_to_practices.py             # perform migration

Notes:
  - Designed for this repo's current structure (topics numeric subfolders 1..20 under tests/).
  - Does not attempt to modify words like 'unittest', 'pytest', or lowercase 'test' inside code logic beyond specific patterns.
"""
from __future__ import annotations

import os
import re
import argparse
import shutil
from typing import List, Tuple

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Patterns & replacements (ordered)
# Preserve 'Test Cases' section heading; do not rename it. Leave list empty for now.
SECTION_REPLACEMENTS: list[tuple[str,str]] = []
# Heading line starting with '# ' and containing 'Test <number>' or 'Test ' -> Practice
HEADING_TEST_RE = re.compile(r'^(#+\s+.*)\bTest\b', re.IGNORECASE)
# Whole-word replacements (capitalized forms)
WORD_REPLACEMENTS = [
    (re.compile(r'\bTests Index\b'), 'Practices Index'),
    (re.compile(r'\bTest Structure\b'), 'Practice Structure'),
    (re.compile(r'\bAvailable Tests\b'), 'Available Practices'),
    (re.compile(r'\bHow to Use These Tests\b'), 'How to Use These Practices'),
    (re.compile(r'\btests per topic\b', re.IGNORECASE), 'practices per topic'),
    # IMPORTANT: Do not alter the phrase 'Test Cases' – skip replacements on lines containing it.
    (re.compile(r'\bTests\b'), 'Practices'),
    (re.compile(r'\bTest\b'), 'Practice'),
]
# Path style replacements inside files
PATH_REPLACEMENTS = [
    (re.compile(r'tests/'), 'tests/'),
]

EXCLUDE_FILE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.zip', '.gz'}
TEXT_FILE_EXTS = {'.md', '.py', '.txt', '.json', '.yml', '.yaml', '.csv'}


def is_text_file(path: str) -> bool:
    _, ext = os.path.splitext(path)
    return ext.lower() in TEXT_FILE_EXTS


def rename_root(dry_run: bool, actions: List[str]):
    tests_dir = os.path.join(ROOT, 'tests')
    practices_dir = os.path.join(ROOT, 'practices')
    if os.path.isdir(practices_dir):
        actions.append('SKIP root rename (tests/ already exists)')
        return
    if os.path.isdir(tests_dir):
        actions.append('RENAME dir tests/ -> tests/')
        if not dry_run:
            shutil.move(tests_dir, practices_dir)
    else:
        actions.append('SKIP root rename (tests/ not present)')


def walk_practices() -> List[str]:
    base = os.path.join(ROOT, 'practices')
    out: List[str] = []
    if not os.path.isdir(base):
        return out
    for dirpath, _, filenames in os.walk(base):
        for fn in filenames:
            out.append(os.path.join(dirpath, fn))
    return out


def rename_files(dry_run: bool, actions: List[str]):
    # Rename basenames starting with test- to practice-
    for path in walk_practices():
        dirname, basename = os.path.split(path)
        if basename.startswith('test-'):
            new_base = 'practice-' + basename[len('test-'):]
            new_path = os.path.join(dirname, new_base)
            actions.append(f'RENAME file {path} -> {new_path}')
            if not dry_run:
                os.replace(path, new_path)


def update_file_content(path: str, dry_run: bool, actions: List[str]):
    if not is_text_file(path):
        return
    try:
        with open(path, 'r', encoding='utf-8') as f:
            original = f.read()
    except Exception:
        return
    updated = original

    # Section replacements
    lines = updated.splitlines()
    changed = False
    for i, line in enumerate(lines):
        for pat, repl in SECTION_REPLACEMENTS:
            if re.search(pat, line):
                new_line = re.sub(pat, repl, line)
                if new_line != line:
                    lines[i] = new_line
                    changed = True
        # Heading substitution (# ... Test ...)
        m = HEADING_TEST_RE.match(line)
        if m:
            # Replace only the first isolated word 'Test'
            new_line = re.sub(r'\bTest\b', 'Practice', line, count=1)
            if new_line != line:
                lines[i] = new_line
                changed = True
    updated = '\n'.join(lines)

    # Whole word replacements (apply after heading logic to catch remaining narrative)
    for rx, repl in WORD_REPLACEMENTS:
        new_lines = []
        line_changed = False
        for ln in updated.splitlines():
            if 'Test Cases' in ln:  # preserve phrase exactly
                new_lines.append(ln)
                continue
            new_ln = rx.sub(repl, ln)
            if new_ln != ln:
                line_changed = True
            new_lines.append(new_ln)
        if line_changed:
            changed = True
        updated = '\n'.join(new_lines)
    # Path replacements
    for rx, repl in PATH_REPLACEMENTS:
        new_upd = rx.sub(repl, updated)
        if new_upd != updated:
            updated = new_upd
            changed = True

    if changed and updated != original:
        actions.append(f'UPDATE content {path}')
        if not dry_run:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(updated)


def update_all_contents(dry_run: bool, actions: List[str]):
    for path in walk_practices():
        update_file_content(path, dry_run, actions)
    # Also update key docs outside practices
    doc_dir = os.path.join(ROOT, 'doc')
    if os.path.isdir(doc_dir):
        for dirpath, _, filenames in os.walk(doc_dir):
            for fn in filenames:
                path = os.path.join(dirpath, fn)
                update_file_content(path, dry_run, actions)
    # Update scripts referencing tests/ (excluding this migration script and generate_progress which already supports both)
    scripts_dir = os.path.join(ROOT, 'scripts')
    for dirpath, _, filenames in os.walk(scripts_dir):
        for fn in filenames:
            path = os.path.join(dirpath, fn)
            if fn == os.path.basename(__file__):
                continue
            update_file_content(path, dry_run, actions)


def main():
    parser = argparse.ArgumentParser(description='Migrate repository terminology from tests to practices.')
    parser.add_argument('--dry-run', action='store_true', help='Preview actions without applying changes')
    args = parser.parse_args()

    actions: List[str] = []
    rename_root(args.dry_run, actions)
    rename_files(args.dry_run, actions)
    update_all_contents(args.dry_run, actions)

    print('\nMigration Plan:' if args.dry_run else '\nMigration Actions:')
    for act in actions:
        print(' -', act)
    print(f"Total actions: {len(actions)}")
    if args.dry_run:
        print('\n(Dry run only – re-run without --dry-run to apply)')

if __name__ == '__main__':  # pragma: no cover
    main()
