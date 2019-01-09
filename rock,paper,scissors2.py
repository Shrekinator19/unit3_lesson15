import random

guess1 = input('Pick from 1, 2, or 3.')
guess1 = int(guess1)
guess2 = input('Pick again from 1, 2, or 3.')
guess2 = int(guess2)

pick1 = random.randint(1,3)
pick2 = random.randint(1,3)

print('Your guesses were ' + str(guess1) + ' and ' + str(guess2) + '.')
print('Your picks were ' + str(pick1) + ' and ' + str(pick2) + '.')

if guess1 == pick1 and guess2 == pick2:
	print('You win Rock, Paper, Scissors!')

elif guess2 == pick1 and guess1 == pick2:
	print('You are still a winner!')

else:
	print('You lose Rock, Paper, Scissors! Try again.')