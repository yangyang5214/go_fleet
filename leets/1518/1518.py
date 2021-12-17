# -*- coding: UTF-8 -*-


def main(numBottles: int, numExchange: int):
    r = 0
    while numBottles >= numExchange:
        r = r + (numBottles - numBottles % numExchange)
        numBottles = numBottles // numExchange + numBottles % numExchange
    return r + numBottles


if __name__ == '__main__':
    print(main(2, 3))
