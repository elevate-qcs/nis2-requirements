# How to use NIS2 Directive Requirements

## 1. Find what applies to you
Filter the **roles** column to your role and check **applies_from** for dates.

## 2. Gap assessment in a spreadsheet
1. Download `data/requirements.csv` and open it in Excel or Google Sheets (comma separated, UTF-8).
2. Add columns: `status` (not started, in progress, implemented, evidence ready, N/A), `owner`, `evidence_location`, `due`.
3. Use the **evidence** column as a guide. Mark non-applicable rows N/A with a reason; don't delete them.

## 3. Prepare for an audit or inspection
For each requirement, make sure you can show at least one record from the evidence column. Auditors sample records, not only documents.

## 4. Use the data in code
```python
import json, urllib.request
url = "https://raw.githubusercontent.com/elevate-qcs/nis2-requirements/main/data/requirements.json"
data = json.load(urllib.request.urlopen(url))
for r in data["requirements"]:
    print(r["ref"], r["title"], "->", r["evidence"])
```

## Fields
| Field | Meaning |
|---|---|
| id | Stable ID |
| ref | Article, clause or category |
| title | Short name |
| roles | Who it applies to |
| summary | What it requires, in plain language (our words) |
| applies_from | Date or status |
| evidence | Examples of objective evidence to keep |

This is a summary to help you organize work. Always check the official text and get qualified advice for legal questions.
