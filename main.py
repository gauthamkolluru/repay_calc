import data_handler

def user_file_name(username, file_name="_products.json"):
    return username + file_name


def update_json_dict(existing_data, new_prod_data, edited_date=""):
    if existing_data:
        if edited_date:
            existing_data[JSON_DICT_KEYS[0]] = edited_date
        if new_prod_data:
            existing_data[JSON_DICT_KEYS[1]].append(new_prod_data)
        return existing_data
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


def get_total_interest(principle, roi, tenure):
    return ((int(principle)*(int(roi)/100))/12)*int(tenure)


def order(choice):
    if choice == 1:
        fd = read_json(user_file_name(input("Enter Username : ")))
        fd = fd if fd else STORE_DICT
        fd['edited on'] = get_date_in_string()
        fd['products'].append(gpd())
        write_json(fd, user_file_name(input("Enter Username : ")))
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
