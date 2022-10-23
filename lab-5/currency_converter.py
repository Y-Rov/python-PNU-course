from decimal import Decimal, getcontext
from typing import Dict, Literal
import requests
import json

_currency_code = Literal['USD', 'UAH', 'EUR', 'BTC', 'RUR']

_cash_ccy = Literal['USD', 'EUR', 'BTC']
_cash_base_ccy = Literal['UAH', 'USD']

_noncash_ccy = Literal['USD', 'EUR', 'RUR', 'BTC']
_exchange = Dict[str, Dict[str, str]]

_cash_exchange: _exchange
_noncash_exchange: _exchange

def __init__() -> None:
    data = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    server_response = json.loads(data.text)
    global _cash_exchange
    _cash_exchange = { exchange['ccy']: exchange for exchange in server_response }
    print(_cash_exchange)
    data = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    server_response = json.loads(data.text)
    global _noncash_exchange
    _noncash_exchange = { exchange['ccy']: exchange for exchange in server_response }
    print(_noncash_exchange)
    getcontext().prec = 2

def buy(what: _cash_ccy, for_what: _cash_base_ccy, client_pays: float) -> Decimal:
    if (what == for_what):
        return Decimal()

    global _cash_exchange
    if (_cash_exchange[what]['base_ccy'] != for_what):
        pass
    else:
        return Decimal(Decimal(client_pays) / Decimal(_cash_exchange[what]['sale'])) 
    
    return Decimal()

__init__()
