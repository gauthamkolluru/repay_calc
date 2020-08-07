from datetime import date, datetime, timedelta


def get_days_from_months(months):
    return int(months) * 30


def read_date_from_string(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()


def get_date_in_string(given_date=datetime.now()):
    return given_date.date().isoformat()


def get_end_date(start_date, tenure):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    differenced_date = start_date + \
        timedelta(days=get_days_from_months(tenure))
    return get_date_in_string(differenced_date)[:-2] + get_date_in_string(start_date)[-2:]
