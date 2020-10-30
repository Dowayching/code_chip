#!/bin/bash
#===============================================================
# @Brief: list dependencies of shared libraries in current path
# 
# @Usage: run this script
# 
# @Remark: 
#===============================================================


for file in ./*
do 
    echo "file: ${file}"
    readelf -d ${file} | grep NEEDED
    echo "----------------------------"
done
