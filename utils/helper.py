from datetime import date, datetime


def date_for_str(date_time):
    return date_time.strftime('%m/%d/%Y')

def str_for_date(date_time):
    return datetime.strptime(date_time, '%m/%d/%Y')

def format_float_for_real_currency(valor):
    return f'R$ {valor:,.2f}'

