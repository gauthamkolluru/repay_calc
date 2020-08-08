

def conout(*args):
    if args:
        for arg in args:
            print("{} : {}".format(arg[0], arg[1]))
        return True
    return False


def conin(arg):
    return input("Enter a {}".format(arg)) if arg else False
