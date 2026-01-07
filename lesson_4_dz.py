# ДЗ 4.1. Перемістити всі нулі до кінця списку

numbers = [1, 0, 2,0,  3, 0, 4, 5, 0, 0, 0]

def move_zeros_to_end(lst):
    non_zero_elements = [num for num in lst if num != 0]
    zero_elements = [num for num in lst if num == 0]
    return non_zero_elements + zero_elements

result = move_zeros_to_end(numbers)
print(result)

# ДЗ 4.2. Знайти суму елементів із парними індексами

numbers = [0, 1, 7, 2, 4, 8] * 8

def sum_even_index_elements(lst):
    return sum(lst[i] for i in range(0, len(lst), 2))

result = sum_even_index_elements(numbers)
print(result)

# ДЗ 4.3. Список із 3 елементів

import random

length = random.randint(3, 10)
lst = [random.randint(1, 10) for _ in range(length)]

result = [lst[0], lst[2], lst[-2]]

print("Початковий список:", lst)
print("Фінальний список:", result)
