from datetime import datetime
import pytz

def format_date(date):
    date_obj = datetime.fromisoformat(date)
    formatted_date = date_obj.strftime('%d/%m/%Y')

    return formatted_date

def rashid():
    cities = [
        "Svargrond",
        "Liberty Bay",
        "Port Hope",
        "Ankrahmun",
        "Darashia",
        "Edron"
        "Carlin"
    ]

    datetime_obj = datetime.now(pytz.timezone('America/Metlakatla'))
    weekday = datetime_obj.weekday()
    city = cities[weekday]

    result = f"Today Rashid is located on {city}."
    return result