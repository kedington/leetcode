#!/bin/bash
FILENAME=git status --short | cut -d " " -f 2 | grep -m 1 "" 
git add $FILENAME
git commit -m "Add " + $FILENAME
git push origin master

