#Напишите функцию, которая принимает на вход строку
# - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла

def my_path(a):
   *path, name_extension = a.split('\\')# упакуем путь в две части - путь и имя+расширение
   name, extension = name_extension.split('.')#разделим имя+расширение на имя и расширение
   full_path = '\\'.join(path)#соберем путь в один элемент
   my_path_to_file = full_path, name, extension# соберем все в кортеж из трех элементов: путь, имя, расширение
   print(my_path_to_file)


b ='C:\\Users\\Olga\\PycharmProjects\\PythonAvtoGB\\dz_seminar5_1.py'

my_path(b)
