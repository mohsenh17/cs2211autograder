# Assignment 3 Autograder

This repository contains scripts to automate the grading of student submissions for Assignment 3. The autograder compiles and runs each student's C program (`part1.c`), executes test cases, and compares the output with the expected results.

## Files and Directories

- `q1_autograder.py`: Python script that handles the compilation, execution, and validation of student submissions.
- `run_autograder.sh`: Shell script that runs the autograder for all student submissions found in the `subs` directory.
- `subs/`: Directory containing subdirectories for each student's submission.

## Directory Structure

The `subs` directory should have the following structure:
```
subs/
├── student1/
│   └── <studentID>-Assignment3/
│       └── part1.c
├── student2/
│   └── <studentID>-Assignment3/
│       └── part1.c
└── ...
```


## Usage

1. **Place student submissions**: Ensure that each student's submission is placed in a subdirectory under `subs` with the naming convention `<student_name>/<studentID>-Assignment3/`.

2. **Make scripts executable**: Ensure that the `run_autograder.sh` script has execute permissions. You can set this using the following command:
    ```bash
    chmod +x run_autograder.sh
    ```

3. **Run the autograder**: Execute the `run_autograder.sh` script to run the autograder on all student submissions:
    ```bash
    ./run_autograder.sh
    ```

4. **Review the results**: The results will be saved in two files within each student's submission directory:
    - `convVal.txt`: Contains a detailed comparison of expected and actual outputs.
    - `re.txt`: Contains the raw output from running the student's program.

## Test Cases

The autograder uses a predefined set of test cases. Each test case includes input data and the expected output. The script will:

- Compile `part1.c` to produce `part1.out`.
- Run `part1.out` with the input data.
- Capture the output and compare it against the expected output.

## Error Handling

If the autograder encounters any errors (e.g., compilation errors), it will print an error message indicating the student's name and the type of error.

## Example Output

The output in `convVal.txt` will look like this for each test case:
```
{input_5_1,2,3,4,5:
{p1: correct}
{p2: correct}
{p3: correct}
{p4: correct}
{p5: correct}
{p6: correct}
}
```
If there is a mismatch between the expected and actual output, the entry will include both the expected and actual outputs:
```
{input_5_1,2,3,4,5:
{p1: correct}
{p2: correct}
{p3:
expected_output: [1] = 2, [3] = 4
code_output: [1] = 2, [3] = 3 }
{p4: correct}
{p5: correct}
{p6: correct}
}
```

## Notes

- Ensure that the Python script is run with Python 3.x.
- Modify the scripts as needed to fit the specific requirements of your environment or assignment specifications.

