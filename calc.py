def get_monthly_emi(principle, roi, tenure):
    total_interest = get_total_interest(principle, roi, tenure)
    return round((int(principle) + int(total_interest))/int(tenure))


def get_total_interest(principle, roi, tenure):
    return ((int(principle)*(int(roi)/100))/12)*int(tenure)


def is_active(given_date):
    return (read_date_from_string(given_date) - date.today()).days > 0
