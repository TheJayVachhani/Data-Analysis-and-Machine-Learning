# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]
fbs = portfolio[3][0]

market = [ 198.84, 1217.93, 267.66, 179.06 ]
# pnl function designed to take portfolio and market
# where they are the same length and return overall performance
def pnl(pfl, mkt):
    result = []
    for n, value in enumerate(mkt):
        result.append(pfl[n][0] * (value - pfl[n][1]))
    product = round(sum(float(n) for n in result), 2)
    return product
print (pnl(portfolio, market))