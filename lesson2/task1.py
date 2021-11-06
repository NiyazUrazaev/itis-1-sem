import argparse


def get_mult_table(n):
    result_array = []
    for i in range(1, n + 1):
        array = []
        for j in range(1, n + 1):
            array.append(i * j)
        result_array.append(array)

    return result_array


def print_table(table):
    for i in range(len(table)):
        for j in range(len(table)):
            print(table[i][j], end='\t')
        print()


if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description='My first arg parser'
    )
    parser.add_argument(
        '--n',
        dest='n',
        type=int,
        help='Значение, до которой строится таблица умножения',
    )

    args = parser.parse_args()

    table = get_mult_table(args.n)

    print_table(table)