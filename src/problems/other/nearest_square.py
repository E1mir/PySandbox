def solution(num):
    if num < 0:
        raise ValueError

    if num == 1:
        return 1

    k = None

    for k in range(num // 2 + 1):
        if k ** 2 == num:
            return k
        elif k ** 2 > num:
            return k - 1

    return k


def best_solution(num):
    if num < 0:
        raise ValueError
    if num == 1:
        return 1

    low = 0
    high = num // 2 + 1

    while low + 1 < high:
        mid = low + (high - low) // 2

        square = mid ** 2

        if square == num:
            return mid
        elif square < num:
            low = mid
        else:
            high = mid

    return low


if __name__ == '__main__':
    a = solution(99898)
    print(a)
    a = best_solution(19)
    print(a)