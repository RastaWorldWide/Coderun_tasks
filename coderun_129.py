import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())

    dictionary = {}
    tree_dictionary = {}

    for i in range(n - 1):
        children = input().split()
        dictionary[children[0]] = children[1]

    s_dictionary = set(dictionary)
    first_parent = None
    for i, values in dictionary.items():
        if values not in s_dictionary:
            first_parent = values
            tree_dictionary[first_parent] = 0

    # parent = None
    # for i in s_dictionary:
    #     parent = i
    #     for j in dictionary:
    #         if



    for i in s_dictionary:
        print(i, )
    print(s_dictionary, tree_dictionary)




if __name__ == '__main__':
    main()
