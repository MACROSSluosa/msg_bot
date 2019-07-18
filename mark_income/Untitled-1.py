#!/usr/bin/python

import os, sys

# Open a file
path = "/Users/mac/pythoncode/"
dirs = os.listdir(path)

# This would print all the files and directories
for file in dirs:
   print file