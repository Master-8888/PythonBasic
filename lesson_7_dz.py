# ДЗ 7.1. Вітання

# def say_hi(name, age):
#     return f"Hi. My name is {name} and I'm {age} years old"
#
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
# print("OK")

#ДЗ 7.2. Модифікувати рядок

# def correct_sentence(text):
#     # 1. Делаем первую букву заглавной
#     text = text[0].upper() + text[1:]
#
#     # 2. Если нет точки в конце — добавляем
#     if not text.endswith("."):
#         text += "."
#
#     return text
#
# assert correct_sentence("greetings, friends") == "Greetings, friends."
# assert correct_sentence("hello") == "Hello."
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
# assert correct_sentence("Greetings, friends.") == "Greetings, friends."
# assert correct_sentence("greetings, friends.") == "Greetings, friends."
# print("OK")


#ДЗ 7.3. Пошук підрядка

# def second_index(text, some_str):
#     first = text.find(some_str)
#
#     if first == -1:
#         return None
#
#     second = text.find(some_str, first + 1)
#
#     if second == -1:
#         return None
#
#     return second
#
# assert second_index("sims", "s") == 3
# assert second_index("find the river", "e") == 12
# assert second_index("hi", "h") is None
# assert second_index("Hello, hello", "lo") == 10
# print("OK")


#ДЗ 7.4. Пошук спільних елементів

def common_elements():
    list_3 = [x for x in range(100) if x % 3 == 0]
    list_5 = [x for x in range(100) if x % 5 == 0]

    set_3 = set(list_3)
    set_5 = set(list_5)

    return set_3 & set_5

