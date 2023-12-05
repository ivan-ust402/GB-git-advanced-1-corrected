"""Домашнее задание"""
# Базовые:

# 1) Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.
# 2) Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте
# форматирование строк.
print('-------------- Задание 2 --------------')

count_of_seconds = int(input('Введите число секунд: '))

def get_formatting_time(time_in_seconds):
    """Get formatting time method"""
    hours = time_in_seconds // 3600
    minutes_in_seconds = (time_in_seconds - hours * 3600)
    minutes = minutes_in_seconds // 60
    seconds = (minutes_in_seconds - minutes * 60)
    if minutes < 10:
        minutes = str(0) + str(minutes)
    if hours < 10:
        hours = str(0) + str(hours)
    if seconds < 10:
        seconds = str(0) + str(seconds)
    print(f'{hours}:{minutes}:{seconds}')


get_formatting_time(count_of_seconds)

# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print('-------------- Задание 3 --------------')

number = input('Введите любое число n: ')

def find_sum(n_entering):
    """Find sum: n + nn + nnn"""
    n_n = n_entering * 2
    n_n_n = n_entering * 3
    return int(n_entering) + int(n_n) + int(n_n_n)

print(f'Искомая сумма: {find_sum(number)}')

# 4) Пользователь вводит целое положительное число. Найдите самую большую цифру
# в числе. Для решения используйте цикл while и арифметические операции.
print('-------------- Задание 4 --------------')

input_number = int(input('Введите целое положительное число: '))

def find_max_digit(num):
    """Find max digit"""
    max_digit = num % 10
    while num != 0:
        compare_digit = num // 10 % 10
        if compare_digit > max_digit:
            max_digit = compare_digit
        num = num // 10
    return max_digit

print(f'Максимальная цифра: {find_max_digit(input_number)}')


# 5) Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше
# издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность
# выручки (соотношение прибыли к выручке). Далее запросите численность
# сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print('-------------- Задание 5 --------------')

first_value = int(input('Введите значение выручки: '))
second_value = int(input('Введите значение издержек: '))

def check_financial_results(proceeds, costs):
    """calculation of the financial result of the company"""
    result = proceeds - costs
    if result > 0:
        print('Прибыль')
        profitability = (proceeds - costs) / proceeds
        print(f'Рентабельность: {profitability}')
        employee = int(input("Введите число сотрудников: "))
        profit_per_employee = result / employee
        print(f'Прибыль фирмы в расчете на одного сотрудника: '
              f'{profit_per_employee}')
    else:
        print('Убыток')

check_financial_results(first_value, second_value)

# 6) Спортсмен занимается ежедневными пробежками. В первый день его результат
# составил a километров. Каждый день спортсмен увеличивал результат на 10 %
# относительно предыдущего. Требуется определить номер дня, на который
# результат спортсмена составит не менее b километров. Программа должна
# принимать значения параметров a и b и выводить одно натуральное число —
# номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
print('-------------- Задание 6 --------------')

a = int(input('Введите километраж первого дня, a: '))
b = int(input('Введите километраж, который он должен достигнуть, b: '))

def calculation_days(first_distance, finish_distance):
    """Determination of the day when the athlete reaches his goal"""
    day = 1
    result = first_distance
    while result < finish_distance:
        result = result + result * 10 / 100
        day += 1
    return day

print(f'Номер дня, когда спортсмен пробежит {b} км: '
      f'{calculation_days(a, b)} день')
