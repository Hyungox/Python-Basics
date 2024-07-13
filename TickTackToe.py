import random
def Choose(index,player):
    try:
        index = int(index)
        if lista[index] == '   ':
            lista[index]= lista[index].replace('   ', f'{player}')
            return lista
        else:
            i = input('Space taken! Pick other space!')
            Choose(i, player)
    except:
        i = input('Wrong input! Pick other space! ')
        Choose(i, player)
def Victory(player):
    print(f'\033[4m{lista[0]}|{lista[1]}|{lista[2]}')
    print(f'{lista[3]}|{lista[4]}|{lista[5]}\033[0m')
    print(f'{lista[6]}|{lista[7]}|{lista[8]}')
    print(f'Congratulations {player1}') if player==' x ' else print(f'Congratulations {player2}')
    gra = False
    return gra
def CheckForWin(list,mark):
    if lista[0] == lista[1] == lista[2] == (' x ' or ' o '):
        gra=Victory(mark)
        return gra
    elif lista[3] == lista[4] == lista[5] == (' x ' or ' o '):
        gra=Victory(mark)
        return gra
    elif lista[6] == lista[7] == lista[8] == (' x ' or ' o '):
        gra = Victory(mark)
        return gra
    elif lista[0] == lista[3] == lista[6] == (' x ' or ' o '):
        gra = Victory(mark)
        return gra
    elif lista[1] == lista[4] == lista[7] == (' x ' or ' o '):
        gra = Victory(mark)
        return gra
    elif lista[2] == lista[5] == lista[8] == (' x ' or ' o '):
        gra = Victory(mark)
        return gra
    elif lista[0] == lista[4] == lista[8] == (' x ' or ' o '):
        gra = Victory(mark)
        return gra
    elif lista[6] == lista[4] == lista[2] == (' x ' or ' o '):
        gra = Victory(mark)
        return gra
    elif '   ' not in lista:
        print("DRAW!")
        gra = False
        return gra
    else:
        gra=True
        return gra



markers=[' x ', ' o ']
gra = True
lista= []
for i in range(10):
    lista.append('   ')



player1=input('Choose a name for Player 1: ')
player2=input('Choose a name for Player 2: ')
i = random.randint(0,1)
print(f'{player1} starts!') if i==0 else print(f'{player2} starts!')
if i==1:
    markers.reverse()
while gra==True:
    for mark in markers:
        print(f'\033[4m{lista[0]}|{lista[1]}|{lista[2]}')
        print(f'{lista[3]}|{lista[4]}|{lista[5]}\033[0m')
        print(f'{lista[6]}|{lista[7]}|{lista[8]}')
        d = input(f'Choose a space {player1}:') if mark==' x ' else input(f'Choose a space {player2}:')
        Choose(d,mark)
        gra = CheckForWin(lista, mark)
        if gra==False:
            break
