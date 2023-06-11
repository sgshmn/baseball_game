from random import randint
# from main import al


def make_q():

    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    q = ''
    for i in range(4):
        temp = randint(0, 9 - i)
        q += digit[temp]
        digit.remove(digit[temp])
    return q
