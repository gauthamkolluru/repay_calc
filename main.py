import json
from datetime import date, datetime, timedelta

# PRODUCTTEMPLATENAME = "products_template.json"

INSTRUCTIONS = {
    "Date format": "yyyy-mm-dd EX 2020-12-31 for 31st December 2020"
}

OPTIONS = {
    1: "New Data",
    2: "Show Next Month EMI Total",
    "Any Key": "Exit"
}

PURCHASE_DETAILS = {
    "item": [
        'name',
        'bought from',
        'bought on',
        'bought using',
        'price',
    ],
    "repayment": [
        "start date",
        "tenure"
    ]
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


def read_json(file_name):
    with open(file_name) as fn:
        return json.load(fn)
    return False


def grd(pd):
    """
    GRD : Get Repayment Details
    """

    for purchase in PURCHASE_DETAILS:
        for item in PURCHASE_DETAILS[purchase]:
            item_detail = input("{} {} : ".format(
                'Product' if purchase.lower() == 'item' else 'Repayment', item))
            pd.update({item: item_detail})
    return pd


def get_end_date(pd):
    start_date = datetime.strptime(pd['start date'], "%Y-%m-%d")
    no_of_days = int(pd['tenure']) * 30
    end_date = start_date + timedelta(days=no_of_days)
    end_date = datetime.strptime(
        "{}-{}-{}".format(end_date.year, end_date.month, start_date.day), "%Y-%m-%d").date().isoformat()
    pd.update({'end date': end_date})
    return pd


def order(choice):
    if choice == 1:
        pd = dict()
        pd = grd(pd)
        pd = get_end_date(pd)
        print(pd)
        return True
    if choice == 2:
        return True
    return False


def menu():

    for option in OPTIONS:
        print("Press {} for {}".format(option, OPTIONS[option]))

    for instruction in INSTRUCTIONS:
        print(instruction + " " + INSTRUCTIONS[instruction])

    return user_input("Press a key : ")


def main():
    choice = menu()
    if choice.isnumeric():
        choice = int(choice)
        order(choice)
    else:
        return True


if __name__ == "__main__":
    print(main())
