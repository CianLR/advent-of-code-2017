#!/bin/bash
# Usage: ../get_input.sh <day>
# Run this from inside the directory for your day, make sure the 'cookie'
# file is in the root of the repo.

set -xe

URL=http://adventofcode.com/2017/day/$1/input
COOKIE="session=$(cat ../cookie)"

wget --no-cookies --header "Cookie: $COOKIE" $URL

