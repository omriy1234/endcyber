# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import simpledialog
import webbrowser

def caesar2(a):
    p=3
    s = ord(a) - p % 26
    if ord(a)>= ord("A") and ord(a)<= ord("Z"):
        if s <= ord("Z"):
            b = s
        else:
            b = s + 26
        return chr(b)
    else:
        if s <= ord("z"):
            b = s
        else:
            b = s + 26
        return chr(b)

def caesar(a , p):
    s = ord(a) + p
    if p == 26 or p <= 27 and s > ord("z"):
            b = s - 26
    elif s <= ord("z"):
        b = s
    else:
        m = (s - ord("z")) / 26 + 1
        b = s - (m * 26)
    return chr(b)

def anbo(a):
    if ord(a) >= ord('a') and ord(a)<=ord('m'):
        char1=ord('a')
        num = 0
        while num + ord('a') != ord(a):
         num = num + 1
         char1 = char1 + 1
        b = ord('n') + num
        return chr(b)

    elif ord(a) >= ord('n') and ord(a)<=ord('z'):
        char1=ord('n')
        num = 0
        while num + ord('n') != ord(a):
         num = num + 1
         char1 = char1 + 1
        b = ord('a') + num
        return chr(b)

    elif ord(a) >= ord('A') and ord(a)<=ord('M'):
        char1=ord('A')
        num = 0
        while num + ord('A') != ord(a):
         num = num + 1
         char1 = char1 + 1
        b = ord('N') + num
        return chr(b)

    else:
        char1=ord('N')
        num = 0
        while num + ord('N') != ord(a):
         num = num + 1
         char1 = char1 + 1
        b = ord('A') + num
        return chr(b)

def azby(a):
    a = a
    if ord(a) >= ord('a') and ord(a)<=ord('z'):
        char1=ord('a')
        num = 0
        while num + ord('a') != ord(a):
         num = num + 1
         char1 = char1 + 1

        b = ord('z') - num
        return (chr(b))

    else:
        char1=ord('A')
        num = 0
        while num + ord('A') != ord(a):
         num = num + 1
         char1 = char1 + 1

        b = ord('Z') - num
        return (chr(b))


def main():
    cyber = "cyber"
    bool = True
    while (bool):
        bool = False
        ROOT = tk.Tk()
        ROOT.withdraw()
        enter = simpledialog.askstring(title="",prompt="enter 'cyber' in azby ")
        ROOT.destroy()
        i = 0
        if str(enter) == 'None':
            bool = True
        else:
            while i < len(enter) and i < len(cyber):
                if len(enter) != len(cyber) or azby(enter[i]) != cyber[i]:
                    bool = True
                print (azby(cyber[i]))
                i += 1

    bool = True
    while (bool):
        bool = False
        ROOT = tk.Tk()
        ROOT.withdraw()
        enter = simpledialog.askstring(title="",prompt="enter 'cyber' in anbo ")
        ROOT.destroy()
        i = 0
        if str(enter) == 'None':
            bool = True
        else:
            while i < len(enter) and i < len(cyber):
                if len(enter) != len(cyber) or anbo(enter[i]) != cyber[i]:
                    bool = True
                print (anbo(cyber[i]))

                i += 1

    bool = True
    while (bool):
        ROOT = tk.Tk()
        ROOT.withdraw()
        enter = simpledialog.askstring(title="",prompt="enter 'cyber' in Caesar cipher 3 ")
        ROOT.destroy()
        x =0
        r = ""
        while x < len(cyber):
            a =cyber[x]
            x = x+1
            if a ==" ":
                r= r + " "
            else:
                l = caesar(a, 3)
                r = r + l
        print (r)
        if r == enter:
            bool = False



    r = ""
    x =0
    f = "kwwsv=22vlwhv1jrrjoh1frp2ylhz2hqgfbehu"
    while x < len(f):
        a =f[x]
        x = x+1
        if a ==" ":
            r= r + " "
        else:
            l = caesar2(a)
            r = r + l

    l = r.split("_")

    print (l[0] + "y" + l[1])

    webbrowser.open(l[0] + "y" + l[1])












if __name__ == '__main__':
    main()