#!/usr/bin/env python3
"""Normalization script for post-migration cleanup.

Goals:
  - Ensure all practice directories contain consistently named markdown & optional python files.
  - Re-sync filename slugs (handle mixed forms like practice-fileoperations vs practice-file-operations).
  - Optionally (flag) regenerate missing .py starter stubs if markdown exists.
  - Report anomalies:
      * Multiple practice-*.md files in a single numeric folder
      * Missing markdown or python
      * Unexpected leftover 'test-' filenames
  - Provide a --fix mode to rename inconsistent slugs (converting camel / concatenated to dash-separated where possible).

This script is conservative: it prints a plan first unless --apply is given.
"""
from __future__ import annotations

import os
import re
import argparse
from typing import List, Dict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PRACTICES_DIR = os.path.join(ROOT, 'practices')
SLUG_RE = re.compile(r'^practice-(?P<slug>.+?)-(\d+)\.(md|py)$')
DASH_NORMALIZE_RE = re.compile(r'[^a-z0-9]+')


def list_topic_dirs() -> List[str]:
    if not os.path.isdir(PRACTICES_DIR):
        return []
    return [d for d in sorted(os.listdir(PRACTICES_DIR)) if os.path.isdir(os.path.join(PRACTICES_DIR, d)) and d != 'README.md']


def normalize_slug(raw: str) -> str:
    lowered = raw.lower()
    return DASH_NORMALIZE_RE.sub('-', lowered).strip('-')


def scan(apply: bool, fix: bool, add_py: bool) -> int:
    topics = list_topic_dirs()
    issues: List[str] = []
    actions: List[str] = []
    for topic in topics:
        topic_path = os.path.join(PRACTICES_DIR, topic)
        for entry in sorted(os.listdir(topic_path)):
            slot_path = os.path.join(topic_path, entry)
            if not (entry.isdigit() and os.path.isdir(slot_path)):
                continue
            md_files = [f for f in os.listdir(slot_path) if f.endswith('.md')]
            py_files = [f for f in os.listdir(slot_path) if f.endswith('.py')]
            # Detect leftover test- files
            for f in md_files + py_files:
                if f.startswith('test-'):
                    issues.append(f'[LEFTOVER TEST PREFIX] {slot_path}/{f}')
            # Ensure exactly one markdown file
            if not md_files:
                issues.append(f'[MISSING MD] {slot_path}')
            elif len(md_files) > 1:
                issues.append(f'[MULTIPLE MD] {slot_path}: {md_files}')
            # Normalize names
            for f in md_files + py_files:
                m = SLUG_RE.match(f)
                if not m:
                    issues.append(f'[UNEXPECTED NAME] {slot_path}/{f}')
                    continue
                raw_slug = m.group('slug')
                norm_slug = normalize_slug(raw_slug)
                if fix and raw_slug != norm_slug:
                    new_name = f.replace(raw_slug, norm_slug)
                    src = os.path.join(slot_path, f)
                    dst = os.path.join(slot_path, new_name)
                    actions.append(f'RENAME {src} -> {dst}')
                    if apply:
                        os.replace(src, dst)
            # Add python stub if requested and missing
            if add_py and not py_files and md_files:
                # Derive slug from first md
                m = SLUG_RE.match(md_files[0])
                if m:
                    slug = m.group('slug')
                    py_name = f'practice-{slug}-{entry}.py'
                    py_path = os.path.join(slot_path, py_name)
                    actions.append(f'CREATE STUB {py_path}')
                    if apply:
                        with open(py_path, 'w', encoding='utf-8') as f:
                            f.write('# TODO: Implement solution for this practice\n\n')
    print('Normalization Issues Found:' if issues else 'No structural issues found.')
    for i in issues:
        print(' -', i)
    print('\nPlanned Actions:' if actions else '\nNo actions needed.')
    for a in actions:
        print(' -', a)
    if not apply and actions:
        print('\n(Re-run with --apply to perform actions)')
    return 0


def main():
    ap = argparse.ArgumentParser(description='Normalize practice directory structure and filenames.')
    ap.add_argument('--apply', action='store_true', help='Apply changes (default is read-only)')
    ap.add_argument('--fix', action='store_true', help='Attempt to fix slug inconsistencies')
    ap.add_argument('--add-py', action='store_true', help='Create missing python stub if markdown exists')
    args = ap.parse_args()
    return scan(apply=args.apply, fix=args.fix, add_py=args.add_py)

if __name__ == '__main__':  # pragma: no cover
    raise SystemExit(main())
