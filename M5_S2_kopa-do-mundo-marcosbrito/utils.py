from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError
from exceptions import ImpossibleTitlesError
from datetime import datetime


def data_processing(dictionary: dict):

    if dictionary["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    year = int(dictionary["first_cup"][:4])
    if year < 1930:
        raise InvalidYearCupError("there was no world cup this year")

    initial_year = 1930
    if year < initial_year or (year - initial_year) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    now = datetime.now()
    actual_year = now.year

    period = actual_year - year
    possible_title = period / 4

    if int(dictionary["titles"]) > possible_title:
        raise ImpossibleTitlesError(
            "impossible to have more titles than disputed cups"
        )
