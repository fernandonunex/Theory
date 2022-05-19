from random import choice


if __name__ == '__main__':

    signs = ['1', '2', '3', '4', '5', '6',
             '7', '8', '9', '0', 'a', 'b', 'c', 'd']
    my_ticket = 'ab4580'
    big_price = ''
    secuence = 6
    n = 0

    while(True):
        big_price = ''
        for x in range(0, secuence):
            big_price += choice(signs)

        if my_ticket == big_price:
            break
        else:
            n += 1
            continue

    print(f'To win the lottery took: {n} times')

    # print('The price is for anyone that the ticket matches with: ')
    # print({big_price})
