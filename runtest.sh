#!/usr/bin/env bash

TESTFILE=/Users/hborcher/Documents/471223_037.tif
OUTPUT=delme.jp2

echo "Testing $TESTFILE"

runcommand="${TESTFILE} -units "PixelsPerInch" -density 300 -resample 300x ${OUTPUT}"
echo ${runcommand}
convert ${runcommand}

identify -format  "%x x %y" ${OUTPUT}
