#!/bin/sh

set -e
FAILED=""
ROOT_DIR="$(pwd)"

for DIRECTORY; do
    echo "Entering $DIRECTORY..."
    cd "$ROOT_DIR/$DIRECTORY/Contents/Resources"
    [ -f URLS ] || continue
    mkdir -p Documents
    for URL in $(cat URLS); do
        NAME=$(echo "$URL" | md5sum | cut -c 1-16)
        echo "$NAME: $URL"
        curl -m 30 -o Documents/$NAME.html -s "$URL" || FAILED="$FAILED $DIRECTORY"
    done
done

for DIRECTORY in $FAILED; do
    echo "DOWNLOAD FAILED FOR $DIRECTORY"
done
