'''Задача 3. Список уникальных цифр числа'''

number = input('Введите целое неотрицательное число: ')
numbers = list(map(int, number))
unique_numbers = list(set(numbers))
print('Cписок уникальных цифр целого числа в порядке возрастания:')
print(unique_numbers)
