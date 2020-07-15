import re
import random
class Hangman:

	def __init__(self,wordlist):
		self.wordlist = wordlist
		self.attempts_remaining = 6
		self.current_letter = ''
		self.chosen_word = '' 
		self.guessed_letters = []

	def choose_word(self):
			file = open(self.wordlist)
			words = file.read().split('\n')# Read all the lines in File
			word_count = len(words)# Count the number of Word in file
			self.chosen_word = words[random.randrange(0, word_count)] # Choose Random word from file with Random
			self.word_status = ['-' for i in range(len(self.chosen_word))] # Intialize all character with '-'

	def fill_word_status(self):
		nums = random.randrange(1,3)# choose Minimum 1 char and Maximum 3 char
		for i in range(nums):
			pos = random.randrange(0,len(self.chosen_word)) # Random position
			self.word_status[pos] = self.chosen_word[pos]

	def guess_letter(self):
		letter = input("Guess the letter: ")
		
		if(letter in self.guessed_letters):
			print("Already guessed that letter !! Your guesses: {}".format(','.join(self.guessed_letters)))
			return
		self.guessed_letters.append(letter)
		occur_list = []#Store the search result
		occurance = re.finditer(letter,self.chosen_word)	

		for m in occurance:
			occur_list.append(m.start())

		if(len(occur_list) == 0): #Guess Wrong	
			self.attempts_remaining -= 1
			print("!!! Your guess was wrong. Attempts Remainig is {}".format(self.attempts_remaining))

		else:

			for pos in occur_list:
				self.word_status[pos] = self.chosen_word[pos]

			print("Correct Word")

	def get_word_status(self):
		print("Current Status : {} \n".format(''.join(self.word_status)))

					
