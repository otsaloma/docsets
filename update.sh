#!/bin/bash
set -e
./download.sh "$@"
./index.sh "$@"
