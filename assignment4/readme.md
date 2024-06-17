# Assignment 4 Autograder

This repository contains scripts to automate the grading of student submissions for Assignment 4. The autograder compiles and runs each student's C program (`sport_db.c`), executes test cases, and compares the output with the expected results.

## Files and Directories

- `q1_autograder.py`: Python script that handles the compilation, execution, and validation of student submissions.
- `run_autograder.sh`: Shell script that runs the autograder for all student submissions found in the `subs` directory.
- `subs/`: Directory containing subdirectories for each student's submission.

## Directory Structure

The `subs` directory should have the following structure:
```
subs/
├── student1/
│   └── <studentID>-Assignment4/
│       └── sport_db.c
├── student2/
│   └── <studentID>-Assignment4/
│       └── sport_db.c
└── ...
```


## Usage

1. **Place student submissions**: Ensure that each student's submission is placed in a subdirectory under `subs` with the naming convention `<student_name>/<studentID>-Assignment4/`.

2. **Make scripts executable**: Ensure that the `run_autograder.sh` script has execute permissions. You can set this using the following command:
    ```bash
    chmod +x run_autograder.sh
    ```

3. **Run the autograder**: Execute the `run_autograder.sh` script to run the autograder on all student submissions:
    ```bash
    ./run_autograder.sh
    ```

4. **Review the results**: The results will be saved in two files within each student's submission directory:
    - `parsed.txt`: Contains a detailed comparison of expected and actual outputs.
    - `raw.txt`: Contains the raw output from running the student's program.

## Test Cases

The autograder uses a predefined set of test cases. Each test case includes input data and the expected output. The script will:

- Compile `sport_db.c` to produce `sport_db.out`.
- Run `sport_db.out` with the input data.
- Capture the output and compare it against the expected output.

## Error Handling

If the autograder encounters any errors (e.g., compilation errors), it will print an error message indicating the student's name and the type of error.

## Example Output

The output in `parsed.txt` will look like this for each test case:
```
test_insert_event:	 passed
test_insert_duplicate_event:	 passed
test_print_events:	 passed
test_search_event:  passed
test_update_event:	 passed
test_event_below_range:	 passed
test_event_above_range:	 passed
test_event_name_length_boundary:    passed
test_invalid_gender_entry:	 passed

```
If there is a mismatch between the expected and actual output, the entry will include both the expected and actual outputs:
```
test_insert_event:	 passed
test_insert_duplicate_event:	 passed
test_print_events:	 passed
test_search_event:  passed
test_update_event:	 passed
test_event_below_range:	 passed
test_event_above_range:	 passed
test_event_name_length_boundary:
	expected_output:4,A,very,very,very,very,very,very,long,event,name,t,13,M
	code_output:2222,dse,re,r
test_invalid_gender_entry:	 passed
```

## Notes

- Ensure that the Python script is run with Python 3.x.
- Modify the scripts as needed to fit the specific requirements of your environment or assignment specifications.

