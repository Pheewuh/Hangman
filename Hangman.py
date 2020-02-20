hangman=[' ','---------','    ¦   ','    O    ','   /¦/   ','    ¦    ','   /¦/   ']
word=list(input('Input your word:'))
worddupe=word[::1]
mistakes=1
displayword=[]

for i in word:
	if i in 'aeiou':
		displayword.append('_')
	else:
		displayword.append('-')
		
def guessing():
	print(displayword)
	global mistakes
	global correctonce
	guess=input('Guess:')
	def guesswork():
		global mistakes
		global correctonce
		global falseonce
		if guess in word:
			print('Correct')
			displayword[word.index(guess)]=guess
			word[word.index(guess)]=0
			del worddupe[0]
			correctonce=True
		elif guess not in word and correctonce==False and falseonce==False:
			mistakes+=1
			print('Wrong')
			for i in range(mistakes):
				print(hangman[i]+'\n')
			falseonce=True	
	[guesswork() for i in range(100)]
	
while mistakes<7 and len(worddupe)>0:
	guessing()
	correctonce=False
	falseonce=False
