import os
def system(cmd):
    cmd = " ".join(cmd[1:]) if len(cmd) > 1 else ""
    os.system(cmd)