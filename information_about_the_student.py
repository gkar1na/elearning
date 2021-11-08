from time import *
import os
from typing import TextIO

i = int(input('Введите ID ученика: '))  # Номер пользователя

os.system('cls')

# Проверка наличия ID
try:
    text_file = open('bin/users/user_' + str(i) + '.txt', 'r') # Попытка открытие файла с данными
except FileNotFoundError:
    # Закрытие программы
    print('\nУченика с таким ID нет. Пожалуйста, введите корректный номер.')
    print('\nЧтобы закрыть программу нажмите "Ctrl" + "C" или крестик в правом верхнем углу\n')
    time = 600
    while time >= 0:
        print('\r', 'Программа автоматически закроется через ' + str(time), end='   ')
        sleep(1)
        time -= 1

user = str(text_file.read())  # Перенос информации с файла в переменную
text_file.close()  # Закрытие файла с данными

# Считывание имени, фамилии, отчества
p = user.index('\n')
name = user[:p]
surname, name, patronymic = name.split(' ')
user = user[p + 1:]

# Считывание класса, буквы класса
p = user.index('\n')
x = user.index(' ')
if p > x:
    grade, letter = user[:p].split(' ')
    user_works = user[p + 2:]
else:
    grade = user[:p]
    letter = ''
    user_works = user[p + 2:]

# Считывание результатов работ
count_works = user_works.count('Работа')
p = 0
works = []
while p < count_works-1:

    works.append([])
    x = user_works.index('Р')
    y = user_works.index('\n')
    user_works = user_works[y+1:] # удаление "работа"

    y = user_works.index('\n')
    works[p].append(user_works[:y]) # запись баллов

    y = user_works.index('\n')
    user_works = user_works[y+1:] # удаление баллов

    y = user_works.index('\n')
    works[p].append(user_works[:y]) # запись оценки

    user_works = user_works[y+2:] # удаление оценки

    p += 1

# Средний балл
p = 0
average_mark = 0
number_of_works = len(works)
while p < number_of_works:
    mark = works[p][1]
    if mark == '5+':
        mark = 6
        average_mark += mark
    else:
        average_mark += int(works[p][1])
    p += 1
average_mark = round(average_mark / number_of_works, 2)

answers = ''
n = len(works)
for i in range(n):
    work = works[i]
    answers = answers + '   ' + str(i + 1) + ') ' + str(work[0]) + ' - ' + str(work[1])
    if i < n - 1:
        answers = answers + '\n'

print('\n')

# Вывод информации об ученике
print('* Информация об ученике с ID ' + str(i) + ':\n' +
      'Фамилия: ' + surname + '\n' +
      'Имя: ' + name + '\n' +
      'Отчество: ' + patronymic + '\n' +
      'Класс: ' + grade + '\n' +
      'Буква: ' + letter + '\n' +
      'Средний балл: ' + str(average_mark) + '\n' +
      'Результаты:\n' + answers)

# Закрытие программы
print('\nЧтобы закрыть программу нажмите "Ctrl" + "C" или крестик в правом верхнем углу\n')
time = 600
while time >= 0:
    print('\r', 'Программа автоматически закроется через ' + str(time), end='   ')
    sleep(1)
    time -= 1
