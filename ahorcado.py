from random import choice
from os import system as os_system
from platform import system as p_system
from sys import exit


def clear_console():
    if p_system() == 'Windows':
        os_system('cls')
    else:
        os_system('clear')


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def get_random_word():
    words = []
    try:
        with open('./files/data.txt', 'r', encoding='utf-8') as f:
            for word in f:
                words.append(word)
        word = choice(words)
        chars = [char.upper() for char in word if char != '\n']
        return normalize(''.join(chars))
    except FileNotFoundError:
        print('El archivo files/data.txt no se encuentra')
        exit()


def get_display_word(word, choices):
    chars = [char if char in choices else '_' for char in word]
    return ' '.join(chars)


def word_discovered(word, choices):
    word_discovered = True
    for char in word:
        if not char in choices:
            word_discovered = False
            break
    return word_discovered


def print_status(word, choices, opportunities):
    clear_console()
    print('----------')
    print('¡AHORCADO!')
    print('----------')
    print('')

    print(get_display_word(word, choices))
    print('')

    if len(choices) > 0:
        print('Letras ya escogidas', choices)
        print('')

    print(f'Tienes {opportunities} intento(s)')
    print('')


def print_win(word):
    clear_console()
    print('¡Felicidades, Ganaste! 🎉🎉🎉🎉🎉')
    print('La palabra era', word)


def print_lose(word):
    clear_console()
    print('Lo siento, perdiste 💀')
    print('La palabra era', word)


def run():
    word = get_random_word()
    opportunities = 5
    choices = []
    full_choice = False

    while opportunities > 0 and not word_discovered(word, choices) and not full_choice:
        print_status(word, choices, opportunities)
        letter = False
        while not letter:
            l = input('👨🏻 Adivina una letra [A-Z] o la palabra completa: ').upper()
            if len(l) > 1:
                full_choice = l
                break
            if l.isalpha() and len(l) == 1:
                if l in choices:
                    print('Ya escogiste esta letra')
                else:
                    letter = l
            else:
                print('Solo sirven letras de la A a la Z')
        if full_choice:
            break
        choices.append(letter)
        if not letter in word:
            opportunities -= 1

    if (full_choice and word == full_choice) or word_discovered(word, choices):
        print_win(word)
        return

    print_lose(word)


if __name__ == '__main__':
    run()
