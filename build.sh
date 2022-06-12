#!/bin/bash
## USAGE:
##   build.sh [-h] [generate|commit|push|publish|sync|serve]
##
## OPTIONS:
##   -h        Print this help and exit
##   generate  Generate the pykyll pages
##   commit    Commit all the changes locally. This will NOT push changes to the
##             remote
##   push      Push the changes to the remote repo
##   publish   Generate the pages, commit the changes and then push everything
##             to the remote repo. Same as "./build.sh generate commit push"
##   serve     Start the server to test changes locally
##   sync      Pull latest changes from the pykyll project
##
## NOTE:
##  This should be called always from the root of the project!

set -e

SRC_BRANCH=gh-pages
CFG=config.json
PYKYLL_PATH=gen

function generate() {
    env PYTHONPATH=$PYKYLL_PATH python3 $PYKYLL_PATH/pykyll.py -cfg $CFG
}

function commit() {
    read -p "Enter commit message: " cmtMsg
    git add -A
    git commit -m "$cmtMsg"
}

function push() {
    git push origin $SRC_BRANCH
}

function publish() {
    generate
    commit
    push
}

function serve() {
    env PYTHONPATH=$PYKYLL_PATH python3 $PYKYLL_PATH/pykyll.py -serve
}

function printHelp() {
    grep '^##' $1 | sed -e 's/^##//' -e 's/^ //'
}

function checkRoot() {
    if [ ! -d ".git" ]; then
        echo "**ERROR** You are not at the root of this project!"
        exit -1
    fi
}

function clone() {
    if [ ! -d $PYKYLL_PATH ]; then
        git clone git@github.com:teju85/pykyll.git $PYKYLL_PATH
    fi
}

function sync() {
    cd $PYKYLL_PATH
    git pull origin main
}

checkRoot
clone
while [ "$1" != "" ]; do
    case "$1" in
        "generate")
            generate
            shift;;
        "commit")
            commit
            shift;;
        "push")
            push
            shift;;
        "publish")
            publish
            shift;;
        "sync")
            sync
            shift;;
        "serve")
            serve
            shift;;
        "-h")
            printHelp $0
            shift
            exit 0;;
        *)
            echo "**ERROR** Bad arg '$1'! Use '-h' option for the right usage."
            shift
            exit -1;;
    esac
done
