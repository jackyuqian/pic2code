#!/usr/bin/python3 -B
import sys, getopt
from PIL import Image
import numpy as np
from parse_template import parse_template

def get_txt(row_start, col_start, row_win, col_win, ctempl_dict, fin):
    # read template and pre-process
    img_rgb = Image.open(fin)
    img_bin = img_rgb.convert('L')
    img_arr = np.array(img_bin) > 50
    Image.fromarray(img_arr).show()
    for row in range(row_start, img_arr.shape[0], row_win):
        for col in range(col_start, img_arr.shape[1], col_win):
            for key, val in ctempl_dict.items():
                if img_arr[row : row + row_win, col : col + col_win].shape != val.shape:
                    break
                elif (img_arr[row : row + row_win, col : col + col_win] == val).all():
                    print(key, end = '')
                    break
        print('\n')
            
        

def print_usage():
    print('./gen_txt.py -i <file>')

def main(argv):
    # Get Arguments
    try:
        opts, args    = getopt.getopt(argv,"i:t:")
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i"):
            fin     = arg
        elif opt in ("-t"):
            ftempl  = arg
    row_start, col_start, row_win, col_win, ctempl_dict = parse_template(ftempl)
    get_txt(row_start, col_start, row_win, col_win, ctempl_dict, fin)
    print("row start= %d" % row_start)
    print("col start= %d" % col_start)
    print("row win  = %d" % row_win)
    print("col win  = %d" % col_win)


if __name__ == '__main__':
    main(sys.argv[1:])



