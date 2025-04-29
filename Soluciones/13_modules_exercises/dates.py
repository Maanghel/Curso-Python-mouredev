from datetime import datetime

def current_date():
    return datetime.now().strftime("%d-%m-%Y")

def date_difference(date1, date2):
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")
    return abs((d1 - d2).days)