import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from lists import solutions, queries, dependencies, greetings

def process(message):
	keywords = word_tokenize(message)
	print(keywords)

	not_flag = 0 
	working_flag = 0

	for word in keywords:
		word = word.lower()

		for key in greetings:
			if key == word:
				return solutions['hi']

		for key in dependencies:
			if key == word:
				return solutions[key]

		for key in queries:
			if key == word:
				if key == 'not':
					not_flag = 1
				if key == 'working' :
					working_flag = 1
				else :
					return solutions[key]

		if not_flag == 1 and working_flag == 1 :
			return solutions['working']

		'''for key in vendor_list:
			if key == word:
				return solutions['vendor']

		for key in tender_list:
			if key == word:
				return solutions['tender']'''

	return "Keyword not found!"
