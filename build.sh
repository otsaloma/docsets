#!/bin/sh
set -e
if [ $# -lt 1 ]; then
    echo "Download and index documentation for use."
    echo "Usage: ./$(basename "$0") DIRECTORY..."
    exit 1
fi
DOWNLOAD_FAILED=""
INDEX_FAILED=""
for DIRECTORY; do
    echo "Entering $DIRECTORY..."
    cd "$DIRECTORY/Contents/Resources"
    DOCSET="$(basename $DIRECTORY .docset)"
    [ -f download ] && ./download || DOWNLOAD_FAILED="$DOWNLOAD_FAILED $DOCSET"
    [ -f index ] && ./index || INDEX_FAILED="$INDEX_FAILED $DOCSET"
    cd "../../.."
done
echo ""
for DOCSET in $DOWNLOAD_FAILED; do echo "DOWNLOAD FAILED FOR $DOCSET"; done
for DOCSET in $INDEX_FAILED; do echo "INDEX FAILED FOR $DOCSET"; done
