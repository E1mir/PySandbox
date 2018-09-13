from random import randint


def dice_7():
    return randint(1, 7)


def dice_5():
    return randint(1, 5)


def convert_7_to_5():
    roll = 7
    while roll > 5:
        roll = dice_7()
        print("dice_7() produced a roll of", roll)
    print("Your final returned roll is below:")
    return roll


def convert_5_to_7():
    while True:
        roll_1 = dice_5()
        roll_2 = dice_5()

        num = ((roll_1 - 1) * 5) + roll_2

        if num > 21:
            continue

        return num % 7 + 1


if __name__ == '__main__':
    ans = convert_7_to_5()
    print(ans)
    ans = convert_5_to_7()
    print(ans)
