import random

word = random.choice(["apple", "banana", "cherry", "date", "fig", "grape"]).lower()
word_len = len(word)
display_word = ""
guesses = 7
is_running = True
print(word)

for dash in range(word_len):
	print("_", end = "",)
print("")

while is_running:
	letter = input("guess a letter: ").lower().strip()
while guesses > 0 :

	if letter in word:
		print(f"the letter '{letter}' is in the word.{display_word}")
		
	else:
		print(f"the letter '{letter}' is not in the word.{display_word}")
		guesses -= 1
		print(f"you have {guesses} left ")
print("Sorry !!! You Used Your All Guesses ")