txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')

_________________________________________________________________________________________________________

#вариант 1

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
turn = randint(0,2) 
if turn:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if turn:
        k = input_dat(player1)
        counter1 += k
        value -= k
        turn = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        turn = True
        p_print(player2, k, counter2, value)

if turn:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

__________________________________________________________________________________________________________

#вариант 2

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
turn = randint(0,2) 
if turn:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if turn:
        k = input_dat(player1)
        counter1 += k
        value -= k
        turn = False
        p_print(player1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        turn = True
        p_print(player2, k, counter2, value)

if turn:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")


________________________________________________________________________________________________


#вариант 3


from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
turn = randint(0,2) 
if turn:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if turn:
        k = input_dat(player1)
        counter1 += k
        value -= k
        turn = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        turn = True
        p_print(player2, k, counter2, value)

if turn:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

______________________________________________________________________________________________________________

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)



def printBoard(board):
    print('7.8.9')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print('4.5.6')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print('1.2.3')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("Ваш ход, " + turn + ".Выбери место куда поставить ")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Это место уже занято.\n Выбери другое")
            continue

        
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nИгра окончена.\n")                
                print(" **** " +turn + " победа. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print("\nИгра окончена.\n")                
                print(" **** " +turn + " победа. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nИгра окончена.\n")                
                print(" **** " +turn + " победа. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print("\nИгра окончена.\n")                
                print(" **** " +turn + " победа. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                printBoard(theBoard)
                print("\nИгра окончена.\n")                
                print(" **** " +turn + " победа. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nИгра окончена.\n")                
                print(" **** " +turn + " победа. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nИгра окончена.\n")                
                print(" **** " +turn + " победа. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nИгра окончена.\n")                
                print(" **** " +turn + " победа. ****")
                break 

       
        if count == 9:
            print("\nИгра окончена.\n")                
            

        
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    
    restart = input("Хотите повторить?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()

__________________________________________________________________________________________________________________

def run_length_encoding(seq):
  compressed = []
  count = 1
  char = seq[0]
  for i in range(1,len(seq)):
    if seq[i] == char:
      count = count + 1
    else :
      compressed.append([char,count])
      char = seq[i]
      count = 1
  compressed.append([char,count])
  return compressed
 
def run_length_decoding(compressed_seq):
  seq = ''
  for i in range(0,len(compressed_seq)):
    if compressed_seq[i].isalpha() == True:
      for j in range(int(compressed_seq[i+1])):
        seq += compressed_seq[i]
 
  return(seq)
 
seq = 'aaaasssdddwwwwwwwweeeffffff'
list1 = run_length_encoding(seq)
 
compressed_seq = ''
 
for i in range(0,len(list1)):
  for j in list1[i]:
    compressed_seq += str(j)
 
print(compressed_seq)
print(run_length_decoding(compressed_seq))
___________________________________________________________________________________________________________

