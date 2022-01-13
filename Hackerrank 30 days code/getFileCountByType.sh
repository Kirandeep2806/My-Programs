#!/bin/bash

getContents=`ls`
pythonFileCount=`ls | grep -c ".*.py"`
cppFileCount=`ls | grep -c ".*.cpp"`
javaFileCount=`ls | grep -c ".*.java"`
echo "Python : $pythonFileCount"
echo "CPP    : $cppFileCount"
echo "Java   : $javaFileCount"

