import json
from datetime import date

PRODUCTTEMPLATENAME = "products_template.json"

OPTIONS = {1: "New Data", 2: "Show Next Month EMI Total"}


def create_file_name(username, file_name="_products.json"):
    return username + file_name


def user_input(in_prompt):
    return input(in_prompt)


def console_output(out_prompt):
    return print(out_prompt)


def write_json(data_dict, file_name):
    with open(file_name, 'w') as fn:
        json.dump(data_dict, fn)
        return True
    return False


def read_json(file_name=PRODUCTTEMPLATENAME):
    with open(file_name) as fn:
        return json.load(fn)
    return False


def menu():
    console_output("Enter new product data : Press 1")
    console_output("Next month EMIs Total : Press 2")
    console_output("Exit : Press Any Other Key")
    return user_input("Press a key : ")


def get_prod_details(pd):

    if pd:

        for k, v in pd.items():

            if isinstance(v, dict):
                pd[k] = get_prod_details(v)

            else:
                pd[k] = user_input("Enter a value for {}".format(k))

        return pd

    return False


def order(choice):

    if choice == 1:

        prod_details = read_json()
        prod_details['edited_on'] = date.isoformat(date.today())

        print(prod_details['products'])

        prod_details['products'] = get_prod_details(prod_details['products'])

        print(prod_details['products'])

        return True

    if choice == 2:
        return True
    return False


def main(OPTIONS):
    choice = menu()
    if choice.isnumeric():
        choice = int(choice)
        order(choice)
    else:
        return True


if __name__ == "__main__":
    print(main())
