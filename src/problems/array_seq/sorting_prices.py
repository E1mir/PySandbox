"""
Problem

Create a function that takes in a list of unsorted prices (integers)
and a maximum possible price value, and return a sorted list of prices

Requirements
Your function should be able to perform this in less than O(nlogn) time.
"""


def solution(unsorted_prices, max_price):
    prices_to_counts = [0] * (max_price + 1)

    for price in unsorted_prices:
        prices_to_counts[price] += 1

    sorted_prices = []

    for price, count in enumerate(prices_to_counts):
        for time in range(count):
            sorted_prices.append(price)

    return sorted_prices


if __name__ == '__main__':
    a = solution([4, 6, 2, 7, 3, 8, 9], 9)
    print(a)
