def denominate(amount, coins):
    arr = [1] + [0] * amount

    for coin in coins:
        for i in range(coin, amount + 1):
            arr[i] += arr[i - coin]

    if amount == 0:
        return 0
    else:
        return arr[amount]


if __name__ == '__main__':
    a = denominate(100, [1, 5, 10, 20, 50, 100])
    print(a)
