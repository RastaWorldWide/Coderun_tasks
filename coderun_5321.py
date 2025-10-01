import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    result = 2**n -1

    print(result)


if __name__ == '__main__':
    main()
