#!/usr/bin/env python3
"""Batch-convert all markdown templates in the repo to fillable .docx."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VENV = os.path.join(ROOT, ".venv-docx", "bin", "python")
CONV = os.path.join(ROOT, "scripts", "md2docx.py")

DOMAINS = ["isms", "governance", "risk", "audit", "privacy-ai", "resilience", "ot", "checklists"]

converted = []
failed = []
for domain in DOMAINS:
    src_dir = os.path.join(ROOT, domain)
    dst_dir = os.path.join(ROOT, "docx", domain)
    os.makedirs(dst_dir, exist_ok=True)
    for f in sorted(os.listdir(src_dir)):
        if not f.endswith(".md"):
            continue
        src = os.path.join(src_dir, f)
        dst = os.path.join(dst_dir, f.replace(".md", ".docx"))
        r = subprocess.run(
            [VENV, CONV, src, dst], capture_output=True, text=True
        )
        if r.returncode == 0:
            converted.append(dst)
        else:
            failed.append((src, r.stderr[-300:]))

print(f"converted: {len(converted)}")
for f in converted:
    print(f"  OK  {os.path.relpath(f, ROOT)}")
if failed:
    print(f"\nFAILED: {len(failed)}")
    for src, err in failed:
        print(f"  FAIL {src}\n    {err}")
    sys.exit(1)
