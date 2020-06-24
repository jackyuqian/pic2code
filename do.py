#!/usr/bin/python3 -B
import os, sys
os.system('mkdir -p output')
for dirpath, dirname, filename in os.walk('pics'):
    if dirpath != 'pics':
        print(dirpath, filename)
        for idx in range(len(filename)):
            ifile       = dirpath + '/' + str(idx) + '.png'
            ofile       = 'output/' + str(idx) + '.v'
            final_file  = 'output/' + dirpath.split('/')[-1] + '.v'
            os.system('./gen_txt.py -i %s -o %s -t templ_black.png -c Black' % (ifile, ofile)) 
            os.system('cat %s >> %s' %(ofile, final_file))
            os.system('rm %s' % ofile)
   

