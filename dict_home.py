# Пользователь вводит текст. Все слова разделены одним пробелом.
# Задача: вычленить все слова и с помощью словаря подсичитать какое слово
# и сколько раз встречается в тексте

# Решение:
# создать список из предложений, все слова перевести в нижний регистр
# создать пустой словарь
# если слово второй всречается, то +1

# Однажды в студеную зимнюю пору. Я из лесу вышел.
# Ночь улица фонарь аптека

string = 'Однажды Однажды в студеную зимнюю пору'.strip().lower()
#string = input('Введите текст: ').strip().lower()
print(string)
#lst= list(input('Введите текст: ').strip().lower())
#lst= list('Введите текст: ').strip().lower()
# print(lst)

#items_string = "яблоко,банан,вишня"
lst = string.split(" ") # Разделяем по запятой
print(lst)

#people = ["Tom", "Sam", "Bob"]
# for word in lst:
#     print(lst)

d = {}
for i in lst:
    d[i] = 1
    if i not in d:
        d[i] = lst.count(i)
    else:
        d[i] + 1
#----------------
#print(d{i,lst(i)})
# i = 0
# for i in range(lst):
#     num = {index(lst): x}

#d = dict.fromkeys(lst, 0)
#d = dict.fromkeys(index(lst),lst)
#d = dict.index(lst)
print(d)
print(list(d.items()))
#----------------
i = 0
for key in d:
    if key in d:
        v = i + 1
        #d = {key, i}
        #print(key, v)
        print(v, key)
        #print(key, d[key, values])
print(list(d.items()))
#print(list(d.keys()))
#print(list(d.values()))
# d = {
#     'пользователь:' 1,
#     'вводит': 1
# }
#
# for

s = 'Пользователь вводит текст. Все слова разделены пробелом'
d = {} # пока пустой словарь
s = s.lower() # перевод в нижний регистр
lst = sorted(s.split())

for word in let: # если слово есть в словаре
    if word in d.keys()
