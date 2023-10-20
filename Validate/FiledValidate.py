import re
from datetime import datetime


def is_empty(variable):
    if variable is None:
        return True
    if isinstance(variable, str) and not variable:
        return True
    return False


def is_numeric(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False


def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_time(time_string):
    try:
        datetime.strptime(time_string, "%H:%M:%S")
        return True
    except ValueError:
        return False
