# Fillable .docx Templates

These are the same templates as the markdown files, converted to **fillable
Microsoft Word forms** that also open in LibreOffice/OpenOffice.

## How to fill them out

1. **Open the file** in Microsoft Word or LibreOffice/OpenOffice Writer.
2. **Tab through the form** — the cursor jumps between fill-in fields
   automatically. The document is protected as a form: you can fill the
   highlighted fields, but the surrounding text is read-only.
3. **Dropdowns** — fields like `[Yes/No]`, `[Mitigate / Transfer / Avoid /
   Accept]`, and `[Major / Minor / Observation]` are drop-down lists. Click
   and pick.
4. **Unprotect to customize** (optional):
   - *Word:* Review → Restrict Editing → Stop Protection
   - *LibreOffice:* Tools → Protect Document → uncheck "Forms"
   - The document stays fillable without unprotecting; unprotecting just
     lets you restructure it too.

## What's inside

| Domain | Files | Notes |
| :----- | :---- | :---- |
| isms/ | 13 | Includes the Statement of Applicability with 93 per-control Yes/No dropdowns |
| governance/ | 5 | |
| risk/ | 4 | |
| audit/ | 4 | |
| privacy-ai/ | 7 | |
| resilience/ | 3 | |
| ot/ | 2 | |
| checklists/ | 3 | |

All documents follow the house conventions: Georgia serif body, navy
headings, shaded table headers, and underlined fill fields.

## Regenerate

The forms are generated from the markdown templates by
`scripts/md2docx.py` (python-docx). To rebuild all:

```bash
python3 -m venv .venv-docx
.venv-docx/bin/pip install python-docx
.venv-docx/bin/python scripts/batch_docx.py
```

Requires: Python 3.9+, python-docx, LibreOffice (optional, for PDF preview).
