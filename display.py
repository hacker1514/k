def display(content, variables):
    content = content.strip()
    if not content.startswith('>'):
        print("\033[33m::\033[31mError\033[33m::\033[35msyntax\033[32m error !")
        return
    content = content[1:].strip()
    if content.startswith('"') and content.endswith('"'):
        text = content[1:-1]
        print(f"\033[36m{text}")
    elif content in variables:
        print(f"\033[36m{variables[content]}")
    else:
        print("\033[33m::\033[31mError\033[33m::\033[35msyntax\033[32m error !")