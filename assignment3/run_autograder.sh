#!/bin/bash

base_dir="subs/"
directories=$(find $base_dir -maxdepth 1 -type d)
for dir in $directories; do
python q1_autograder.py $dir
done