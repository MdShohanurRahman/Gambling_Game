import random
import time

head_tail = ['H', 'H', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'T']
count, heads, tails, game_no = 0,0,0,1

while(True):
  
  flip = random.choice(head_tail)

  if flip == 'H':
    heads += 1
  else:
    tails += 1
  
  diff = abs(heads-tails)
  balance = abs(count-8)
  
  time.sleep(1)
  print(f'Flip_no {count:2d} ==> {flip:2}   Head {heads:2}   Tail {tails:2}   Difference {diff}')
  
  if diff == 3:
    time.sleep(2)
    print(f'\nGame {game_no} Result : ')
    time.sleep(1)
    print(f'You win {balance} tk\n\n') if count < 8 else print(f'You lose {balance} tk\n\n')
    time.sleep(2)
    user_input = input('If you want to play this game again ? y/n \n').strip().casefold()
    
    if user_input == 'y':
      count,heads,tails = 0,0,0
      random.shuffle(head_tail)
      game_no += 1
    else:
      print('\nThanks for playing\n')
      break
  
  count += 1

  
