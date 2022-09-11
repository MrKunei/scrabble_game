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
    Создание рандомного списка букв для игрока
    """
    list_user = random.sample(list_letters, index)
    for letter in list_user:
        list_letters.remove(letter)
    return list_user


def check_word_in_list(word, list_user):
    """
    Проверка наличия букв введенного слова в списке игрока
    """
    counter = 0
    list_letter = list_user[:]  #копия списка для проверки повторяющихся букв
    letters_word = list(word)
    for letter in letters_word:
        if letter in list_letter:
            counter += 1
            list_letter.remove(letter)
    if counter == len(letters_word):
        return True
    else:
        return False


def list_word_in_file():
    """
    Выгрузка слов в спискок из файла
    """
    file_words = []
    with open("ru_word.txt", encoding="utf-8") as file:
        for line in file:  # чтение файла по строкам
            file_words.append(line.rstrip())
    return file_words

def check_word_in_file(word, file_words):
    """
    Проверка наличия слов в списке выгруженном из файла
    """
    if word in file_words:
        return True


def update_lists_true_answer(list_letters, list_user, word):
    """
    Обновление списков если слово есть
    """
    add_letters = []
    for letter in list(word):
        list_user.remove(letter)  # удаление букв из списка игрока
    # проверка хватает ли букв в списке для добавления
    if len(list_letters) >= len(list(word)) + 1:
        i = 0
        while i < len(list(word)) + 1:
            #добавление и удаление букв по одной
            #чтобы избежать рандомного повторения букв в единственном экземпляре
            add_letter = create_lists_user(list_letters, 1)
            add_letters += add_letter
            i += 1
    else:
        i = 0
        while i < len(list_letters):
            add_letter = create_lists_user(list_letters, 1)
            add_letters += add_letter
            i += 1

    list_user += add_letters
    # вывод добавленных букв в виде строки
    add_letters_str = ", ".join(add_letters)
    print(f"Добавляю следующие буквы: {add_letters_str}")

def update_lists_false_answer(list_letters, list_user):
    """
    Обновление списка если слова нет
    """
    add_letter = create_lists_user(list_letters, 1)
    list_user += add_letter
    add_letter_str = "".join(add_letter)
    print(f"Добавляю следующие буквы: {add_letter_str}")


def check_points(word):
    """
    Возврат баллов за правильный ответ, согласно таблице за каждую букву
    """
    point_user = 0
    points_letter = {"а": 1, "б": 3, "в": 1, "г": 3, "д": 2, "е": 1, "ё": 3,
                     "ж": 5, "з": 5, "и": 1, "й": 4, "к": 2, "л": 2, "м": 2,
                     "н": 1, "о": 1, "п": 2, "р": 1, "с": 1, "т": 1, "у": 2,
                     "ф": 10, "х": 5, "ц": 5, "ч": 5, "ш": 8, "щ": 10, "ъ": 10,
                     "ы": 4, "ь": 3, "э": 8, "ю": 8, "я": 3}
    for letter in word:
        point_user += points_letter[letter]
    return point_user

def print_info_add_points(point, name_user):
    if point == 3:
        print(f"{name_user} получает {point} балла")
    else:
        print(f"{name_user} получает {point} баллов")


def show_winer(points_1, points_2, user_1, user_2):
    """
    Вывод информации о победителе
    """
    if sum(points_1) > sum(points_2):
        print(f"Победитель {user_1}")
        print(f"Счёт {sum(points_1)} : {sum(points_2)}")
    else:
        print(f"Победитель {user_2}")
        print(f"Счёт {sum(points_1)} : {sum(points_2)}")


def check_answer(list_user, name_user, list_letters, points_user, file_words):
    """
    Ход игрока: проверка ответа, обновление списка, начисление очков за слово
    """
    while True:
        print(f"\n" + "_" * 15 + f"Ходит {name_user}:" + "_" * 15)
        list_user_str = ", ".join(list_user)
        print(f"Ваши буквы: {list_user_str}")
        word = input(f"Ваше слово: ").lower()

        if word == "stop":  # проверка ввода на "stop" для выхода
            break
        # проверки на правильность слова и обновление списков
        elif check_word_in_list(word, list_user):
            if check_word_in_file(word, file_words):
                point = check_points(word)
                print(f"Такое слово есть")
                print_info_add_points(point, name_user)
                update_lists_true_answer(list_letters, list_user, word)
                points_user.append(point)
                break
            else:
                print(f"Такого слова нет\n{name_user} не получает баллов")
                update_lists_false_answer(list_letters, list_user)
                break
        else:
            print("Некоторых букв у вас нет. Попробуйте ещё раз.")
            continue
    return word


def main():
    points_1 = [] # списки для учета баллов
    points_2 = []

    file = list_word_in_file()

    print(f"-" * 50 + "\nПривет.\nМы начинаем играть в Scrabble\n" + "-" * 50)
    letters = create_list_letters()

    name_user_1 = input(f"\nКак зовут первого игрока? ").lower().title()
    name_user_2 = input("Как зовут второго игрока? ").lower().title()
    print(f"{name_user_1} vs {name_user_2}\n(раздаю случайные буквы)")

    letter_1 = create_lists_user(letters, 7)
    letter_2 = create_lists_user(letters, 7)

    #для вывода списков в виде строки
    str_user_1 = ", ".join(letter_1)
    str_user_2 = ", ".join(letter_2)
    print(f"{name_user_1} - буква: {str_user_1}")
    print(f"{name_user_2} - буква: {str_user_2}")

    while True:
        if len(letters) == 0:  # если закончились буквы в списке
            print("Буквы закончились.")
            break
        """
        Ход первого игрока
        """
        word_1 = check_answer(letter_1, name_user_1, letters, points_1, file)
        if word_1 == "stop":
            break
        """
        Ход второго игрока
        """
        word_2 = check_answer(letter_2, name_user_2, letters, points_2, file)
        if word_2 == "stop":
            break



    print("-" * 25 + "GAME OVER" + "-" * 25)
    show_winer(points_1, points_2, name_user_1, name_user_2)


if __name__ == '__main__':
    main()

