# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!
portfolio = {
    "AAPL" : {
        "quantity" : 10,
        "strike" : 154.12
    },
    "GOOG" : {
        "quantity" : 2,
        "strike" : 812.56
    },
    "TSLA" : {
        "quantity" : 12,
        "strike" : 342.12        
    },
    "FB" : {
        "quantity" : 18,
        "strike" : 209.0
    }
}

market = {
    "AAPL" : 198.84,
    "GOOG" : 1217.93,
    "TSLA" : 267.66,
    "FB" : 179.06
}

#CRUD on dictionary
# READ
# whats the quantity of apple? keys have to be unique
# print(portfolio["AAPL"]["quantity"])
# CREATE / UPDATE
# portfolio["AFK"] = 1010
# DELETE
# del(portfolio["AFK"])

def pnl(pfl, mkt):
    result = []
    for name, price in mkt.items():
        result.append(pfl[name]["quantity"] * (price - pfl[name]["strike"]))
    product = round(sum(float(n) for n in result), 2)
    return product
print(pnl(portfolio, market))