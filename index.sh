#!/bin/bash
set -e
FAILED=""
ROOT_DIR="$(pwd)"
export PYTHONPATH=$ROOT_DIR:$PYTHONPATH
for DIRECTORY; do
    echo "Entering $DIRECTORY..."
    cd "$ROOT_DIR/$DIRECTORY/Contents/Resources"
    ./index.py || FAILED="$FAILED $DIRECTORY"
done
for DIRECTORY in $FAILED; do
    echo "INDEX FAILED FOR $DIRECTORY"
done
