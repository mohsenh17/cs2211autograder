import os
import glob
import subprocess
import sys
    
def compileAndRunQ2(studentName):
    """
    Compiles and runs the student's code for assignment 2 problem 2 with various test cases.

    Args:
    - studentName (str): The name of the student directory containing the code.

    Returns:
    - None
    """
    test_cases = {
        "input_1": {"input": "1\n0\n", "expected_out": "one"},
        "input_23": {"input": "13\n0\n", "expected_out": "thirteen"},
        "input_25": {"input": "25\n0\n", "expected_out": "twenty-five"},
        "input_100": {"input": "100\n0\n", "expected_out": "one hundred"},
        "input_101": {"input": "101\n0\n", "expected_out": "one hundred and one"},
        "input_512": {"input": "512\n0\n", "expected_out": "five hundred and twelve"},
        "input_678": {"input": "678\n0\n", "expected_out": "six hundred and seventy-eight"},
        "input_843": {"input": "843\n0\n", "expected_out": "eight hundred and forty-three"},
        "input_999": {"input": "999\n0\n", "expected_out": "nine hundred and ninety-nine"},
        "input_320": {"input": "320\n0\n", "expected_out": "three hundred and twenty"}
    }
    directories = glob.glob("assignment2/{}/2*-Assignment2".format(studentName))[0]
    os.system("gcc {}/intToEnglish.c -o {}/intToEnglish.out".format(directories,directories))
    command = "./{}/intToEnglish.out".format(directories)

    w = open("assignment2/{}/q2ConvVal.txt".format(studentName), 'w')
    w.write("input, expected output, calculated output, outcome, error \n")
    for key, value in test_cases.items():
        input_data = value["input"]
        expected_output = value["expected_out"]
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=input_data)
        outcome = False
        inp  = key.split("_")[1]
        finall_out = stdout
        if expected_output in finall_out:
            outcome = True
        w.write("{}, {}, {}, {}\n".format(inp, expected_output, outcome, stderr))
        

    
    


    
studentName = str(sys.argv[1]).split('/')[1]
print(studentName)
try:
    compileAndRunQ2(studentName)
except:
    print(studentName,': some error')
