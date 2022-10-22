from typing import Dict, Literal, NamedTuple
import requests
import json

_currency_code = Literal['USD', 'UAH', 'EUR', 'BTC', 'RUR']
_exchange = Dict[str, Dict[str, str]]

_is_cash_rate: bool = True
_cash_exchange: _exchange
_noncash_exchange: _exchange

def __init__() -> None:
    data = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    server_response = json.loads(data.text)
    _cash_exchange = { exchange['ccy']: exchange for exchange in server_response }
    print(_cash_exchange)
    data = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    server_response = json.loads(data.text)
    _noncash_exchange = { exchange['ccy']: exchange for exchange in server_response }
    print(_noncash_exchange)

def set_cash_rate(cash: bool) -> None:
    _is_cash_rate = cash

def buy(what: _currency_code, for_what: _currency_code, you_pay: float) -> float:
    if (what == for_what):
        print('Currencies must be different!')
        return 0

    if (what == 'USD'):
        pass
    return 0

__init__()
