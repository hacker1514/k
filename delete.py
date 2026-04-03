from eval_code import variables
from fun import fun_list

def dlt(kind, name):
    kind = kind.strip()
    name = name.strip()

    if kind == "var":
        if name in variables:
            del variables[name]
        else:
            print(f"\033[33m::\033[31mError\033[33m:: \033[35mVariable '\033[33m{name}\033[35m' not found!")

    elif kind == "fun":
        f = None
        for func in fun_list:
            if func.name == name:
                f = func
                break
        if f:
            fun_list.remove(f)
        else:
            print(f"\033[33m::\033[31mError\033[33m:: \033[35mFunction '\033[33m{name}\033[35m' not found!")

    else:
        print(f"\033[33m::\033[31mError\033[33m:: \033[35mInvalid delete type '\033[33m{kind}\033[35m'! Use 'var' or 'fun'.")