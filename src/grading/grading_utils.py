'''
Created on Sep 17, 2013

@author: lnunno
'''
import os
import subprocess
from datetime import datetime

java_root = '/usr/share/java'
junit3 = os.path.join(java_root,'junit.jar')
junit4 = os.path.join(java_root,'junit4.jar')

def mirror_directory_tree(input_root,output_root):
    if input_root.endswith(os.sep):
        input_root = input_root[:-1]
    for dirpath,dirnames,_ in os.walk(input_root):        
        for d in dirnames:
            p = os.path.join(dirpath,d)
            relative_path = p[len(input_root)+1:]
            outpath = os.path.join(output_root,relative_path)
            if not os.path.exists(outpath):
                os.makedirs(outpath)
                
def tar_extract_specific(tar_file,elements):
    for e in elements:
        print command('tar -xzvf %s %s' % (tar_file,e))
                
def run_junit3(test_file):
    command('java -cp %s junit.textui.TestRunner %s' % (junit3,test_file))
    
def run_junit4(test_file):
    command('java -cp %s org.junit.runner.JUnitCore %s' % (junit4,test_file))
                
def command(cmd):
    try:
        return subprocess.check_output(cmd,shell=True)
    except subprocess.CalledProcessError:
        print 'ERRORS with command ', cmd
        
def calculate_late_time(turnin_file,due_date):
    turnin_time = datetime.fromtimestamp(os.path.getmtime(turnin_file))
    return turnin_time,turnin_time - due_date

def lateness_string(turnin_time,due_date):
    return '''\
DUE DATE= %s 
TURNIN TIME= %s 
TIME LATE= %s
''' % (due_date, turnin_time, turnin_time - due_date)

def get_students(student_file):
    with open(student_file) as f:
        students = f.readlines()
        students = map(lambda x: x.strip(), students)
    return students
        
def main():
    pass

if __name__ == '__main__':
    main()
    