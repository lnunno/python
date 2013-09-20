'''
Created on Sep 17, 2013

@author: lnunno
'''
import os
import re
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
        
def compile_java(java_src_file,classpaths=None):
    classpaths = classpaths or []
    classpaths.append('.')
    path = ':'.join(classpaths)
    command('javac -cp %s %s' % (path,java_src_file))
                
def run_junit3(test_file,classpaths=None):
    classpaths = classpaths or []
    classpaths.append('.')
    classpaths.append(junit3)
    path = ':'.join(classpaths)
    command('java -cp %s junit.textui.TestRunner %s' % (path,test_file))
    
def run_junit4(test_file,classpaths=None):
    classpaths = classpaths or []
    classpaths.append('.')
    classpaths.append(junit4)
    path = ':'.join(classpaths)
    command('java -cp %s org.junit.runner.JUnitCore %s' % (path,test_file))
                
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

def make_unified_grading_file(student_list,dst,additional_content=''):
    with open(dst,'w') as f:
        for s in student_list:
            content = '''\
---
USERNAME: %s
%s
TOTAL: GRADE/100
''' % (s,additional_content) 
            f.write(content)
    print "Wrote grading file to",os.path.abspath(dst)
            

def _make_grades_file(outroot, acc, oldusername):
    p = os.path.join(outroot, oldusername)
    if not os.path.exists(p):
        os.makedirs(p)
    with open(os.path.join(p, 'grade.txt')) as f:
        f.write(acc)

def split_grading_file(grading_file,outroot):
    gf = open(grading_file)
    acc = ''
    oldusername = ''
    for line in gf.readlines():
        m = re.match('USERNAME: (\w+)', line)
        if m:
            username = m.group(1).strip()
            if acc and oldusername:
                _make_grades_file(outroot, acc, oldusername)
                oldusername = username
                acc = ''
        else:
            acc += line
            continue
    _make_grades_file(outroot, acc, username)
        
def main():
    pass

if __name__ == '__main__':
    main()
    