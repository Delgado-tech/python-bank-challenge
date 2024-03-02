from datetime import datetime


def string_to_date(string: str):
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S")