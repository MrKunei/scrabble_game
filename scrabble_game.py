import random

dict_alfa = {"а": 8, "б": 2, "в": 4, "г": 2, "д": 4, "е": 8, "ё": 1, "ж": 1,
             "з": 2, "и": 5, "й": 1, "к": 4, "л": 4, "м": 3, "н": 5, "о": 10,
             "п": 4, "р": 5, "с": 5, "т": 5, "у": 4, "ф": 1, "х": 1, "ц": 1,
             "ч": 1, "ш": 1, "щ": 1, "ъ": 1, "ы": 2, "ь": 2, "э": 1, "ю": 1,
             "я": 2}


def create_list_letters():
    string_letters = ""
    for letter, quantity in dict_alfa.items():
        letters = letter * quantity
        string_letters += letters
    list_letters = list(string_letters)
    return list_letters


def create_lists_user(list_letters, index):
    list_user = random.sample(list_letters, index)
    for letter in list_user:
        list_letters.remove(letter)
    return list_user


def check_word_in_list(word, list_user):
    counter = 0
    letters_word = list(word)
    for letter in letters_word:
        if letter in list_user:
            counter +=1
    if counter == len(letters_word):
        return True
    else:
        return False


def check_word_in_file(word):
    with open("russian_word.txt", encoding="utf-8") as file:
        if word in file.read():
            return True
        else:
            return False


def update_lists(list_letters, list_user, word):
    for letter in list(word):
        list_user.remove(letter)
    add_letter = create_lists_user(list_letters, len(word)+1)
    list_user += add_letter
    add_letter_str = ", ".join( add_letter)
    print(f"Добавляю следующие буквы: {add_letter_str}")


def check_points(word):
    points_letter = {0: 0, 1: 0, 2: 0, 3: 3, 4: 6, 5: 7, 6: 8, 7: 9}
    return int(points_letter[len(word)])


def check_answer(list_user, name_user, list_letters, points):
    while True:
        print(f"\nХодит {name_user}:")
        print(f"Ваши буквы: '{list_user}'")

        word = input(f"Ваше слово: ")
        if word == "stop":
            return word
            break
        if check_word_in_list(word, list_user):
            if check_word_in_file(word):
                print(f"Такое слово есть\n{name_user} "
                      f"получает {check_points(word)}")
                points += check_points(word)
                update_lists(list_letters, list_user, word)
                break
            else:
                print(f"Такого слова нет\n{name_user} не получает очков")
                list_user += create_lists_user(list_letters, 1)
                add_letter = create_lists_user(list_letters, 1)
                print(f"Добавляю следующие буквы: {add_letter}")
                break
        else:
            print("Некоторых букв у вас нет. Повторите ввод")
            continue

def show_winer(points_user_1, points_user_2, user_1, user_2):
    if points_user_1 > points_user_2:
        print(f"Победил {user_1}")
        print(f"Счёт {points_user_1} : {points_user_2}")
    else:
        print(f"Победил {user_2}")
        print(f"Счёт {points_user_1} : {points_user_2}")


def main():
    print(f"*"*50 + "\nПривет.\nМы начинаем играть в Scrabble\n" + "*"*50)
    letters = create_list_letters()

    name_user_1 = input(f"\nКак зовут первого игрока? ")
    name_user_2 = input("Как зовут второго игрока? ")
    print(f"{name_user_1} vs {name_user_2}\n(раздаю случайные буквы)")

    letter_1 = create_lists_user(letters, 7)
    letter_2 = create_lists_user(letters, 7)

    print(f"{name_user_1} - буква: '{letter_1}'")
    print(f"{name_user_2} - буква: '{letter_2}'")

    points_1 = 0
    points_2 = 0

    while True:
        word_1 = check_answer(letter_1, name_user_1, letters,points_1)
        word_2 = check_answer(letter_2, name_user_2, letters, points_2)

        if word_1 or word_2 == "stop":
            show_winer(points_1, points_2, name_user_1, name_user_2)
            break

        elif len(letters) == 0:
            print("Буквы закончились.")
            print("-"*25 + "GAME OVER" + "-"*25)
            show_winer(points_1, points_2, name_user_1, name_user_2)
            break



if __name__ == '__main__':
    main()