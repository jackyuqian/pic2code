#!/usr/bin/python3
with open("template.txt", "w") as fp:
    txt =  ""
    txt += 16*chr(9608) + '\n'
    for i in range(7):
        txt += chr(9608) + '\n'
    txt += "`1234567890-=\n"
    txt += "~!@#$%^&*()_+\n"
    txt += "qwertyuiop[]\\\n"
    txt += "QWERTYUIOP{}|\n"
    txt += "asdfghjkl;'\n"
    txt += 'ASDFGHJKL:"\n'
    txt += "zxcvbnm,./\n"
    txt += "ZXCVBNM<>?\n"

    print(txt, file=fp)
    print(txt)
