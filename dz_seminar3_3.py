#Создайте словарь со списком вещей для похода
# в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

my_things = dict(cup=200, shugar=300, tent=1000, salt=100, chaynik=500,spichki=150)#список вещей и их вес
print('You have this: ')
for key in my_things.keys():
    print(key)# распечатаем какие вещи есть
MAX_BACKPACK = 2000#максимальный вес рюкзака
backpack = 0#реальный вес рбкзака
my_list = []#список вещей, который поместится в рюкзак
while backpack <= MAX_BACKPACK:# пока реальный рюкзак не больше максимального
    print('What things you want to take?')#что ты хочешь взять
    a = input()
    my_list.append(a)#добавляем это в список вещей
    backpack = backpack + my_things[a]#вычимсляем новый реальный вес рюкзака
    if backpack <= MAX_BACKPACK:
        print(f'you take {my_list}, your backpack weighs {backpack}')
    else:
        print(f'Sorry, your backpack can take only {MAX_BACKPACK}')









