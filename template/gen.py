#!/usr/bin/python3
with open("template.txt", "w") as fp:
    txt =  ""
    txt += 64*chr(9608) + '\n'
    for i in range(7):
        txt += chr(9608) + '\n'
    txt += "`1234567890-="
    txt += "~!@#$%^&*()_+"
    txt += "qwertyuiop[]\\"
    txt += "QWERTYUIOP{}|"
    txt += "asdfghjkl;'"
    txt += 'ASDFGHJKL:"'
    txt += "zxcvbnm,./"
    txt += "ZXCVBNM<>?"
    txt += " "
    txt += "\n"

    print(txt, file=fp)
    print(txt)
