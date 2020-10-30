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

# repos list
REPOS_LIST=('code_chip' 
		  	'shortcut_life'
		  	'do_exercises'
		  	'leetcode_practice'
			'project_temp')

# download the repos
if [[ ! -z $1 ]]; then
	for repo_name in ${REPOS_LIST[*]}
	do
		echo "Downloading repository ${repo_name} ..."
		git clone https://github.com/Dowayching/${repo_name}.git
		echo "Download repository ${repo_name} ok !"
		echo ""
	done
    exit 1
fi

# update the repos
for repo_name in ${REPOS_LIST[*]}
do
    echo "Updating repository ${repo_name} ..."
	pushd ${repo_name}
    git pull
    popd 
	echo "Update repository ${repo_name} ok !"
	echo ""
done
