# ДЗ 6.1. Діапазон букв

import string

letters = string.ascii_letters

user = input('Введите диапазон букв (например: a-c): ')
start, end = user.split("-")

start = letters.index(start)
end_index = letters.index(end)

result = letters[start:end_index + 1]

print(result)

# ДЗ 6.2. Конвертер із числа в дату

import datetime

seconds = int(input('Введите количество секунд: '))

days = seconds // 86400
seconds = seconds % 86400

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

if days == 1:
    day_word = "день"
elif days < 5:
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")


# ДЗ 6.3. Добуток чисел

number = input('введите число: ')

while len(number) > 1:
    result = 1

    for digit in number:
        result *= int(digit)

    number = str(result)

print(number)
