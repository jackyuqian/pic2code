#!/usr/bin/python3 -B
import sys, getopt
from PIL import Image
import numpy as np
from parse_template import parse_template

def get_txt(row_start, col_start, row_win, col_win, ctempl_dict, fin, char_color):
    # read template and pre-process
    img_rgb = Image.open(fin)
    img_bin = img_rgb.convert('L')
    if char_color == "Black":
        img_arr = np.array(img_bin) < 180
    else:
        img_arr = np.array(img_bin) > 40
    #Image.fromarray(img_arr).show()
    txt     = []
    min_norm= 99999
    for row in range(row_start, img_arr.shape[0], row_win):
        txt.append("")
        for col in range(col_start, img_arr.shape[1], col_win):
            min_norm        = 99999
            key_selected    = ''
            for key, val in ctempl_dict.items():
                if img_arr[row : row + row_win, col : col + col_win].shape != val.shape:
                    break
                else:
                    if np.linalg.norm(img_arr[row : row + row_win, col : col + col_win] ^ val) <= min_norm:
                        min_norm        = np.linalg.norm(img_arr[row : row + row_win, col : col + col_win] ^ val)
                        key_selected    = key

            if min_norm > 10:
                txt[-1] += ' '
            else:
                txt[-1] += key_selected
        txt[-1] = txt[-1].rstrip()
        print(txt[-1])
    return txt

def print_usage():
    print('./gen_txt.py -i <file> -t <ftempl -c Write/Black')

def main(argv):
    char_color  = "Black"
    # Get Arguments
    try:
        opts, args    = getopt.getopt(argv,"i:t:c:")
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i"):
            fin         = arg
            fout        = fin.split('.')[0] + '.v'
        elif opt in ("-t"):
            ftempl      = arg
        elif opt in ("-c"):
            char_color  = arg
    row_start, col_start, row_win, col_win, ctempl_dict = parse_template(ftempl, char_color)
    txt = get_txt(row_start, col_start, row_win, col_win, ctempl_dict, fin, char_color)
    with open(fout, 'w') as fp:
        for line in txt:
            print(line, file = fp)
    print("\n==========================")
    print("row start= %d" % row_start)
    print("col start= %d" % col_start)
    print("row win  = %d" % row_win)
    print("col win  = %d" % col_win)


if __name__ == '__main__':
    main(sys.argv[1:])



