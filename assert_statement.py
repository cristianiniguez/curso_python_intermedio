def divisors(num):
    assert num > 0, "Debes ingresar un número positivo"
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors


def run():
    try:
        num = input("Ingresa un número positivo: ")
        assert num.isnumeric(), "Debes ingresar un número"
        print(divisors(int(num)))
        print("Terminó mi programa")
    except AssertionError as ae:
        print(ae)


if __name__ == '__main__':
    run()
