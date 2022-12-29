import requests

response = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
if response.status_code == 200:
    content = response.json()
    eur = content[0]
    usd = content[1]
    buy_eur = round(float(eur['buy']), 2)
    sale_eur = round(float(eur['sale']), 2)
    buy_usd = round(float(usd['buy']), 2)
    sale_usd = round(float(usd['sale']), 2)
