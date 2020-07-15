import hangmanCreator

hangman = hangmanCreator.Hangman("/home/sp/udemy_PY/hangman/listof_words.txt")
hangman.choose_word()
hangman.fill_word_status()

while True:
	hangman.get_word_status()
	hangman.guess_letter()

	if(hangman.attempts_remaining == 0):
		print("Out of Attempts.The word was {}.Game over".format(hangman.chosen_word))
		break

	elif(hangman.chosen_word == ''.join(hangman.word_status)):
		print("Wow! You won the game")
		break

