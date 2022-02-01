# Calculating with Dictionaries
# 1.8.1
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 1.8.2

min_price = min(zip(prices.values(), prices.keys()))

max_price = max(zip(prices.values(), prices.keys()))

prices_sorted = sorted(zip(prices.values(), prices.keys()))

# This code has error
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
prices(max(prices_and_names)) #ValueError

# Discussion
min(prices)
max(prices)

# --
min(prices.values())
max(prices.values())

# --
min(prices, key=lambda k: prices[k])
max(prices, key=lambda k: prices[k])

min_value = prices[min(prices, key=lambda k: prices[k])]

# --
prices = {'AAA' : 45.23, 'ZZZ' : 45.23}
min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))