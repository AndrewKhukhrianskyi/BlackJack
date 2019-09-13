import random
player_1 = random.randint(2,11)
player_2 = random.randint(2,11)
name = input(" Введите имя 1-го игрока: " )
name_2 = input(" Введите имя 2-го игрока: " )

print(" Карта " ,name, ":", player_1)
print(" Карта " ,name_2, ":", player_2)
for i in range(8):
    print( name, " тянет карту: ")
    player_choose = int(input(" Тянете еще?(Да = 1, Нет = 2): "))
    if player_choose == 1:
        card = random.randint(2,11)
        player_1+= card
    elif player_choose == 2:
        print(name, " заканчивает ход ")
        break
    print(" Текущий результат ", name, ":", player_1)
for i in range(8):
    print( name_2, " тянет карту: ")
    player2_choose = int(input(" Тянете еще?( Да = 1, Нет = 2):"))
    if player2_choose == 1:
        card = random.randint(2,11)
        player_2 += card
    elif player_choose == 2:
        print(name_2, " заканчивает ход ")
        break
    print(" Текущий результат ", name_2, ":", player_2)

if player_1 < 21 and player_2 > 21:
    print( name, " победил! " )
    print( " Текущее значение карт игроков: ",name," - ", player_1, name_2, " - ", player_2)
elif player_1 > 21 and player_2 > 21:
    if player_1 == player_2:
        print(" Ничья ")
    print( " У обоих игроков перебор значений карт - победит тот игрок, у которого значение ближе к значению 21 ")
    print( " Текущее значение карт игроков: ",name," - ", player_1, name_2, " - ", player_2)
    while True:
        player_1-=1
        player_2-=1
        if player_1 == 21 or player_2 == 21:
            break          
    print( " Текущее значение карт игроков: ",name," - ", player_1, name_2, " - ", player_2)
    if player_1 == 21:
        print( name, " победил! " )
    if player_2 == 21:
        print( name_2, " победил! " )
elif player_1 > 21 and player_2 < 21:
    print( name_2, " победил! " )
    print( " Текущее значение карт игроков: ",name," - ", player_1, name_2, " - ", player_2)
elif player_1 > player_2:
    print( name, " победил! " )
    print( " Текущее значение карт игроков: ",name," - ", player_1, name_2, " - ", player_2)
elif player_1 < player_2:
    print( name_2, " победил! " )
    print( " Текущее значение карт игроков: ",name," - ", player_1, name_2, " - ", player_2)
elif player_1 == player_2:
    print( " Ничья ")
    print( " Текущее значение карт игроков: ",name," - ", player_1, name_2, " - ", player_2)


    
