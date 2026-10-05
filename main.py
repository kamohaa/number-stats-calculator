# Задание 3
number_list = []
user_input = ''
while(user_input.lower() != "стоп"):
    user_input = input("Введите число, либо 'стоп' чтобы остановиться: ")
    if(user_input.lower() == "стоп"):
        break
    try:
        numbers = float(user_input)
        number_list.append(numbers)
    except ValueError:
        print("Вы ввели не число")

if not number_list:
    print("Ваш список пуст")
else:
    addition = sum(number_list)
    avrg = addition / len(number_list)
    maximum = max(number_list)

    print("Ваш список чисел: ")
    for number in number_list:
        print(number, end=" ")

    print()
    print(addition, ' - сумма ваших чисел.')
    print(avrg, ' - среднее арифметическое ваших чисел.')
    print(maximum, ' - максимальное среди ваших чисел.')

    with open("results.txt", "w") as f:
        f.write(f"{addition} - сумма ваших чисел.\n")
        f.write(f"{avrg} - среднее арифметическое ваших чисел.\n")
        f.write(f"{maximum} - максимальное среди ваших чисел.\n")
    print("Был создан файл 'results.txt' с результатом работы!")



# # Задание 2
# stop_word = ""
# while (stop_word != "стоп"):
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     addition = a + b
#     avrg = (a + b) / 2
#     maximum = max(a, b)
#     print(addition, ' - сумма ваших чисел.')
#     print(avrg, ' - среднее арифметическое ваших чисел.')
#     print(maximum, ' - максимальное среди ваших чисел.')
#     stop_word = input("Введите 'стоп' чтобы остановить: ")


# # Задание 1
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# addition = a + b
# avrg = (a + b) / 2
# maximum = max(a, b)
# print(addition, ' - сумма ваших чисел.')
# print(avrg, ' - среднее арифметическое ваших чисел.')
# print(maximum, ' - максимальное среди ваших чисел.')
