import os
import subprocess
import glob
import re
import sys

def replace_whitespace_with_comma(text):
    result = re.sub(r'\s+', ',', text.strip())
    return result

def write_log(file_address, message):
    with open(file_address, 'a+') as w:
        w.write(message)

def run_test_case(test_case, executable, raw_file_address, parsed_file_address, table_name):
    process = subprocess.Popen([executable], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=test_case["input"])
    if stderr:
        print(f"Error running the test case '{test_case}':\n{stderr}")
        return False
    expected_output = test_case["expected_out"]
    producedMessage = replace_whitespace_with_comma(stdout[stdout.find('\n', stdout.find(f'{table_name} Code')):stdout.find('Enter', stdout.find(f'{table_name} Code'))].strip())
    if not expected_output in replace_whitespace_with_comma(stdout):
        write_log(parsed_file_address, f"\n\texpected_output: {expected_output}")
        write_log(parsed_file_address, f"\n\tcode_output: {producedMessage}\n")
        write_log(raw_file_address, f"\n{stdout}\n\n\n\n\n")
    else:
        write_log(parsed_file_address, "\tpassed\n")
    return expected_output in replace_whitespace_with_comma(stdout)

def compile_and_run(student_name):
    directories = glob.glob(f"subs/{student_name}/2*-Assignment5")
    if not directories:
        print("Assignment directory not found.")
        return
    directory = directories[0]

    compile_command = f"gcc {directory}/*.c -o {directory}/sport_db.out"
    compile_process = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if compile_process.returncode != 0:
        print(f"Compilation failed:\n{compile_process.stderr.decode()}")
        return

    executable = f"{directory}/sport_db.out"
    raw_file_address = f"subs/{student_name}/raw.txt"
    parsed_file_address = f"subs/{student_name}/parsed.txt"

    event_test_cases = {
        "test_insert_event": {
            "input": "e\ni\n0\nField Hockey\n12\nM\np\nq\nq\n",
            "expected_out": "0,Field Hockey,12,M"
        },
        "test_print_events": {
            "input": "e\ni\n1\nHandball\n16\nX\ni\n2\nSwimming\n14\nW\ni\n3\nCycling\n20\nM\np\nq\nq\n",
            "expected_out": "3,Cycling,20,M,2,Swimming,14,W,1,Handball,16,X"
        },
        "test_search_event": {
            "input": "e\ni\n1\nHandball\n16\nX\ns\n1\np\nq\nq\n",
            "expected_out": "1,Handball,16,X"
        },
        "test_update_event": {
            "input": "e\ni\n1\nHandball\n16\nX\nu\n1\nBasketball\n15\nM\np\nq\nq\n",
            "expected_out": "1,Basketball,15,M"
        },
        "test_event_below_competitors_range": {
            "input": "e\ni\n1\nSoccer\n8\nM\np\nq\nq\n",
            "expected_out": ""
        },
        "test_event_above_competitors_range": {
            "input": "e\ni\n1\nSoccer\n100\nM\np\nq\nq\n",
            "expected_out": ""
        },
        "test_event_name_length_boundary": {
            "input": "e\ni\n4\nA very very very very very very long event name that should be truncated\n13\nM\np\nq\nq\n",
            "expected_out": "4,A very very very very very very long event nam,13,M"
        },
        "test_invalid_gender_entry": {
            "input": "e\ni\n3\nSwimming\n30\nA\np\nq\nq\n",
            "expected_out": ""
        },
        "test_erase_event": {
            "input": "e\ni\n2\nVolleyball\n20\nX\ne\n2\np\nq\nq\n",
            "expected_out": ""
        },
        "test_duplicate_event_code": {
            "input": "e\ni\n5\nBasketball\n22\nW\ni\n5\nBadminton\n15\nM\np\nq\nq\n",
            "expected_out": "5,nBasketball,22,W"
        }
    }

    athlete_test_cases = {
        "test_insert_athlete": {
            "input": "a\ni\n0\nJohn Smith\n25\nUSA\np\nq\nq\n",
            "expected_out": "0,John Smith,25,USA"
        },
        "test_print_athletes": {
            "input": "a\ni\n1\nJane Doe\n30\nCAN\ni\n2\nAlice Johnson\n22\nMEX\ni\n3\nBob Brown\n27\nUSA\np\nq\nq\n",
            "expected_out": "1,Jane Doe,30,CAN,2,Alice Johnson,22,MEX,3,Bob Brown,27,USA"
        },
        "test_search_athlete": {
            "input": "a\ni\n1\nJane Doe\n30\nCAN\ns\n1\nq\nq\n",
            "expected_out": "1,Jane Doe,30,CAN"
        },
        "test_update_athlete": {
            "input": "a\ni\n1\nJane Doe\n30\nCAN\nu\n1\nJane Smith\n28\nUSA\np\nq\nq\n",
            "expected_out": "1,Jane Smith,28,USA"
        },
        "test_athlete_below_age_range": {
            "input": "a\ni\n1\nJohn Smith\n13\n21\nUSA\np\nq\nq\n",
            "expected_out": "Error: Age must be between 14 and 120"
        },
        "test_athlete_above_age_range": {
            "input": "a\ni\n1\nJohn Smith\n121\n21\nUSA\np\nq\nq\n",
            "expected_out": "Error: Age must be between 14 and 120"
        },
        "test_athlete_name_length_boundary": {
            "input": "a\ni\n4\nA very very very very very very long name that should be truncated\n23\nUSA\np\nq\nq\n",
            "expected_out": "4,A very very very very very very long name tha,23,USA"
        },
        "test_nationality_code_length_boundary": {
            "input": "a\ni\n3\nAlice Johnson\n27\nUSAA\np\nq\nq\n",
            "expected_out": "3,Alice Johnson,27,USA"
        },
        "test_erase_athlete": {
            "input": "a\ni\n2\nBob Brown\n27\nUSA\ne\n2\np\nq\nq\n",
            "expected_out": "2,Bob Brown,27,USA (not present)"
        },
        "test_duplicate_athlete_code": {
            "input": "a\ni\n5\nMichael Jordan\n35\nUSA\ni\n5\nSerena Williams\n39\nUSA\np\nq\nq\n",
            "expected_out": "Error: Athlete code must be unique"
        }
    }

    
    for key, value in event_test_cases.items():
        write_log(raw_file_address, f"{key}:\n")
        write_log(parsed_file_address, f"{key}:")
        run_test_case(value, executable, raw_file_address, parsed_file_address, 'Event')
    
    for key, value in athlete_test_cases.items():
        write_log(raw_file_address, f"{key}:\n")
        write_log(parsed_file_address, f"{key}:")
        run_test_case(value, executable, raw_file_address, parsed_file_address, 'Athlete')

#compile_and_run("test")

# Usage:
studentName = str(sys.argv[1]).split('/')[1]
#studentName = ''
print(studentName)
try:
    compile_and_run(studentName)
    print(studentName)
except:
    print(studentName,': some error')
