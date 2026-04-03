stack = []
top = -1

class LoopContext:
    def __init__(self):
        self.it = 0
        self.start_loop = None
        self.end_loop = None

class loop_node:
    def __init__(self, line):
        self.line = line
        self.next = None

def loop(text):
    global top
    number = text.strip()
    ctx = LoopContext()
    if number == "inf":
        ctx.it = -1
    else:
        try:
            ctx.it = int(number)
        except:
            print("\033[33m::\033[31mError\033[33m::\033[35minvalid number!\033[0m")
            return
    stack.append(ctx)
    top += 1

def add_loop(text):
    global top
    if top < 0:
        return
    c = loop_node(text)
    ctx = stack[top]
    if ctx.start_loop is None:
        ctx.start_loop = ctx.end_loop = c
    else:
        ctx.end_loop.next = c
        ctx.end_loop = c

def eval_loop(func):
    global top
    if top < 0:
        return
    ctx = stack[top]
    it = ctx.it
    start_loop = ctx.start_loop
    try:
        if it == -1:
            while True:
                temp = start_loop
                while temp:
                    func(temp.line.split(" "))
                    temp = temp.next
        else:
            for _ in range(it):
                temp = start_loop
                while temp:
                    func(temp.line.split(" "))
                    temp = temp.next
    except KeyboardInterrupt:
        print("\n\033[33m::\033[36mInfo\033[33m::\033[32m Loop stopped\033[0m")
    ctx.start_loop = None
    ctx.end_loop = None
    stack.pop()
    top -= 1