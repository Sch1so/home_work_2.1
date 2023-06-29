# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

quan_el = int(input('Введите колличество эллементов списка -> '))
list = []

for i in range(quan_el):
    list.append(int(input(f'Введите {i + 1} эллемент списка -> ')))

num = int(input('Введите число которое хотите найти в списке -> '))
count = 0
for j in range(len(list)):
    if num == list[j]:
        count += 1

print(*list)
print(f'Число {num} встречается в списке {count} раз')


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

import random

quan_el = int(input('Введите колличество эллементов списка -> '))
min_num = int(input('Введите минимальное значение списка -> '))
max_num = int(input('Введите максимальное значение списка -> '))
list_new = []

for i in range(quan_el):
    list_new.append(int(random.randint(min_num, max_num)))

num_new = int(input('Введите число -> '))
my_list = []

for i in range(len(list_new)):
    if list_new[i] > num_new:
        
        my_list.append(list_new[i] - num_new)
    else:
        my_list.append(num_new - list_new[i])

num_index = 0
numbder = my_list[0]

for i in range(len(my_list) - 1):
    if numbder >= my_list[i + 1]:
        num_index = i + 1
        numbder = my_list[i + 1]

print(*list_new)
print(f'Ближайшее к числу {num_new} является -> {list_new[num_index]}')




# task 20 В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с 
# английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу,
# которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

russ_scrb = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10
}
eng_scrb = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

import re
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))
word = input('Введите слово ')
word = word.upper()
word_list = []

for wordls in word:
    word_list += wordls

score = 0
if isCyrillic(word):
    for i in range(len(word_list)):
        score += russ_scrb.get(word_list[i])
else:
     for i in range(len(word_list)):
        score += eng_scrb.get(word_list[i])
print(score)