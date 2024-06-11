#!/bin/bash

base_dir="assignment2/"
directories=$(find $base_dir -maxdepth 1 -type d)
for dir in $directories; do
python q1_autograder.py $dir
python q2_autograder.py $dir
done