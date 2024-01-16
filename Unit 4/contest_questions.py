def tournament_select():
    games_won = 0
    for i in range(0, 6):
        question = input()
        if question == 'W':
            games_won += 1
        
    
    if games_won == 5 or games_won == 6:
        return '1'
    elif games_won == 3 or games_won == 4:
        return '2'
    elif games_won == 1 or games_won == 2:
        return '3'
    else:
        return '-1'

#print(tournament_select())

def magic_square():
    i1 = int(input())
    i2 = int(input())
    i3 = int(input())
    i4 = int(input())
    

