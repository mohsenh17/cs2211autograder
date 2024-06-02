# Assignment 2 Autograder

This repository contains scripts to automatically grade student submissions for Assignment 2. The autograder is designed to handle and evaluate student code submissions for two questions, compiling their C programs and comparing their output against expected results.

## Repository Structure

The repository contains the following files:

- `student_submission_preparation.py`: Prepares student submission files for grading.
- `q1_autograder.py`: Grades Question 1 by compiling and running the student's `converter.c` file.
- `q2_autograder.py`: Grades Question 2 by compiling and running the student's `intToEnglish.c` file.
- `run_autograder.sh`: A shell script to run the autograder for all student submissions.

## Files Description

### `student_submission_preparation.py`

This script extracts and prepares student submission files from a specified directory. It organizes the submissions by student name and extracts the relevant files into an `assignment2` directory.

### `q1_autograder.py`

This script compiles and runs the `converter.c` file provided by students for Question 1. It uses a set of predefined test cases to validate the output of the student's program against the expected results. The results, including the input, expected output, calculated output, outcome, and any errors, are recorded in a file named `convVal.txt` in each student's directory.

### `q2_autograder.py`

This script compiles and runs the `intToEnglish.c` file provided by students for Question 2. Similar to `q1_autograder.py`, it uses predefined test cases to compare the program's output with expected results. The results are stored in a file named `q2ConvVal.txt` in each student's directory.

### `run_autograder.sh`

This shell script runs the autograder for all student submissions by calling `q1_autograder.py` and `q2_autograder.py` for each student directory.

## How to Run

1. **Prepare the Student Files**: Extract student submissions using `student_submission_preparation.py`.

   ```sh
   python student_submission_preparation.py <path_to_student_submissions>

2. **Run the Autograder**: Execute the `run_autograder.sh` script to grade all submissions.

    ```sh
    ./run_autograder.sh

## Output
The results for Question 1 will be stored in `convVal.txt` within each student's directory.

The results for Question 2 will be stored in `q2ConvVal.txt` within each student's directory.