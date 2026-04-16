from variables import variables
from exp_engine import safe_eval
def get(code):
    if len(code)!=1 and code[0]=="<":
        code.pop(0)
        for i in code:
            variables[i]=safe_eval(input("\033[32m"),variables)
    else:
        print("\033[33m::\033[31mError\033[33m::\033[4;36msyntax\033[0m\033[35m error !")
