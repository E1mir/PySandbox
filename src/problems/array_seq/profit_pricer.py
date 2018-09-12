"""
Problem

You've been given a list of historical stock prices for a single day for Amazon stock.
The index of the list represents the timestamp, so the element at index of 0 is the initial price of the stock,
the element at index 1 is the next recorded price of the stock for that day, etc.
Your task is to write a function that will return the maximum profit possible from the purchase
and sale of a single share of Amazon stock on that day.

For example, if you were given the list of stock prices:

prices = [12,11,15,3,10]

Then your function would return the maximum possible profit, which would be 7 (buying at 3 and selling at 10).

"""


def profit_checker(stock_prices):
    min_stock_price = stock_prices[0]
    max_profit = 0

    for price in stock_prices:
        min_stock_price = min(min_stock_price, price)

        comparison_profit = price - min_stock_price

        max_profit = max(max_profit, comparison_profit)

    return max_profit


def profit_checker2(stock_prices):
    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices!')

    min_stock_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for price in stock_prices[1:]:
        comparison_profit = price - min_stock_price

        max_profit = max(max_profit, comparison_profit)
        min_stock_price = min(min_stock_price, price)

    return max_profit


if __name__ == '__main__':
    stock = [10, 2, 12]
    p = profit_checker(stock)
    print(p)
    p = profit_checker2(stock)
    print(p)
