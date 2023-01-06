#!/bin/sh
set -e
FAILED=""
ROOT_DIR="$(pwd)"
download () {
    NAME=$(echo "$1" | md5sum | cut -c 1-16)
    echo "$NAME: $1"
    curl -m 30 -o Documents/$NAME.html -s "$1" || FAILED="$FAILED $DIRECTORY"
}
for DIRECTORY; do
    echo "Entering $DIRECTORY..."
    cd "$ROOT_DIR/$DIRECTORY/Contents/Resources"
    [ -f URLS ] || continue
    mkdir -p Documents
    for URL in $(cat URLS); do download $URL; done
    find Documents -empty -delete
done
for DIRECTORY in $FAILED; do
    echo "DOWNLOAD FAILED FOR $DIRECTORY"
done
