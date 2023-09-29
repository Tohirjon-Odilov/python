from requests import get


class Currency:
    def __init__(self, json):
        self.title = json["title"]
        self.code = json["code"]
        self.cb_price = json["cb_price"]
        self.nbu_buy_price = json["nbu_buy_price"]
        self.nbu_cell_price = json["nbu_cell_price"]
        self.date = json["date"]


def getData():
    url = "https://nbu.uz/uz/exchange-rates/json/"
    response = get(url)
    print(response)
    usd_price = None
    currencies = []
    if response.status_code == 200:
        data = response.json()
        for i in data:
            currencies.append(Currency(i))

    return currencies