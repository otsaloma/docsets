#!/bin/bash
set -e
ROOT_DIR="$(pwd)"
FAIL_FILE="$ROOT_DIR/index.fail"
truncate -s0 "$FAIL_FILE"
export PYTHONPATH=$ROOT_DIR:$PYTHONPATH
for DIRECTORY; do
    echo "Entering $DIRECTORY..."
    cd "$ROOT_DIR/$DIRECTORY/Contents/Resources"
    ./index.py || echo "$DIRECTORY" >> "$FAIL_FILE"
done
echo; sed 's/^/INDEX FAILED FOR /' "$FAIL_FILE"
