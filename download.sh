#!/bin/bash
set -e
ROOT_DIR="$(pwd)"
FAIL_FILE="$ROOT_DIR/download.fail"
truncate -s0 "$FAIL_FILE"
download () {
    NUM="$1"
    URL="$2"
    HASH=$(echo "$URL" | md5sum | cut -c 1-16)
    printf "%4d. %s %s\n" $NUM $HASH $URL
    test -s Documents/$HASH.html && return 0
    curl --fail \
         --max-time 30 \
         --output Documents/$HASH.html \
         --silent \
         "$URL"

    test -s Documents/$HASH.html
}
# Export download function for parallel.
export -f download
export SHELL=/bin/bash
for DIRECTORY; do
    echo "Entering $DIRECTORY..."
    cd "$ROOT_DIR/$DIRECTORY/Contents/Resources"
    test -f URLS || continue
    mkdir -p Documents
    cat URLS | sort -R | parallel -j8 --halt now,fail=1 download {#} {} || echo "$DIRECTORY" >> "$FAIL_FILE"
done
echo; sed 's/^/DOWNLOAD FAILED FOR /' "$FAIL_FILE"
