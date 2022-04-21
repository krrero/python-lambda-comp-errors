from functools import reduce


def saludo(func):
    func()


def hola():
    print('Ola')


def adios():
    print('chao')
    

if __name__ == '__main__':
    saludo(hola)
    saludo(adios)

    my_list = [1,4,5,6,9,13,19,21]

    odd = list(filter(lambda x: x%2  != 0, my_list))

    print(odd)

    map_list = [1, 2, 3, 4, 5]

    squares = list(map(lambda x: x**2, map_list))

    print(squares)

    reduce_list = [2, 2, 2, 2, 2]

    sum = reduce(lambda a, b: a * b, reduce_list)

    print(sum)