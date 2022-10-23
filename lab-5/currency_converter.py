""" ## Simple currency converter
       This module uses PrivatBank API to get exchange rates.
       There are a few methods for transactions with cash (..._cash methods) and without (..._noncash methods).
       Bank sells USD, EUR, BTC (cash) and USD, EUR, RUR, BTC (noncash). Clients buy them with UAH or USD.
       Bank buys from clients USD, EUR, BTC (cash) and USD, EUR, RUR, BTC (noncash). Clients receives UAH or USD.
"""

from typing import Dict, Literal, Union
import requests

# Type aliases
_cash_ccy = Literal['USD', 'EUR', 'BTC']
_noncash_ccy = Literal['USD', 'EUR', 'RUR', 'BTC']
_cash_base_ccy = Literal['UAH', 'USD']
_exchange = Dict[str, Dict[str, str]]

# Dictionary that holds a cash exchange
_cash_exchange: _exchange
# Dictionary that holds a cashless exchange
_noncash_exchange: _exchange

def __init__() -> None:
    """This hidden function runs when the module is importing.
        It sends two "GET" requests and receives cash and noncash exchange rates in JSON format.
    """
    # Get cash exchange rate
    server_response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5').json()

    global _cash_exchange
    _cash_exchange = { exchange['ccy']: exchange for exchange in server_response }
    
    # Get cashless exchange rate
    server_response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11').json()
    
    global _noncash_exchange
    _noncash_exchange = { exchange['ccy']: exchange for exchange in server_response }
    

def __buy__(what_exactly: Union[_cash_ccy, _noncash_ccy], payment: float, pay_in: _cash_base_ccy, exchange: _exchange) -> float:
    """This hidden function contains the main logic of currency "buying".
        It's was written to reduce code duplication. Any direct call will cause an undefined behavior.
    """
    # Exact currency case
    if (what_exactly == pay_in):
        return 0
    
    # Case when 'base_ccy' field of 'what_exactly' currency is not the same as 'pay_in'
    if exchange[what_exactly]['base_ccy'] != pay_in:
        # Check if pay_in currency is in our dictionary
        if exchange.get(pay_in, 0) != 0:
            intermediate_buy = float(exchange[pay_in]['buy']) * payment
            return intermediate_buy / float(exchange[what_exactly]['sale'])
        else:
            intermediate_exchange = exchange[exchange[what_exactly]['base_ccy']]
            intermediate_buy = payment / float(intermediate_exchange['sale'])
            return intermediate_buy / float(exchange[what_exactly]['sale'])
    else:
        return payment / float(exchange[what_exactly]['sale'])

def buy_cash(what_exactly: _cash_ccy, payment: float, pay_in: _cash_base_ccy) -> float:
    """This function allows you to "buy" currency (cash).
        
        Args:
            what_exactly (Literal['USD', 'EUR', 'BTC']): the currency that you want to buy
            payment (float): amount of money that you have
            pay_in (Literal['UAH', 'USD']): the currency of your money

        Returns:
            float: result of the exchange operation in "what_exactly" currency.
    """
    global _cash_exchange
    return __buy__(what_exactly, payment, pay_in, _cash_exchange)

def buy_noncash(what_exactly: _noncash_ccy, payment: float, pay_in: _cash_base_ccy) -> float:
    """This function allows you to "buy" currency (noncash).
        
        Args:
            what_exactly (Literal['USD', 'EUR', 'RUR', 'BTC']): the currency that you want to buy
            payment (float): amount of money that you have
            pay_in (Literal['UAH', 'USD']): the currency of your money

        Returns:
            float: result of the exchange operation in "what_exactly" currency.
    """
    global _noncash_exchange
    return __buy__(what_exactly, payment, pay_in, _noncash_exchange)

def __sale__(payment: float, pay_in: Union[_cash_ccy, _noncash_ccy], sum_get_in: _cash_base_ccy, exchange: _exchange) -> float:
    """This hidden function contains the main logic of currency "selling".
        It's was written to reduce code duplication. Any direct call will cause an undefined behavior.
    """
    # Exact currency case
    if (pay_in == sum_get_in):
        return 0
    
    # Case when 'base_ccy' field of 'pay_in' currency is not the same as 'sum_get_in'
    if exchange[pay_in]['base_ccy'] != sum_get_in:
        # Check if sum_get_in currency is in our dictionary
        if exchange.get(sum_get_in, 0) != 0:
            intermediate_buy = float(exchange[pay_in]['buy']) * payment
            return intermediate_buy / float(exchange[sum_get_in]['sale'])
        else:
            intermediate_buy = float(exchange[pay_in]['buy']) * payment
            return intermediate_buy * float(exchange[sum_get_in]['sale'])
    else:
        return payment * float(exchange[pay_in]['buy'])

def sale_cash(payment: float, pay_in: _cash_ccy, sum_get_in: _cash_base_ccy) -> float:
    """This function allows you to "sell" currency (cash).
        
        Args:
            payment (float): amount of money that you have
            pay_in (Literal['USD', 'EUR', 'BTC']): the currency of your money
            sum_get_in (Literal['UAH', 'USD']): the received currency

        Returns:
            float: result of the exchange operation in "sum_get_in" currency.
    """
    global _cash_exchange
    return __sale__(payment, pay_in, sum_get_in, _cash_exchange)

def sale_noncash(payment: float, pay_in: _cash_ccy, sum_get_in: _cash_base_ccy) -> float:
    """This function allows you to "sell" currency (noncash).
        
        Args:
            payment (float): amount of money that you have
            pay_in (Literal['USD', 'EUR', 'BTC']): the currency of your money
            sum_get_in (Literal['UAH', 'USD']): the received currency

        Returns:
            float: result of the exchange operation in "sum_get_in" currency.
    """
    global _noncash_exchange
    return __sale__(payment, pay_in, sum_get_in, _noncash_exchange)

__init__()
