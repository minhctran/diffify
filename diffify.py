#!/usr/bin/env python3
import subprocess
from subprocess import PIPE
import os
import time


def flattenFile(filein, fileout):
    for line in filein:
        if '\input' in line:
            sub_name = line.strip()
            sub_name = sub_name[7:-1]
            fsub = open(sub_name+'.tex', 'r')
            flattenFile(fsub, fileout)
            fsub.close()
            print('Pulling from '+sub_name+'.tex')
        else:
            fileout.write(line)


def countdown(n):
    for x in range(n):
        print(n-x)
        time.sleep(1)


def flatten(fin_name, fout_name, commit='master'):
    if commit != 'master':
        myCommand(['git', 'checkout', commit])
    fin = open(fin_name, 'r')
    fout = open(fout_name, 'w')
    print('Flattening '+fin_name+' into '+fout_name)
    flattenFile(fin, fout)
    fin.close()
    fout.close()
    if commit != 'master':
        myCommand(['git', 'checkout', 'master'])


def myCommand(command, stdout=None, stderr=None, shell=False):
    # Excexute a terminal command
    print(command)
    output = subprocess.Popen(command, stdout=stdout, stderr=stderr, shell=shell)
    stdout, stderr = output.communicate()
    print(stdout)
    print(stderr)


def cleanup(fileList):
    # Delete temp files
    for file in fileList:
        try:
            os.remove(file)
            print('Removing '+file)
        except:
            print(file+' not found')


def pdflatex(filename):
    # compile TeX files into PDF
    try: 
        myCommand('pdflatex '+filename, stdout=None, stderr=None, shell=True)
        myCommand('bibtex '+filename[:-4], stdout=None, stderr=None, shell=True)
        myCommand('pdflatex '+filename, stdout=None, stderr=None, shell=True)
        myCommand('pdflatex '+filename, stdout=None, stderr=None, shell=True)
        latexAuxList = ['.aux', '.toc', '.log', '.syntex.gz', '.bbl', '.blg', 'Notes.bib']
        for ext in latexAuxList:
            cleanup([filename[:-4]+ext])
    except:
        print('Something went wrong. Pdflatex failed!')
        

def pathSplit(s):
    # Split path into path and file name
    slashPos = [pos for pos, char in enumerate(s) if char == '/']
#    print(slashPos)
    if slashPos:
        return s[0:slashPos[-1]+1],s[slashPos[-1]+1:]
    else:
        return '', s
#    print(s[0:slashPos[-1]+1])
#    print(s[slashPos[-1]+1:])


def diffify(main_path, old_ver, new_ver='master', make_pdf = True, clean_up = True):
    ## move to the project folder
    dir_name, fin_name = pathSplit(main_path)
    try:    
        dir_path = os.path.dirname(os.path.realpath(__file__))+'/'
    except:
        dir_path = ''
    os.chdir(dir_path+dir_name)
    
    ## name old version, current version and diff files
    flattenedOldFileName = fin_name[:-4]+'-flat-'+old_ver[:6]+'.tex'
    flattenedNewFileName = fin_name[:-4]+'-flat-'+new_ver[:6]+'.tex'
    diffFileName = fin_name[:-4]+'-diff-'+old_ver[:6]+'-vs-'+new_ver[:6]+'.tex'
    
    ### flatten the old version
    flatten(fin_name, flattenedOldFileName, commit=old_ver)
    
    ### flatten the current version
    flatten(fin_name, flattenedNewFileName, commit=new_ver)
    
    ### Make a diff file
    command = 'latexdiff '+flattenedOldFileName+' '+flattenedNewFileName+' > '+diffFileName
    myCommand(command, stdout=PIPE, stderr=PIPE, shell=True)
    
    ### Compile the diff file is make_pdf = True
    if make_pdf:
        pdflatex(diffFileName)
    
    ### Clean up if clean_up = True
    if clean_up:
        cleanup([flattenedOldFileName, flattenedNewFileName, diffFileName])
    
    print('Finished!')


#diffify(need_input=False,make_pdf=False,clean_up=False)

















