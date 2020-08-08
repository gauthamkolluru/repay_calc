import utils.io_utils as iu

import data_handler


def order(choice):
    if choice == 1:
        return True
    if choice == 2:
        return True
    return False


def menu(opts):
    for opt in opts.items():
        iu.conout(opt)
    return iu.conin('choice')


def main():
    choice = menu(data_handler.default_data.OPTIONS)
    if choice.isnumeric():
        choice = int(choice)
        order(choice)
    else:
        return True


if __name__ == "__main__":
    print(main())
