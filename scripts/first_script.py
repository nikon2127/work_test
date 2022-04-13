import cowsay


def greet(two):
    print(f"Hello, {two}")


def greet_ret(two):
    return f'Hello, {two}'


def main():
    greet('Bob')
    greet('ann')
    print(greet_ret('Nik'))


if __name__ == '__main__':
    main()
    cowsay.tux('Hello, Nikon')
