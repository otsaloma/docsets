#!/bin/bash
set -e
./clean.sh "$@"
./download.sh "$@"
./index.sh "$@"
