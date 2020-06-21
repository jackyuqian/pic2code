#!/usr/bin/python3
with open("template.txt", "w") as fp:
    txt =  ""
    txt += 16*chr(9608) + '\n'
    for i in range(7):
        txt += chr(9608) + '\n'
    txt += "abcdefghigklmnopqrstuvwxyz\n"
    txt += "ABCDEFGHIGKLMNOPQRSTUVWXYZ\n"
    print(txt, file=fp)
    print(txt)
