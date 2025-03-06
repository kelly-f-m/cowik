from datetime import datetime
import pytz


def rashid_location() -> str:
    """
    Retorna a cidade que o Rashid se encontra.

    :return: Uma string com o local que o Rashid se encontra.
    """
    cities = [
        "Svargrond",
        "Liberty Bay",
        "Port Hope",
        "Ankrahmun",
        "Darashia",
        "Edron",
        "Carlin",
    ]

    datetime_obj = datetime.now(pytz.timezone("America/Metlakatla"))
    weekday = datetime_obj.weekday()

    city = cities[weekday]

    result = f"Today Rashid is located on {city}."
    return result
