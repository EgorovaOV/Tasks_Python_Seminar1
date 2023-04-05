#Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами
#поскольку я ничего не создала, то я просто сделаю пакет из всех дз

import os
import shutil
#ниже я закомментирую код, которым скопировала все из папки PythonAvtoGB в папку с моим пакетом my_packet

#for file in os.listdir('C:\\Users\\Olga\\PycharmProjects\\PythonAvtoGB'):
 #   if file.startswith('dz_seminar'):
  #      shutil.copytree('C:\\Users\\Olga\\PycharmProjects\\PythonAvtoGB', 'my_packet')

from my_packet import dz_seminar5_1 as dz51

x = dz51.my_path('C:\\Users\\Olga\\PycharmProjects\\PythonAvtoGB')






