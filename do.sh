#!/bin/bash
mkdir -p output
rm -rf output/$1.v
touch output/$1.v
#for ifile in pics/$1/*.png
#do
#    ofile_ext=$(basename "$ifile")
#    ofile=./pics/$1/${ofile_ext%.*}.v
#   ./gen_txt.py -i $ifile -o $ofile -t templ_black.png -c Black 
#    echo  $ofile Done!
#done
for ifile in pics/$1/*.v
do
    cat $ifile >> ./output/$1.v
done
