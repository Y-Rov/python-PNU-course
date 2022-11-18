import currency_converter as curr

print(curr.__doc__)
first = curr.buy_cash('USD', 50, 'UAH')
second = curr.buy_cash('EUR', 50, 'USD')
third = curr.buy_cash('BTC', 500000, 'UAH')
fourth = curr.buy_noncash('USD', 50, 'UAH')

fifth = curr.sale_cash(50, 'USD', 'UAH')
