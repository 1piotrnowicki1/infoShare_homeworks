from math import sqrt


def pitagoras_c():
    side_a = int(input('Input the length of side a: '))

    side_b = int(input('Input the length of side b: '))

    # try:
    #     int(side_a, side_b);
    #     # Variable a is int
    #     print('varibles int')
    # except ValueError:
    #     # Variable a is not an int
    #     print('is not int')

    side_c = sqrt(side_a * side_a + side_b * side_b)

    print(f'The length of side c is: {side_c}')
    print(side_c)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pitagoras_c()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
