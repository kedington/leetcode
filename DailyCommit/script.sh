#!/bin/bash
cd /Users/snapIoTMini3/test/LeetCode 
FILENAME=$(git status --short | cut -d " " -f 2 | grep -m 1 "")
git add $FILENAME
git commit -m "Adding ${FILENAME}"
git push origin master

