import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from lists import solutions, queries, dependencies, greetings

def process(message):
	keywords = word_tokenize(message)
	print(keywords)

	not_flag = 0 
	working_flag = 0
	submit_flag = 0
	bid_flag = 0
	confrm_flag = 0
	status_flag = 0
	edit_flag = 0

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
				if key in solutions.keys():
					return solutions[key]
				if key == 'bid':
					bid_flag = 1
				if key == 'submit':
					submit_flag = 1
				if key == 'tenders':
					return solutions['all tenders']
				if key == 'confirmation':
					return confrm_flag = 1
				if key == 'status':
					return status_flag = 1
				if key == 'tender':
					return solutions['particular tender']
				if key == 'not':
					not_flag = 1
				if key == 'working' :
					working_flag = 1
				if key == 'edit':
					edit_flag = 1

		if not_flag == 1 and working_flag == 1 :
			return solutions['working']

		if bid_flag == 1 and submit_flag == 1:
			return solutions['submit bid']

		if bid_flag == 1 and confrm_flag == 1 and status_flag == 1:
			return solutions['confirm bid status']

		if bid_flag == 1 and edit_flag == 1:
			return solutions['edit bid']

		'''for key in vendor_list:
			if key == word:
				return solutions['vendor']

		for key in tender_list:
			if key == word:
				return solutions['tender']'''

	return "Keyword not found!"
