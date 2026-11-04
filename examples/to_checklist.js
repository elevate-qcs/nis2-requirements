// Usage: node to_checklist.js ../data/requirements.json > checklist.md
const d = require(require("path").resolve(process.argv[2]));
console.log(`# ${d.framework} checklist\n`);
for (const r of d.requirements) console.log(`- [ ] **${r.ref}** ${r.title}: ${r.evidence}`);
