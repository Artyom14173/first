print("Добро пожаловать в программу робот.\nЕго изначальная позиция - Север.")
position = 11 #11 - Север. 12 - Запад. 13 - Юг. 14 - Восток
#While true - Бесконечный цикл. Тоесть программа повторяется н-ное кол-во раз.
while True:
    print("Команды: 0 = продолжить движение, 1 = повернуть налево, -1 = повернуть направо")
    command = int(input("Введите команду: ")) #Вводится комманды 0 = продолжить движение, 1 = повернуть налево, -1 = повернуть направо
    #рассматриваются все возможные случаи ходов робота н-ное кол-во раз.
    if position == 11:
        if command == 0:
            position = 11
            print("Север")
        elif command == 1:
            position = 12
            print("Запад")
        elif command == -1:
            position = 14
            print("Восток")
    elif position == 12:
        if command == 0:
            position = 12
            print("Запад")
        elif command == 1:
            position = 13
            print("Юг")
        elif command == -1:
            position = 11
            print("Север")
    elif position == 13:
        if command == 0:
            position = 13
            print("Юг")
        elif command == 1:
            position = 14
            print("Восток")
        elif command == -1:
            position = 12
            print("Запад")
    elif position == 14:
        if command == 0:
            position = 14
            print("Восток")
        elif command == 1:
            position = 11
            print("Север")
        elif command == -1:
            position = 13
            print("Юг")
       