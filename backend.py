import requests
from bs4 import BeautifulSoup

currency_list = []


def get_current_rate(from_currency, to_currency):
    global currency_list
    url = f"https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount=1"
    # print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    currency_code_from = soup.find("div", id="fromInput").find("select", id="from")
    # print(currency_code_from)
    for curr in currency_code_from:
        if curr == "\n":
            pass
        else:
            currency_list.append(curr.get_text().strip())

    currency = soup.find("span", class_="ccOutputRslt")
    rate = float(currency.get_text().split(" ")[0])
    return rate


def get_currency(value_currency_from, value_currency_to, amount_entry, current_amount):
    from_curr = value_currency_from.get().split(" - ")[0]
    to_curr = value_currency_to.get().split(" - ")[0].strip()
    # print(from_curr, type(from_curr))
    # print(to_curr, type(to_curr))
    current_rate = float(get_current_rate(from_curr, to_curr))
    amount_to_convert = float(amount_entry.get())
    converted_amount = current_rate * amount_to_convert
    current_amount.config(text=round(converted_amount, 2))
