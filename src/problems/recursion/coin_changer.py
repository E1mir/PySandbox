"""
Problem Statement
Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.

For example:

If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

1+1+1+1+1+1+1+1+1+1
5 + 1+1+1+1+1
5+5
10

With 1 coin being the minimum amount.
"""


# worst solution
def rec_coin(target, coins):
    # default value set to target
    min_coins = target

    # base case
    if target in coins:
        return 1

    else:

        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target - i, coins)
            # reset minimum if new num_coins less than minimum coins
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


def rec_coin_dyn(target, coins, cache):
    min_coins = target

    # base case
    if target in coins:
        cache[target] = 1
        return 1

    # return a known result if it in cache
    elif cache[target] > 0:
        return cache[target]
    else:
        # for every coin value i <= target
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin_dyn(target - i, coins, cache)

            if num_coins < min_coins:
                min_coins = num_coins

                # reset cache result
                cache[target] = min_coins

    return min_coins


# Solution from Wikipedia
def _get_change_making_matrix(set_of_coins, r):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(r + 1):
        m[0][i] = i
    return m


def change_making(coins, n):
    """This function assumes that all coins are available infinitely.
    n is the number to obtain with the fewest coins.
    coins is a list or tuple with the available denominations."""
    matrix = _get_change_making_matrix(coins, n)
    for c in range(1, len(coins) + 1):
        for r in range(1, n + 1):
            # Just use the coin coins[c - 1].
            if coins[c - 1] == r:
                matrix[c][r] = 1

            # coins[c - 1] cannot be included.
            # Use the previous solution for making r,
            # excluding coins[c - 1].
            elif coins[c - 1] > r:
                matrix[c][r] = matrix[c - 1][r]
            # coins[c - 1] can be used.
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coins[c - 1]).
            # 2. Using the previous solution for making r - coins[c - 1] (without
            #      using coins[c - 1]) plus this 1 extra coin.
            else:
                matrix[c][r] = min(matrix[c - 1][r], 1 + matrix[c][r - coins[c - 1]])
    return matrix[-1][-1]


if __name__ == '__main__':
    print(rec_coin(15, [1, 5, 10]))
    # print(rec_coin(63, [1, 5, 10, 25])) takes a lot of time
    target_amount = 754
    coins_list = [1, 5, 10, 25]
    cache_storage = [0] * (target_amount + 1)
    print(rec_coin_dyn(target_amount, coins=coins_list, cache=cache_storage))
