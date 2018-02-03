# Make a two-player Rock-Paper-Scissors game.
# * Rock beats scissors
# * Scissors beats paper
# * Paper beats rock
print(""
      "Please pick one of the following for each player : "
      "> rock"
      "> paper"
      "> scissors"
      "")
while True:
    game = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    if (player_a not in game or player_b not in game):
        print("Please enter valid values!")
        print('')
        continue
    a = game.get(player_a)
    b = game.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins the game.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            print('')
            continue
        else:
            print('game over.')
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                print('')
                continue
            else:
                break
    elif dif in [-2, 1]:
        print('player b wins the game.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            print('')
            continue
        else:
            print('game over.')
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                print('')
                continue
            else:
                break
    else:
        print('Draw.Please continue.')
        print('')