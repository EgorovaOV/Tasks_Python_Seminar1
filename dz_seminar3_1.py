#Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list_1 = [11, 24, 16, 100, 411, 85]
print(list_1)
#help(list)
list_1.extend(list_1 * 2)
print(list_1)
i = 0
list_2 = []
while i < len(list_1):
    if list_1[i] not in list_2:
        list_2.append(list_1[i])
    else:
        i+=1
print(list_2)








