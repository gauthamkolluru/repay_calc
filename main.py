import json
from datetime import date, datetime

PRODUCTTEMPLATENAME = "products_template.json"

OPTIONS = {
    1: "New Data",
    2: "Show Next Month EMI Total",
    "Any Key": "Exit"
}

PURCHASE_DETAILS = {
    "ITEM_DETAILS": {
        'name': "",
        'bought from': "",
        'bought on': "",
        'bought using': "",
        'price': "",
    },
    "REPAYMENT_DETAILS": {
        "start date": "",
        "tenure": "",
        "end date": "",
        "emi": ""
    }

}


def user_file_name(username, file_name="_products.json"):
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


def menu(options=OPTIONS):

    for option in options:
        print("Press {} for {}".format(option, options[option]))

    return user_input("Press a key : ")


# def gpd():
#     """
#     GPD : Get Product Details
#     """
#     return {i: input("Product {} : ".format(i)) for i in ITEM_DETAILS}


def grd():
    """
    GRD : Get Repayment Details 
    """
    return {i: {j: input("{} {} : ".format('Product' if i.lower() == 'item_details' else 'Repayment', j)) for j in PURCHASE_DETAILS[i]} for i in PURCHASE_DETAILS}


def order(choice):
    if choice == 1:
        pd = grd()
        print(pd)
        return True
    if choice == 2:
        return True
    return False


def main():
    choice = menu()
    if choice.isnumeric():
        choice = int(choice)
        order(choice)
    else:
        return True


if __name__ == "__main__":
    print(main())
