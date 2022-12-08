def calcPi(limit):  #функция задающая максимальное число пи после запятой.
    

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
            if 4 * q + r - t < n * t:
                    
                    yield n
                  
                    if counter == 0:
                            yield '.'
                   
                    if decimal == counter:
                            print('')
                            break
                    counter += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr


def main(): #Функция расчета пи с заданым лимитом 

    
    pi_digits = calcPi(int(input("Введите желаемое количество чисел после запятой: ")))

    i = 0

    
    for d in pi_digits:
            print(d, end='')
            i += 1
            

if __name__ == '__main__':
    main()


-----------------------------------------------------------------------------------------------------

n = int(input("Введите число для разбивания на множетели: "))
i = 1
 
while(i <= n):
    c = 0
    if(n % i == 0):
        j = 1
        while(j <= i):
            if(i % j == 0):
                c = c + 1
            j = j + 1
             
        if (c == 2):
            print(i)
    i = i + 1

---------------------------------------------------------------------------------------------------

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")

---------------------------------------------------------------------------------------------------





import random


def file(file_name): 
    make_file(file_name)  
    f = open(file_name, 'a')
    f.write(solution())  
    f.close()


def make_file(file_name):       
    f = open(file_name, 'w')
    f.close()


def solution():   
    n = int(input("вводим степень многочлена "))
    equa = ''
    for i in range(n, -1, -1):
        k = kf(i)  
        if k != 0:
            if i > 1:
                el = str(k)+'*x^'+str(i)
            elif i == 1:
                el = str(k)+'*x'
            else:
                el = str(k)
        
        equa = equa + "+" + el
    equa = equa[1:]  
    print(equa)
    return equa


def kf(n): 
    k = random.randint(0, 101)
    return k


if __name__ == '__main__':
    file_name = 'text.txt' 
    file(file_name)
    file_name = 'text1.txt' 
    file(file_name)


_____________________________________________________________________________


import random

# запись в файл
def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

# создание случайного числа от 0 до 100
def rnd():
    return random.randint(0,101)

# создание коэффициентов многочлена
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
# создание многочлена в виде строки 
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# получение степени многочлена
def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена
def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов
def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    


# создание двух файлов

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file("file34_1.txt", create_str(koef1))
write_file("file34_2.txt", create_str(koef2))

# нахождение суммы многочлена

with open('file34_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file34_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])
write_file("file34_res.txt", create_str(lst_new))
with open('file34_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")


