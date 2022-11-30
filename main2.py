
x = input("Введите число ")

def summa(x):                            
    if float(x) < 0:                            
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f"Сумма чисел равна {summa(x)}")



_____________________________

input_num = int(input("Введите число: "))
list = [1]

for i in range (1,input_num):
    list.append ((i+1) * list [i-1])

print(list)

________________________________

n = int(input("Введите число : ")) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))
____________________________________



from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-20,10))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print("Задайте количество элементов: ", get_numbers(numbers))

x = int(input("Задайте позицию первого элемента: "))
y = int(input("Задайте позицию второго элемента: "))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f"Умножение элементов: {numbers[x -1]} * {numbers[y -1]} =", mult)





____________________________________




import random

s = "Строка"
new_s = []


s = list(s)
while s:
    i = random.randint(0, len(s)-1)
    new_s.append(s.pop(i))
print("".join(new_s))

