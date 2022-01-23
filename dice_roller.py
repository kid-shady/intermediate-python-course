import random
def main():
  dice_rolls=int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  dice_sums=0
  for i in range(0,dice_rolls):     
    roll=random.randint(1,dice_size)
    dice_sums+=roll
    print(f'you rolled a {roll}')
    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll == dice_size:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
  print(f'you rolled a total of {dice_sums}')
if __name__== "__main__":
  main()
