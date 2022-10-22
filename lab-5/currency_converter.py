from typing import Dict, Literal, NamedTuple
import requests
import json

class CashExchange(NamedTuple):
    usd: Dict[str, str]
    eur: Dict[str, str]
    btc: Dict[str, str]

class NonCashExchange(NamedTuple):
    usd: Dict[str, str]
    eur: Dict[str, str]
    rur: Dict[str, str]
    btc: Dict[str, str]

_is_cash_rate: bool = True
_currency_code = Literal['USD', 'UAH', 'EUR', 'BTC', 'RUR']
_cash_exchange: CashExchange
_noncash_exchange: NonCashExchange

def __init__() -> None:
    data = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    _cash_exchange = CashExchange(*json.loads(data.text))
    data = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')
    _noncash_exchange = NonCashExchange(*json.loads(data.text))

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
