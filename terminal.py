from eval_code import *

def help():
    print("\n\033[1;33m+============================================================+\033[0m")
    print("\033[1;33m|                    \033[1;36mK LANGUAGE TERMINAL\033[1;33m                     |\033[0m")
    print("\033[1;33m+============================================================+\033[0m\n")

    print("\033[1;36mDeveloper :\033[0m Niranjan Kumar K")
    print("\033[1;36mPurpose   :\033[0m Custom scripting and learning environment\n")

    print("\033[1;33m+---------------------- CORE COMMANDS -----------------------+\033[0m")
    print("\033[32mdisplay > \"text\"       :\033[0m print output")
    print("\033[32ma 10                   :\033[0m create variable")
    print("\033[32ma 20                   :\033[0m update variable")
    print("\033[32ma b                    :\033[0m copy value")
    print("\033[32mget a                  :\033[0m fetch value\n")

    print("\033[1;33m+---------------------- FLOW CONTROL ------------------------+\033[0m")
    print("\033[32mloop n                 :\033[0m repeat n times")
    print("\033[32m. <statement>          :\033[0m add line to loop")
    print("\033[32m/loop                  :\033[0m execute loop\n")

    print("\033[1;33m+---------------------- FUNCTIONS ---------------------------+\033[0m")
    print("\033[32mfun name               :\033[0m define function")
    print("\033[32m- <statement>          :\033[0m add line to function")
    print("\033[32m/fun                   :\033[0m end function")
    print("\033[32mname                   :\033[0m call function\n")

    print("\033[1;33m+---------------------- SYSTEM ------------------------------+\033[0m")
    print("\033[32m... command            :\033[0m execute system command")
    print("\033[32mpause n                :\033[0m delay execution (seconds)\n")

    print("\033[1;33m+---------------------- SPECIAL -----------------------------+\033[0m")
    print("\033[32m$                     :\033[0m comment line")
    print("\033[32mhelp                  :\033[0m show this help")
    print("\033[32m_exit                 :\033[0m exit terminal")
    print("\033[32m--version             :\033[0m version of k language\n")

    print("\033[1;33m+---------------------- EXAMPLES ----------------------------+\033[0m")
    print("\033[32mloop 3\033[0m")
    print("\033[32m. display > \"hello\"\033[0m")
    print("\033[32m/loop\033[0m\n")

    print("\033[32mfun greet\033[0m")
    print("\033[32m- display > \"hi\"\033[0m")
    print("\033[32m/fun\033[0m")
    print("\033[32mgreet\033[0m\n")

    print("\033[1;33m+---------------------- FEATURES ----------------------------+\033[0m")
    print("\033[32m-> Variables are globally accessible\033[0m")
    print("\033[32m-> Supports loops and nested execution\033[0m")
    print("\033[32m-> Supports recursive functions\033[0m")
    print("\033[32m-> Simple and fast interpreter design\033[0m")
    print("\033[32m-> Direct system command execution\033[0m\n")

    print("\033[1;33m+---------------------- FUTURE ------------------------------+\033[0m")
    print("\033[32m-> Condition system (if/else)\033[0m")
    print("\033[32m-> Expression evaluation\033[0m")
    print("\033[32m-> File handling\033[0m")
    print("\033[32m-> Advanced scripting engine\033[0m\n")

    print("\033[1;33m+============================================================+\033[0m\n")

def terminal():
    print(
        "\033[1;33m+------------------------------------------------+\033[0m\n"
        "\033[1;33m|\033[0m \033[1;36mDeveloper :\033[0m \033[37mNiranjan Kumar K\033[0m                   \033[1;33m|\033[0m\n"
        "\033[1;33m+------------------------------------------------+\033[0m\n"
        "\033[1;33m|\033[0m \033[1;36mEmail     :\033[0m \033[37mhackerenvironment1514@gmail.com\033[0m    \033[1;33m|\033[0m\n"
        "\033[1;33m+------------------------------------------------+\033[0m\n"
        "\033[1;33m|\033[0m \033[1;36mEngine    :\033[0m \033[35mNone\033[0m                               \033[1;33m|\033[0m\n"
        "\033[1;33m+------------------------------------------------+\033[0m\n"
        "\033[1;33m|\033[0m \033[1;36mNote      :\033[0m \033[32msystem commands allowed with ...\033[0m   \033[1;33m|\033[0m\n"
        "\033[1;33m+------------------------------------------------+\033[0m\n\n"
        "\033[1;34mEnjoy Learning and Practicing!\033[0m\n\n"
        "\033[1;31mExit using:\033[0m \033[37m_exit\033[0m\n"
    )
    prompt = "\033[33m::\033[32mk\033m\033[33m::\033[32m$\033[35m "
    try:
        while True:
            code = input(prompt).strip()
            if not code:
                continue
            if code == "_exit":
                break
            if code == "--help":
                help()
                continue
            eval_code(code.split(" "))
    except KeyboardInterrupt:
        print("\n\033[31mKeyboard Interrupt Detected, exiting...\033[0m")
    except Exception as e:
        print(f"\033[31mError in terminal: {e}\033[0m")
    print(
        "\n\033[1;32mSuccessfully Exited from K terminal ....     !\033[0m\n\n"
        "\033[1;36mNiranjan Special Thanked, for using Terminal !\033[0m\n"
    )
