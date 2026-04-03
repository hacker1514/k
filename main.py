import colorama
from sys import exit, argv
colorama.init()
from eval_code import *
from terminal import *
from editor import *

if len(argv)==1:
    print("\033[33m::\033[31mError\033[33m:: \033[4;36marguments\033[0m\033[32m not found !")
    exit()

if argv[1]=="--terminal":
    terminal()
    exit()

if argv[1]=="--version":
    print("\033[33m::\033[35mversion\033[33m::\033[32m1.0")
    exit()

if argv[1]=="--file":
    try:
        editor(argv[2])
    except:
        print("\033[33m::\033[31mError\033[33m::\033[32mfile name not found !")
    exit()

if '.' in argv[1]:
    if argv[1].split('.')[1]=="k":
        try:
            f=open(argv[1],"r")
            code=f.read().split("\n")
            f.close()
        except:
            print(f"\033[33m::\033[31mError\033[33m::\033[32mfile \033[33m{argv[1]}\033[32m not found !")
            exit()
        try:
            for i in code:
                i=i.strip()
                if len(i)==0:
                    continue
                eval_code(i.split(' '))
        except Exception as e:
            print("\033[33m::\033[31mError\033[33m::\033[32m", e)
    else:
        print("\033[33m::\033[31mError\033[33m::\033[32mfile extension should be '\033[33m.k\033[32m' !")
        exit()
else:
    print("\033[33m::\033[31mError\033[33m:: \033[4;36marguments\033[0m\033[32m not found !")
    exit()