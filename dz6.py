import random
a = [1,2,7,5,4]
print(a)
x = [a[i] for i in range(1, len(a), 2)]
print(f"Сумма элементов списка, стоящих на нечётной позиции {sum(x)}")
------------------------------------------------------------------------------------------------------

def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)

------------------------------------------------------------------------------------------------------

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")

------------------------------------------------------------------------------------------------------

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))