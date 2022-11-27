



#num=int(input("введите номер дня недели: "))
#if num < 6: 
#	print("День недели не является выходным")
#else:
#	print("день недели выходной")
#
#if num>7 or num<0:
#	print("такого дня недели не существует")






#import random

#x=random.randint(0,1)
#y=random.randint(0,1)
#z=random.randint(0,1)
#print(x)
#print(y)
#print(z)
#if((not (x or y or z)) == (not x and not y and not z)):
#	print("Утверждение доказано")





#print("Х и Y не могут быть равны нулю")
#X=int(input("введите координаты для оси Х: "))
#Y=int(input("введите координаты для оси Y: "))

#if X==0 or Y==0:
#	print("вы ввели не верное число повторите еще раз")
#	exit()
#if X>0 and Y>0:
#	print("первая четверть")
#if X<0 and Y<0:
#	print("третья четверть")
#if X>0 and Y<0:
#	print("четвертая четверть")
#if X<0 and Y>0:
#	print("вторая четверть")







#num=int(input("Задайте номер четверти что бы узнать диапазон координат(минимальное число 1 максимальное 4): "))
#
#if num<0 or num>4:
#	print("вы ввели не верное число повторите еще раз")
#	exit()
#
#if num==1:
#	print("В данной четверти Х и Y могут равнятся от 0 до +∞ ")
#if num ==2:
#	print("В данной четверти Х будет равен от 0 до -∞ и Y может равнятся от 0 до +∞ ")
#if num ==3:
#	print("В данной четверти Х и Y могут равнятся от 0 до -∞ ")
#if num ==4:
#	print("В данной четверти Y будет равен от 0 до -∞ и X может равнятся от 0 до +∞ ")




import math
x1 = float(input("x1 - "))
y1 = float(input("y1 - "))
x2 = float(input("x2 - "))
y2 = float(input("y2 - "))
a = math.sqrt((x2-x1)**2+(y2-y1)**2)
print('{:.3f}'.format(a), sep='')
