import random 
from termcolor import colored
from tabulate import tabulate
import guess_characters
#--------------------------

char_list = ['Master Yoda', 'Anakin Skywalker', 'Luke Skywalker', 'Obi Wan Kenobi', 'Ahsoka Tano', 'General Grevious', 'Count Dooku']

char_dict = {
	'Master Yoda': guess_characters.Master_Yoda,
	'Anakin Skywalker': guess_characters.Anakin_Skywalker,
	'Obi Wan Kenobi': guess_characters.Obi_Wan_Kenobi,
	'Luke Skywalker': guess_characters.Luke_Skywalker,
	'Ahsoka Tano': guess_characters.Ahsoka_Tano,
	'General Grievous': guess_characters.General_Grievous,
	'Count Dooku': guess_characters.Count_Dooku
}

#--------------------------
guess_word = random.choice(char_list)
attempts = 6
headers = ['Guess', 'Side', 'Lightsaber Color', 'Planet', 'Gender', 'Species', 'Master', 'Rank']
empty_list = ['Guess...', 'Guess...', 'Guess...', 'Guess...', 'Guess...', 'Guess...', 'Guess...']
table = [headers, empty_list]

print(tabulate(table, headers = 'firstrow', tablefmt = 'fancy_grid'))
print("A long time ago in a galaxy far far away there is a game called Stardle...\nGuess todays Star Wars character by using the force. You have 10 attempts.\nMay the force be with you...\n")


try:
	del table[1]

	while True:
		data = []

		if attempts > 0:
			guess = input("Please enter your guess here: ")

			if guess == guess_word:

				for i in range(8):
					data.append((colored(char_dict[guess][i], 'green')))
				
				table.append(data)
				print(tabulate(table, headers = 'firstrow', tablefmt = 'fancy_grid'))
				print("\nExecelent, young Padawan. You guessed right. It was " + guess_word + "\nCome back tomorrow and continue to your train.")
				break

			elif guess != guess_word:

				for i in range(8):
					if char_dict[guess][i] == char_dict[guess_word][i]:
						data.append((colored(char_dict[guess][i], 'green')))

					elif char_dict[guess][i] != char_dict[guess_word][i]:

						if (char_dict[guess][i] in char_dict[guess_word][i]) or (char_dict[guess_word][i] in char_dict[guess][i]):
							data.append((colored(char_dict[guess][i], 'yellow')))

						elif (char_dict[guess][i] not in char_dict[guess_word][i]) or (char_dict[guess_word][i] not in char_dict[guess][i]):
							data.append((colored(char_dict[guess][i], 'red')))

				attempts -= 1
				table.append(data)
				print(tabulate(table, headers = 'firstrow', tablefmt = 'fancy_grid'))
				print('You have ' + str(attempts) + ' attempt(s) left.')
				continue

		elif attempts == 0:
			print("It's " + guess_word + ".\nYou are not strong enuogh to be a jedi master.")
			break

except KeyboardInterrupt:	
	print('\nYou give up soon young padawan...')



