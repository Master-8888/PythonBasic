# 1. Квадрат числа

number = int(input("Введите число: "))
square = number ** 2
print(f"Квадрат числа {number} равен {square}")


# 2. “Середнє трьох чисел”

number1 = int(input("Введите число №1: "))
number2 = int(input("Введите число №2: "))
number3 = int(input("Введите число №3: "))
average = (number1 + number2 + number3) / 3
print(f"Середнє трьох чисел {number}, {number}, {number} дорівнює {average}")

# 3. “Перетворення хвилин у години”

number_of_minutes = int(input("Введіть кількість хвилин: "))
watch = number_of_minutes // 60
minutes = number_of_minutes % 60
print(f"{number_of_minutes} хвилин становить {watch} годин і {minutes} хвилин")

# v4. “Розрахунок знижки”

sum = int(input("Введіть ціну: "))
discount = int(input("Введіть знижку (%): "))
total_price = sum - (sum * discount / 100)
print(f"Ціна зі знижкою: {total_price}")

# 5. “Остання цифра числа”

numbers = int(input("Введіть 3х значное число: "))
last_digit = numbers % 10
print(f"Остання цифра числа {numbers} - {last_digit}")

# 6. “Периметр прямокутника”

length = int(input("Введіть довжину прямокутника: "))
width = int(input("Введіть ширину прямокутника: "))
perimeter = 2 * (length + width)
print(f"Периметр прямокутника зі сторонами {length} і {width} дорівнює {perimeter}")

# 7. Виведення числа в стовпчик

numbers = int(input("Введіть число: "))
first_digit = numbers // 1000
second_digit = (numbers // 100) % 10
third_digit = (numbers // 10) % 10
last_digit = numbers % 10

print(first_digit)
print(second_digit)
print(third_digit)
print(last_digit)

''''''nbjhhjbkjbkbh'''