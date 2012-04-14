#!/bin/bash
# bootstrap.sh
#
# create a new project based on py-boostrap in a new location and rename all
# references to boostrap to your projects name.
#
# usage: boostrap.sh <project name> <project path>
# example: boostrap.sh tacobell ~/Projects/Tacobell

USAGE="usage: $0 <project name> <project path>"


# take lower case word and return a proper cased version of it
function proper_case {
    echo -n "${1:0:1}" | tr "[:lower:]" "[:upper:]"
    echo "${1:1}"
}


# handle arguments
if [ -z "$1" ] ; then
    echo "missing project name argument"
    echo $USAGE
    exit 1
fi
PROJECT_NAME="$1"
PROJECT_NAME_PROPER=$(proper_case $PROJECT_NAME)

if [ -z "$2" ] ; then
    echo "missing project path argument"
    echo $USAGE
    exit 1
fi
PROJECT_PATH="$2"


# setup new project dir
mkdir -p $PROJECT_PATH

# copy over py-boostrap
git archive master | tar -x -C $PROJECT_PATH

# replace all references to boostrap in project files
for f in $(grep -lr bootstrap $PROJECT_PATH); do
    sed -e "s/bootstrap/${PROJECT_NAME}/g" < $f > $f.tmp && mv $f.tmp $f
done

# replace all references to Bootstrap in project files
for f in $(grep -lr Bootstrap $PROJECT_PATH); do
    sed -e "s/Bootstrap/${PROJECT_NAME_PROPER}/g" < $f > $f.tmp && mv $f.tmp $f
done

# rename project module directory
mv ${PROJECT_PATH}/bootstrap ${PROJECT_PATH}/${PROJECT_NAME}

# echo blurb
echo "bootstraping of $PROJECT_NAME to $PROJECT_PATH was successful."

