#!/bin/sh

git config --global --add safe.directory /github/workspace
git config --global user.email "noreply@github.com"
git config --global user.name "Github Actions[bot]"

currentYear=$(date +'%Y')
branchName="license/${currentYear}"
commitMessage="Update license to ${currentYear}"
python3 /app/main.py --file $1 --output $1
git checkout "${branchName}" || git checkout -b "${branchName}"
git add $1
git commit --message "${commitMessage}}"
git push origin "license/${currentYear}"
gh pr create --assignee "${3}" --reviewer "${3}" --title "${4}" --body "${commitMessage}" --label "${6}"
