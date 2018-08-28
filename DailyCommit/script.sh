#!/bin/bash
git status --short | cut -d " " -f 2 | grep -m 1 "" | xargs git add
git commit -m "Test commit"
git push origin master

