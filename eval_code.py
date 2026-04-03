variables = {}
keywords = ["display", "get", "loop", "/loop","fun","/fun","pause","import"]

from display import *
from system import *
from get import *
import loop
import fun
from pause import *

def eval_code(code):
    try:
        code = [x for x in code if x.strip()]
        if not code:
            return
        if code[0] == ".":
            loop.add_loop(" ".join(code[1:]))
            return
        if code[0] == "-":
            fun.add_fun(" ".join(code[1:]))
            return
        if code[0] == "fun":
            fun.fun(" ".join(code[1:]))
        elif code[0]=="$":
            pass
        elif code[0] == "del":
            from delete import dlt
            if len(code) < 3:
                print("\033[33m::\033[31mError\033[33m:: \033[35msyntax error for del! Usage: del var|fun name")
            else:
                dlt(code[1], code[2])
        elif code[0] == "import":
            from impt import impt
            if len(code) < 2:
                print("\033[33m::\033[31mError\033[33m:: \033[35msyntax error for import!")
            else:
                impt(code[1])
        elif code[0] == "export":
            from export import expt
            if len(code) < 2:
                print("\033[33m::\033[31mError\033[33m:: \033[35msyntax error for export! Usage: export module_name")
            else:
                expt(code[1])
        elif code[0] == "/fun":
            fun.end_fun()
        elif code[0]=="pause":
            if(len(code)==1):
                print(f"\033[33m::\033[31mError\033[33m::\033[35msyntax \033[32m error !")
            else:
                pause(code[1])
        elif code[0] == "call":
            if(len(code)==1):
                print(f"\033[33m::\033[31mError\033[33m::\033[35msyntax \033[32m error !")
            else:
                fun.call_fun(code[1], eval_code)
        elif code[0] == "loop":
            loop.loop(" ".join(code[1:]))
        elif code[0] == "/loop":
            loop.eval_loop(eval_code)
        elif code[0] == "display":
            display(" ".join(code[1:]), variables)
        elif code[0] == "get":
            if code[1]=="<":
                if len(code)===2:
                    variables[code[2]] = get()
                else:
                    print(f"\033[33m::\033[31mError\033[33m::\033[35mvariable \033[32m not found !")
            else:
                print(f"\033[33m::\033[31mError\033[33m::\033[35msyntax \033[32m error !")
        elif code[0] == "...":
            system(code)
        elif len(code) == 2:
            if code[1] in variables:
                variables[code[0]] = variables[code[1]]
            else:
                variables[code[0]] = code[1]
        else:
            print(f"\033[33m::\033[31mError\033[33m::\033[35m{code[0]}\033[32m not found !")
    except:
        print(f"\033[33m::\033[31mError\033[33m::\033[35msyntax \033[32m error !")
