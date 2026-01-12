# ДЗ 5.1. Ім'я змінної

# import string
# import keyword

# name = input(f'Введите имя переменной:>>>>> ')

# # пустая строка НЕТ
# if name == "":
#     print(False)

# # не начинаться с цифры переменная
# elif name[0].isdigit():
#     print(False)

# #  не содержать большие буквы
# elif any("A" <= ch <= "Z" for ch in name):
#     print(False)

# #  нельзя пробелы
# elif any(ch in (set(string.punctuation) - {"_"}) for ch in name) or " " in name:
#     print(False)

# #  не быть зарезервированным словом
# elif name in keyword.kwlist:
#     print(False)

# #  можно _
# elif set(name) == {"_"} and len(name) > 1:
#     print(False)

# elif any(not (ch.isdigit() or ("a" <= ch <= "z") or ch == "_") for ch in name):
#     print(False)

# else:
#     print(True)


# ДЗ 5.2. Модифікувати калькулятор

# while True:
#     number_1 = int(input("Введіть перше число: "))
#     number_2 = int(input("Введіть друге число: "))
#     actions = input("Введіть дію (+, -, *, /): ")
#
#     if actions == "+":
#         result = number_1 + number_2
#         print(result)
#
#     elif actions == "-":
#         result = number_1 - number_2
#         print(result)
#
#     elif actions == "*":
#         result = number_1 * number_2
#         print(result)
#
#     elif actions == "/":
#         if number_2 == 0:
#             print("Ділення на нуль неможливе")
#         else:
#             result = number_1 / number_2
#             print(result)
#
#     else:
#         print("Невідома дія")
#
#     again = input("Продовжити? (y/yes - так, інше - ні): ").strip().lower()
#     if again not in ("y", "yes"):
#         print("Роботу завершено.")
#         break

# ДЗ 5.3. hashtag

import string

text = input(f'Введите имя переменной:>>>>>')

# знаки пунктуации
for ch in string.punctuation:
    text = text.replace(ch, "")

words = text.split()

# Большая буква
capitalized_words = []
for word in words:
    capitalized_words.append(word.capitalize())

# добавляем #
hashtag = "#" + "".join(capitalized_words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
