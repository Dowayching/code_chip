#!/bin/bash
#===============================================================
# @Brief: one command to get the anto's repository from github 
# 
# @Usage: bash get_anto_github.sh [-d] 
#    -d   download the repos first time
# 
# @Remark: 
#   1. for first time, copy this script to project root folder,
#      and run "bash get_anto_github.sh -d", then remove it. 
#      Afterward, just run this script on /script_life/bash
#   2.it is for linux / MacOS, install cygwin if if you to run
#      under windows
#===============================================================

# download the repos
if [[ ! -z $1 ]]; then
    git clone https://github.com/Dowayching/code_chip.git
    git clone https://github.com/Dowayching/shortcut_life.git
    git clone https://github.com/Dowayching/do_exercises.git
    exit 1
fi

# switch to project root directory
cd ../..

# update the repos
for repos in */; do
    echo $repos
    pushd $repos
    git pull
    popd
done

# switch back to the directory that this script resides
cd script_life/bash


