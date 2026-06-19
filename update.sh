#!/bin/bash
set -e
./download.sh "$@"
./index.sh "$@"
echo; sed 's/^/DOWNLOAD FAILED FOR /' download.fail
echo; sed 's/^/INDEX FAILED FOR /' index.fail
