"""Usage: python filter_by_role.py ../data/requirements.json <role>"""
import json, sys
d = json.load(open(sys.argv[1])); role = sys.argv[2] if len(sys.argv) > 2 else ""
for r in d["requirements"]:
    if not role or role in r["roles"] or "all" in r["roles"]:
        print(f"{r['ref']:<16} {r['title']} | evidence: {r['evidence']}")
