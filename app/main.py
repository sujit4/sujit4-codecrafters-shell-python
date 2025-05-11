import sys
import shlex

def cmd_exit(args):
    if not args:
        exit_code = 0
    elif len(args) == 1 and args[0] == "0":
        exit_code = int(args[0])
    else:
        print(f"exit {' '.join(args)}: command not found")
        return
    sys.exit(exit_code)

def cmd_echo(args):
    print(" ".join(args))

def cmd_type(args):
    if not args:
        print("No arguments given!")
    elif len(args) == 1:
        if args[0] in COMMANDS:
            print(f"{args[0]} is a shell builtin")
        else:
            print(f"{args[0]}: not found")
    else:
        print("Too many arguments!!")

# command registry
COMMANDS = {
    "exit": cmd_exit,
    "echo": cmd_echo,
    "type": cmd_type
}

def main():
    while True:
        try:
            sys.stdout.write("$ ")
            sys.stdout.flush()

            user_input = input()
            if not user_input.strip():
                continue
            
            # split input into an array of words
            input_array = shlex.split(user_input)
            cmd = input_array[0]
            args = input_array[1:]

            # lookup command in the command registry
            if cmd in COMMANDS:
                COMMANDS[cmd](args)
            else:
                print(f"{user_input}: command not found")
    
        except EOFError:
            print("Exiting shell...")
            break

        except KeyboardInterrupt:
            print("\n^C")
            continue


if __name__ == "__main__":
    main()
