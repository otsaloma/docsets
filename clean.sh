#!/bin/sh
set -e
ROOT_DIR="$(pwd)"
for DIRECTORY; do
    echo "Entering $DIRECTORY..."
    cd "$ROOT_DIR/$DIRECTORY/Contents/Resources"
    rm -rfv Documents docSet.dsidx
done
