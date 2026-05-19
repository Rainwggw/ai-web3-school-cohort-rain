#!/bin/bash

# Create daily note script
# Usage: ./create-daily-note.sh

# Get today's date
TODAY=$(date +%Y-%m-%d)

# Create the daily note file
cat > "daily/$TODAY-learning-note.md" << EOF
# Daily Note - $TODAY

## Today's Goals

- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## Learning Content

### Topics Covered

-

### Key Takeaways

-

### Questions / Blockers

-

## Experiments / Code

\`\`\`
# Code snippets or experiments
\`\`\`

## Resources

-

## Tomorrow's Plan

-

## Check-in

- [ ] Submitted to WCB platform
- Check-in link:

---

*Created using template: $(date)*
EOF

echo "Daily note created: daily/$TODAY-learning-note.md"

# Open the file for editing
if command -v code &> /dev/null; then
    code "daily/$TODAY-learning-note.md"
elif command -v vim &> /dev/null; then
    vim "daily/$TODAY-learning-note.md"
else
    echo "Please open daily/$TODAY-learning-note.md manually to edit"
fi