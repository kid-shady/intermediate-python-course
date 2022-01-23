import random
def main():
  dice_rolls=3
  dice_sums=0
  for i in range(0,dice_rolls):     
    roll=random.randint(1,6)
    dice_sums+=roll
    print(f'you rolled a {roll}')
    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll == 6:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
  print(f'you rolled a total of {dice_sums}')
if __name__== "__main__":
  main()
