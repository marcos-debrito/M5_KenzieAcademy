from utils import data_processing


def main():
    dict = {
        "name": "França",
        "titles": 1,
        "top_scorer": "Zidane",
        "fifa_code": "FRA",
        "first_cup": "2002-10-18",
    }
    data_processing(dict)


if __name__ == "__main__":
    main()
