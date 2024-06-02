import os
import glob
import subprocess
import re
import sys


def extract_floats(text):
    """
    Extracts floating-point numbers from the given text using regular expression.

    Args:
    - text (str): The input text from which floating-point numbers need to be extracted.

    Returns:
    - list: A list of floating-point numbers extracted from the text.
    """
    pattern = r"\d*\.\d+|\d+\.\d*"
    floats = re.findall(pattern, text)
    floats = [float(num) for num in floats]

    return floats  

def compileAndRunQ1(studentName):
    """
    Compiles and runs the student's code for assignment 2 problem 1 with various test cases.

    Args:
    - studentName (str): The name of the student directory containing the code.

    Returns:
    - None
    """
    directories = glob.glob("assignment2/{}/2*-Assignment2".format(studentName))[0]
    os.system("gcc {}/converter.c -o {}/converter.out".format(directories,directories))
    command = "./{}/converter.out".format(directories)
    test_cases = {
        "input_GtoO_2.5": {"input": "1\nG\n2.5\n5\n", "expected_out": 0.088175},
        "input_GtoO_2": {"input": "1\nG\n2\n5\n", "expected_out": 0.07054},
        "input_GtoO_1": {"input": "1\nG\n1\n5\n", "expected_out": 0.03527},
        
        "input_OtoG_1": {"input": "1\nO\n1\n5\n", "expected_out": 28.35},
        "input_OtoG_2": {"input": "1\nO\n2\n5\n", "expected_out": 56.7},
        "input_OtoG_2.5": {"input": "1\nO\n2.5\n5\n", "expected_out": 70.88},
        
        "input_MtoY_1": {"input": "2\nM\n1\n5\n", "expected_out": 1.196},
        "input_MtoY_100": {"input": "2\nM\n100\n5\n", "expected_out": 119.6},
        "input_MtoY_10.43": {"input": "2\nM\n10.43\n5\n", "expected_out": 12.47},
        
        "input_YtoM_10.43": {"input": "2\nY\n10.43\n5\n", "expected_out": 8.72},
        "input_YtoM_100": {"input": "2\nY\n100\n5\n", "expected_out": 83.6},
        "input_YtoM_1": {"input": "2\nY\n1\n5\n", "expected_out": 0.836},
        
        "input_LtoP_1": {"input": "3\nL\n1\n5\n", "expected_out": 2.11},
        "input_LtoP_20": {"input": "3\nL\n20\n5\n", "expected_out": 42.2},
        "input_LtoP_20.61": {"input": "3\nL\n20.61\n5\n", "expected_out": 43.48},
        
        "input_PtoL_20.61": {"input": "3\nP\n20.61\n5\n", "expected_out": 9.76},
        "input_PtoL_20": {"input": "3\nP\n20\n5\n", "expected_out": 9.47},
        "input_PtoL_1": {"input": "3\nP\n1\n5\n", "expected_out": 0.47},
        
        "input_MtoF_1": {"input": "4\nM\n1\n5\n", "expected_out": 3.28},
        "input_MtoF_150": {"input": "4\nM\n150\n5\n", "expected_out": 492},
        "input_MtoF_150.61": {"input": "4\nM\n150.61\n5\n", "expected_out": 494},
        
        "input_FtoM_150.61": {"input": "4\nF\n150.61\n5\n", "expected_out": 45.92},
        "input_FtoM_150": {"input": "4\nF\n150\n5\n", "expected_out": 45.731},
        "input_FtoM_1": {"input": "4\nF\n1\n5\n", "expected_out": 0.304},
        "input_quit_none":{"input":"5\n", 'expected_out':None},
        "input_nonvalid1_none":{"input":"500\n5\n", 'expected_out':None},
        "input_nonvalid2_none":{"input":"2\nZ\n5\n", 'expected_out':None}
    }
    w = open("assignment2/{}/convVal.txt".format(studentName), 'w')
    w.write("conversion type, input, expected output, calculated output, outcome, error \n")
    for key, value in test_cases.items():
        input_data = value["input"]
        expected_output = value["expected_out"]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=input_data)
        outcome = False
        convType, inp  = key.split("_")[1:]
        candidate_out = stdout.strip()
        if not 'quit' in key and not 'nonvalid' in key:
            #print(key)
            finall_out = stdout
            candidate_out = extract_floats(finall_out)
            for item in candidate_out:
                if abs((expected_output-item)<0.2):
                    outcome = True
                    calculated =item
        if len(stderr)==0:
            outcome = True
        w.write("{}, {}, {}, {}, {}, {}\n".format(convType, inp, expected_output, calculated, outcome, stderr))

studentName = str(sys.argv[1]).split('/')[1]
print(studentName)
try:
    compileAndRunQ1(studentName)
except:
    print(studentName,': some error')
