class NotEnoughMoney(ValueError):
    pass


class NoCashInATM(ValueError):
    pass


class ATM(object):
    def __init__(self, balance=0, money=(1, 5, 10, 20, 50, 100)):
        self._money = tuple(sorted(money))
        self._balance = balance

    def withdraw(self, amount):

        if amount > self._balance:
            raise NotEnoughMoney

        withdrawing = {}
        need_to_give = amount

        if need_to_give in self._money:
            withdrawing[need_to_give] = 1
            return withdrawing

        for cash in self._money[::-1]:
            count = 0
            while need_to_give >= cash:
                count += 1
                withdrawing[cash] = count
                need_to_give -= cash
            if need_to_give < 0:
                raise NoCashInATM
        self._balance -= amount
        return withdrawing

    def balance(self):
        return self._balance

    def __repr__(self):
        return "ATM({self._balance}, {self._money})".format(self=self)

    def __str__(self):
        return "Your balance is: {self._balance}".format(self=self)


if __name__ == '__main__':
    bank = ATM(1500)
    print(bank)
    w = bank.withdraw(1232)
    print(w)
    print(bank)  # now balance is 268
    w = bank.withdraw(267)
    print(w)
    print(bank) # now balance is 1
