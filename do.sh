#!/bin/bash
mkdir -p output
for ifile in ./pics/*.png
do
    ofile_ext=$(basename "$ifile")
    ofile=./output/${ofile_ext%.*}.v
    ./gen_txt.py -i $ifile -o test_1.v -t templ_black.png -c Black 
    echo  $ofile Done!
done
