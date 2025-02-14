from datetime import datetime

def format_date(date):
    date_obj = datetime.fromisoformat(date)
    formatted_date = date_obj.strftime('%d/%m/%Y')

    return formatted_date