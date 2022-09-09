import random

dict_alfa = {"а": 8, "б": 2, "в": 4, "г": 2, "д": 4, "е": 8, "ё": 1, "ж": 1,
             "з": 2, "и": 5, "й": 1, "к": 4, "л": 4, "м": 3, "н": 5, "о": 10,
             "п": 4, "р": 5, "с": 5, "т": 5, "у": 4, "ф": 1, "х": 1, "ц": 1,
             "ч": 1, "ш": 1, "щ": 1, "ъ": 1, "ы": 2, "ь": 2, "э": 1, "ю": 1,
             "я": 2}


def create_list_letters():
    """
    Создание списка букв из словаря
    """
    string_letters = ""
    for letter, quantity in dict_alfa.items():
        letters = letter * quantity
        string_letters += letters
    list_letters = list(string_letters)
    return list_letters


def create_lists_user(list_letters, index):
    """
    Создание рандомного списка букв игрока
    """
    list_user = random.sample(list_letters, index)
    return list_user


def check_word_in_list(word, list_user):
    """
    Проверка на наличие букв введенного слова в списке игрока
    """
    counter = 0
    list_letter = list_user[
                  :]  # копия списка игрока для проверки повторяющихся букв
    letters_word = list(word)
    for letter in letters_word:
        if letter in list_letter:
            counter += 1
            list_letter.remove(letter)
    if counter == len(letters_word):
        return True
    else:
        return False


def check_word_in_file(word):
    """
    Проверка слова в списке файла
    """
    with open("russian_word.txt", encoding="utf-8") as file:
        for line in file:  # чтение файла по строкам
            if word == line.rstrip():  # сравнение слова со строкой файла
                return True


def update_lists(list_letters, list_user, word):
    """
    Обновление списков при правильном слове
    """
    for letter in list(word):
        list_user.remove(letter)  # удаление букв из списка игрока

    add_letter = create_lists_user(list_letters, len(word) + 1)
    list_user += add_letter

    for add in add_letter:
        list_letters.remove(
            add)  # удаление из общего списка букв добавленных игроку

    add_letter_str = ", ".join(add_letter)
    print(f"Добавляю следующие буквы: {add_letter_str}")


def check_points(word):
    """
    Проверка количества баллов за правильный ответ, согласно количеству букв в слове
    """
    points_letter = {0: 0, 1: 0, 2: 0, 3: 3, 4: 6, 5: 7, 6: 8, 7: 9}
    point = points_letter[len(word)]
    return point


def show_winer(points_1, points_2, user_1, user_2):
    """
    Вывод информации о победителе
    """
    if points_1 > points_2:
        print(f"Победитель {user_1}")
        print(f"Счёт {points_1} : {points_2}")
    else:
        print(f"Победитель {user_2}")
        print(f"Счёт {points_1} : {points_2}")


def check_answer(list_user, name_user, list_letters, points_user):
    """
    Ход игрока, проверка ответа, обновление списка, начисление очков за слово
    """
    while True:
        print(f"\n" + "_" * 15 + f"Ходит {name_user}:" + "_" * 15)
        list_user_str = ", ".join(list_user)
        print(f"Ваши буквы: '{list_user_str}'")
        word = input(f"Ваше слово: ").lower()

        if word == "stop":  # проверка ввода на "stop" для выхода
            return word
            break

        elif check_word_in_list(word, list_user):
            if check_word_in_file(word):
                point = check_points(word)
                print(f"Такое слово есть\n{name_user} "
                      f"получает {point}")
                update_lists(list_letters, list_user, word)
                print(f"Ваши очки: {points_user}")
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


def main():
    print(f"-" * 50 + "\nПривет.\nМы начинаем играть в Scrabble\n" + "-" * 50)
    letters_list = create_list_letters()

    name_user_1 = input(f"\nКак зовут первого игрока? ").lower().title()
    name_user_2 = input("Как зовут второго игрока? ").lower().title()
    print(f"{name_user_1} vs {name_user_2}\n(раздаю случайные буквы)")

    letter_1 = create_lists_user(letters_list, 7)
    letter_2 = create_lists_user(letters_list, 7)

    str_user_1 = ", ".join(letter_1)
    str_user_2 = ", ".join(letter_2)

    print(f"{name_user_1} - буква: '{str_user_1}'")
    print(f"{name_user_2} - буква: '{str_user_2}'")

    while True:
        points_1 = 0
        points_2 = 0
        """
        Ход первого игрока
        """
        word_1 = check_answer(letter_1, name_user_1, letters_list, points_1)
        if word_1 == "stop":
            show_winer(points_1, points_2, name_user_1, name_user_2)
            print("-" * 25 + "GAME OVER" + "-" * 25)
            break
        """
        Ход второго игрока
        """
        word_2 = check_answer(letter_2, name_user_2, letters_list, points_2)
        if word_2 == "stop":
            print("-" * 25 + "GAME OVER" + "-" * 25)
            show_winer(points_1, points_2, name_user_1, name_user_2)
            break

        elif len(letters_list) == 0:  # если закончились буквы в списке
            print("Буквы закончились.")
            print("-" * 25 + "GAME OVER" + "-" * 25)
            show_winer(points_1, points_2, name_user_1, name_user_2)
            break


if __name__ == '__main__':
    main()
