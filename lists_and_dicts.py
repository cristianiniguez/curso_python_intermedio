def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"first_name": "Cristian", "last_name": "Iñiguez"}

    super_list = [
        {"first_name": "Cristian", "last_name": "Iñiguez"},
        {"first_name": "Mary", "last_name": "Saucedo"},
        {"first_name": "Dario", "last_name": "Rojas"},
        {"first_name": "Felix", "last_name": "Gonzales"},
        {"first_name": "Javier", "last_name": "Tapia"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
        # natural_nums - [1, 2, 3, 4, 5]
        # integer_nums - [-2, -1, 0, 1, 2]
        # floating_nums - [1.1, 4.5, 6.43]

    for item in super_list:
        print(item)
        # {'first_name': 'Cristian', 'last_name': 'Iñiguez'}
        # {'first_name': 'Mary', 'last_name': 'Saucedo'}
        # {'first_name': 'Dario', 'last_name': 'Rojas'}
        # {'first_name': 'Felix', 'last_name': 'Gonzales'}
        # {'first_name': 'Javier', 'last_name': 'Tapia'}


if __name__ == '__main__':
    run()
