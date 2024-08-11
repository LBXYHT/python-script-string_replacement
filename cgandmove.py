#!/usr/bin/env python3
# coding=utf-8

#above is the necessity for most python script
import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('-src', default='my', help='set source folder name')
parser.add_argument('-dst', help='set destination folder name')
args = parser.parse_args()

#input oldstring to replace
oldstr = args.src
newstr = args.dst

#old path
oldpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), oldstr)
print("old path:    ", oldpath)
newpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), newstr)
print("new path:    ", newpath)

shutil.copytree(oldpath, newpath)

def change_name(newpath, oldstr, newstr):
    filelist = os.listdir(newpath)
    #check all files in filelist
    for file in filelist:
        olddir = os.path.join(newpath, file)
        if os.path.isdir(olddir):
            dirname = file.replace(oldstr, newstr)
            newdir = os.path.join(newpath, dirname)
            os.rename(olddir, newdir)
            change_name(newdir, oldstr, newstr)
            continue
        else:
            #input new filepath and new filename
            new_file = file.replace(oldstr, newstr)
            newdir = os.path.join(newpath, new_file)

            #input str and new replace string
            os.rename(olddir, newdir)
    
def change_content(newpath, oldstr, newstr):
    filelist2 = os.listdir(newpath)
    pattern = oldstr
    OLDSTR = oldstr.upper()
    pattern1 = OLDSTR
    NEWSTR = newstr.upper()
    for file in filelist2:
        subfile = os.path.join(newpath, file)
        #change strings in content
        if os.path.isdir(subfile):
            change_content(subfile, oldstr, newstr)
            continue
        else:
            newdir = os.path.join(newpath, file)
            with open(newdir, 'r') as f:
                lines = f.readlines()
                ss = ""
                for line in lines:
                    if (line.find(pattern)):
                        line = line.replace(oldstr, newstr)
                    if (line.find(pattern1)):
                        line = line.replace(OLDSTR, NEWSTR)
                        
                    ss += line
                    
            with open(newdir, 'w', encoding='utf-8') as f:
                f.write(ss)
    
change_name(newpath, oldstr, newstr)
change_content(newpath, oldstr, newstr)

print("Over".center(20, '='))