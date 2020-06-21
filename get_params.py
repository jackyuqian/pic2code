#!/usr/bin/python3
import sys, getopt
from PIL import Image
import numpy as np

def find_longest_substring(lst_in, ele):
    # return : [start, len]
    ele_start   = -1
    ele_length  = 0
    rslt        = [-1, 0]
    for idx in range(len(lst_in)):
        if lst_in[idx] == ele:
            if ele_start == -1:
                ele_start   = idx
            ele_length  += 1
        elif ele_length != 0:
            if ele_length > rslt[1]:
                rslt    = [ele_start, ele_length]
            ele_start   = -1
            ele_length  = 0
    return rslt

def get_params(ftempl):
    # read template and pre-process
    img_rgb = Image.open(ftempl)
    img_bin = img_rgb.convert('L')
    img_arr = np.array(img_bin) > 128
    
    # find care colume
    care_col    = np.argmax(np.sum(img_arr, axis = 0))
    col_start, col_length   = find_longest_substring(img_arr[:, care_col], True)
    col_win     = (col_length / 8)

    # find care row 
    care_row    =np.argmax(np.sum(img_arr, axis = 1))
    row_start, row_length   = find_longest_substring(img_arr[care_row, :], True)
    row_win     = (row_length / 16)
    
    return [row_start, col_start, row_win, col_win]

def print_usage():
    print('./gen_params.py -i <template>')

def main(argv):
    # Get Arguments
    try:
        opts, args    = getopt.getopt(argv,"i:")
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i"):
            fin = arg
    row_start, col_start, row_win, col_win  = get_params(fin)
    print("row start= %d" % row_start)
    print("col start= %d" % col_start)
    print("row win  = %d" % row_win)
    print("col win  = %d" % col_win)


if __name__ == '__main__':
    main(sys.argv[1:])



