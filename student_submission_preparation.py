import os
import glob
import subprocess

def getStudentFiles(directoryAddress):
    """
    Extracts student submission files for assignment 2 from the given directory address.

    Args:
    - directoryAddress (str): The address of the directory containing student submission files.

    Returns:
    - None
    """
    for submission in glob.glob('{}/*'.format(directoryAddress)):
        try:
            studentName = submission.split('/')[-1].split('-')[2][1:-1]
        except:
            print("error",submission)
        os.system('mkdir assignment2/{}'.format(studentName))
        try:
            poc = subprocess.run("tar -xf {}/25*-Assignment2.tar -C assignment2/{}".format(submission, studentName), shell=True, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(studentName, "error")
            os.system("rm -r assignment2/{}".format(studentName))
