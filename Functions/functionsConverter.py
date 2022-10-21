

import requests


def priceRequest(coin):

    url = (f'https://api.yadio.io/exrates/{coin}')
    response = requests.get(url)
    values = response.json()
    price = values["BTC"]
    return f"el precio de bitcoin es:\n{price} {coin}"

def fiatToSats( coin, amount, prima):

    url = (f'https://api.yadio.io/convert/{amount}/{coin}/BTC')
    response = requests.get(url)
    Value = response.json()
    result = Value["result"]
    if prima.lstrip("-").isdigit():

        result = result * 100000000
        prima = result * (float(prima) / 100)
        result = result + prima
        return f" {result} sats = {amount} {coin}"
    else:
        result = result * 100000000
        return f" {result} sats = {amount} {coin}"


   
def satToFiat(sats, coin, prima):
    
    sats = int(sats) / 100000000
    url = (f'https://api.yadio.io/convert/{sats}/BTC/{coin}')
    response = requests.get(url)
    Value = response.json()
    result = Value["result"]
    satresult = sats *100000000
    if prima.lstrip("-").isdigit():
        prima = result * (float(prima) / 100)
        result = result + prima 
        return f"{satresult} = {result} {coin}"
    else:
        return f"{satresult} = {result} {coin}"

