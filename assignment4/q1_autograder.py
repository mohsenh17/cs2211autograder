import os
import subprocess
import glob
import re
import sys

def replace_whitespace_with_comma(text):
    """
    Replaces all whitespace characters in the given text with commas.

    Args:
        text (str): The input string with whitespace.

    Returns:
        str: The modified string with whitespace replaced by commas.
    """
    result = re.sub(r'\s+', ',', text)
    return result

def write_log(fileAddress, message):
    """
    Writes a message to a log file, appending it to the end of the file.

    Args:
        fileAddress (str): The path to the log file.
        message (str): The message to be written to the log file.
    """
    w = open(fileAddress, 'a+')
    w.write(message)

    



def run_test_case(test_case, executable, rawFileAddress, parsedFileAddress):
    """
    Runs a test case by executing the provided executable with the test case input, 
    compares the output to the expected output, and logs the results.

    Args:
        test_case (dict): A dictionary containing the input and expected output for the test case.
        executable (str): The path to the executable to be tested.
        rawFileAddress (str): The path to the log file for raw output.
        parsedFileAddress (str): The path to the log file for parsed results.

    Returns:
        bool: True if the test case passes, False otherwise.
    """
    process = subprocess.Popen([executable], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=test_case["input"])
    if stderr:
        print(f"Error running the test case '{test_case}':\n{stderr}")
        return False
    expected_output = test_case["expected_out"]
    producedMessage = replace_whitespace_with_comma(stdout[stdout.find('\n', stdout.find('Event Code')):stdout.find('Enter', stdout.find('Event Code'))].strip())
    if not expected_output in replace_whitespace_with_comma(stdout):
        write_log(parsedFileAddress, "\n\texpected_output:"+expected_output)
        write_log(parsedFileAddress, "\n\tcode_output:"+producedMessage+'\n')
        write_log(rawFileAddress, "\n"+stdout+'\n\n\n\n\n')
    else:
        write_log(parsedFileAddress, "\t passed\n")
        
    return expected_output in replace_whitespace_with_comma(stdout)


def compile_and_run(studentName):
    """
    Compiles the C program for a given student and runs a series of test cases,
    logging the results of each test case.

    Args:
        studentName (str): The name of the student whose program is being tested.

    Returns:
        None
    """
    directories = glob.glob(f"subs/{studentName}/2*-Assignment4")
    if not directories:
        print("Assignment directory not found.")
        return
    directory = directories[0]

    compile_command = f"gcc {directory}/sport_db.c -o {directory}/sport_db.out"
    compile_process = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if compile_process.returncode != 0:
        print(f"Compilation failed:\n{compile_process.stderr.decode()}")
        return

    executable = f"{directory}/sport_db.out"
    rawFileAddress = f"subs/{studentName}/raw.txt"
    parsedFileAddress = f"subs/{studentName}/parsed.txt"

    
    test_cases = {
        "test_insert_event": {
            "input": "i\n0\nField Hockey\n12\nM\np\nq\n",
            "expected_out": "0,Field,Hockey,12,M"
        },
        "test_print_events": {
            "input": "i\n1\nHandball\n16\nX\ni\n2\nSwimming\n14\nW\ni\n3\nCycling\n20\nM\np\nq\n",
            "expected_out": "1,Handball,16,X,2,Swimming,14,W,3,Cycling,20,M"
        },
        "test_search_event": {
            "input": "i\n1\nHandball\n16\nX\ns\n1\nq\n",
            "expected_out": "1,Handball,16,X"
        },
        "test_update_event": {
            "input": "i\n1\nHandball\n16\nX\nu\n1\nBasketball\n15\nM\np\nq\n",
            "expected_out": "1,Basketball,15,M"
        },
        "test_event_below_range": {
            "input": "i\n1\nSoccer\n8\ni\n1\nSoccer\n13\nM\np\nq\n",
            "expected_out": "1,Soccer,13,M"
        },
        "test_event_above_range": {
            "input": "i\n1\nSoccer\n800\ni\n1\nSoccer\n13\nM\np\nq\n",
            "expected_out": "1,Soccer,13,M"
        },
        "test_event_name_length_boundary": {
            "input": "i\n4\nA very very very very very very long event name that should be truncated\n13\nM\np\nq\n",
            "expected_out": "4,A,very,very,very,very,very,very,long,event,name,t,13,M"
        },
        "test_invalid_gender_entry": {
            "input": "i\n3\nSwimming\n30\nA\ni\n1\nSoccer\n13\nM\np\nq\n",
            "expected_out": "1,Soccer,13,M"
        }


    }
    
    
    for key, value in test_cases.items():
        write_log(rawFileAddress, key+':\n')
        write_log(parsedFileAddress, key+':')
        run_test_case(value, executable, rawFileAddress, parsedFileAddress)
        
        
    

compile_and_run("Zhantore_Borangali")

exit()
studentName = str(sys.argv[1]).split('/')[1]
#studentName = ''
print(studentName)
try:
    compile_and_run(studentName)
    print(studentName)
except:
    print(studentName,': some error')
