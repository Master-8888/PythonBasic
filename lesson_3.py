# ДЗ 3.1. Найпростіший калькулятор

number_1 = int(input("Введіть перше число: "))
number_2 = int(input("Введіть друге число: "))
actions = input("Введіть дію (+, -, *, /): ")
if actions == "+":
    result = number_1 + number_2
    print(result)
elif actions == "-":
    result = number_1 - number_2
    print(result)
elif actions == "*":
    result = number_1 * number_2
    print(result)
elif actions == "/":
    if number_2 == 0:
        print("Ділення на нуль неможливе")
    else:
        result = number_1 / number_2
        print(result)
else:
    print("Невідома дія")


# ДЗ 3.2. Перемістити елемент у списку

numbers = [1, 2, 3, 4, 5]
x = numbers.pop()
numbers.insert(0, x)
print(numbers)

# ДЗ 3.3. Розділити один список на два списки

numbers = [1, 2, 3, 4, 5, 6]
first_list = numbers[:3]
second_list = numbers[3:]
print(first_list)
print(second_list)

numbers_1 = [1, 2, 3]
first_list_1 = numbers_1[:2]
second_list_1 = numbers_1[2:]
print(first_list_1)
print(second_list_1)

numbers_2 = [1, 2, 3, 4, 5]
first_list_2 = numbers_2[:3]
second_list_2 = numbers_2[3:]
print(first_list_2)
print(second_list_2)

numbers_3 = [1]
first_list_3 = numbers_3[:1]
second_list_3 = numbers_3[1:]
print(first_list_3)
print(second_list_3)

numbers_4 = []
first_list_4 = numbers_4[:1]
second_list_4 = numbers_4[1:]
print(first_list_4)
print(second_list_4)

