import argparse


def func(a, b):
    return a ** b


if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description='My first arg parser'
    )
    parser.add_argument(
        '--val1',
        dest='val1',
        type=int,
        help='First int value'
    )
    parser.add_argument(
        '--val2',
        dest='val2',
        type=int,
        help='Second int value'
    )
    parser.add_argument(
        '--val3',
        dest='val3',
        type=str,
        help='Third str value'
    )

    args = parser.parse_args()

    print(args.val3)

    result = func(args.val1, args.val2)

    print(result)