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
        "tenure",
        "roi"
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


def gpd():
    """
    GPD : Get Purchase Details
    """
    pd = dict()
    for purchase in PURCHASE_DETAILS:
        for item in PURCHASE_DETAILS[purchase]:
            item_detail = input("{} {} : ".format(
                'Product' if purchase.lower() == 'item' else 'Repayment', item))
            pd.update({item: item_detail})

    pd.update({'end date': get_end_date(
        pd['start date'], pd['tenure'])})

    pd.update({'emi': get_monthly_emi(pd['price'], pd['roi'], pd['tenure'])})

    pd.update({'active': is_active(pd['end date'])})

    print(pd)

    return pd


def is_active(given_date):
    return (read_date_from_string(given_date) - date.today()).days > 0


def get_monthly_emi(principle, roi, tenure):
    total_interest = get_total_interest(principle, roi, tenure)
    return round((int(principle) + int(total_interest))/int(tenure))


def get_days_from_months(months):
    return int(months) * 30


def read_date_from_string(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()


def get_date_in_string(given_date):
    return given_date.date().isoformat()


def get_end_date(start_date, tenure):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    differenced_date = start_date + \
        timedelta(days=get_days_from_months(tenure))
    return get_date_in_string(differenced_date)[:-2] + get_date_in_string(start_date)[-2:]


def get_total_interest(principle, roi, tenure):
    return ((int(principle)*(int(roi)/100))/12)*int(tenure)


def order(choice):
    if choice == 1:
        pd = gpd()
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
