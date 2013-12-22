#!/bin/bash

# install requirements separately to /libs
pip install -r requirements/local.txt -t ./libs

PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LIB_DIR='./libs'
DIRS=`find $LIB_DIR -depth 1 -type d -not -name '*egg-info'`

# and now loop through the directories:
for DIR in $DIRS
  do
    DIR_NAME=${DIR#$LIB_DIR}
    # skip django since GAE provides it
    if test $DIR_NAME != '/django'
      then
        # add symlink from the libs to the project
        ln -s ${PROJECT_ROOT}/libs${DIR_NAME} ${PROJECT_ROOT}/{{ project_name }}${DIR_NAME}
        echo create symlink from /libs${DIR_NAME}
        echo to /{{ project_name }}${DIR_NAME}
    fi
  done