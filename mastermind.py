# ----------------------------
# Mastermind
# Aaron and Jordan
# 12/6/14 Project started and mostly finished
# 1/19/15 Finished and cleaned up
# ----------------------------

import random

guesses = 7
current = ["*","*","*","*"]

# ----------------------------
#  Mastermind
# ----------------------------
# Input:  Int, the # of guesses left to the user
# Output: void, prints string telling user whether they
#         won or lost

def mastermind(guesses):
	nums = ["first", "second", "third", "fourth"]
	guess = None
	isSolved = False
	
	# generates a random list of four numbers
	daCode = [random.randint(0,9) for x in range(4)]
	
	while not isSolved and guesses > 0:
		
		# getting input from the user
		print ''.join(current)
		userInput = raw_input("Give your guess! ")
		while not(len(userInput)<5):
			print "Please only enter four numbers!" + "\n"
			userInput = raw_input("Give your guess! ")
		guess = str(userInput)
		guess = [int(i) for i in str(userInput).strip(",")]

		# check to see if the guess was correct
		if guess == daCode:
			return "~~~~~~~~~~\n YOU WON!\n~~~~~~~~~~"
		
		# checking to see if the guess has any matching numbers
		for i in range(len(guess)):
			if guess[i] in daCode:
				if guess[i] == daCode[i]:
					print "The " + str(nums[i]) + " number is CORRECT."
					current[i] = str(guess[i])
				elif guess[i] in daCode and not(str(guess[i]) in current):
					print "The  " + str(nums[i]) + " number is in the wrong position"
				else:
					print "The " + str(nums[i]) + " number is WRONG"
			else:
				print "The " + str(nums[i]) + " number is WRONG."
		guesses -= 1
		print "You have " + str(guesses) + " guesses left!" + "\n"
		
	return "YOU LOST! The correct answer: " + str(int(''.join(map(str,daCode))))
    
print mastermind(guesses)
