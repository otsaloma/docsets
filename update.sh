#!/bin/sh
set -e
./download.sh "$@"
./index.sh "$@"
