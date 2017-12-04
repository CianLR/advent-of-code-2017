#!/bin/bash
# Usage: ./submit <day> <level> <python3_file>
# Run this from inside the directory for your day, make sure the 'cookie'
# file is in the root of the repo.

set -xe

URL=http://adventofcode.com/2017/day/$1/answer
COOKIE="session=$(cat ../cookie)"

curl -d "level=$2&answer=$(python3 $3 < input)" --cookie $COOKIE $URL

