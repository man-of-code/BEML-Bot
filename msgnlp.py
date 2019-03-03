import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from lists import solutions, queries, dependencies, greetings

def process(message):
	keywords = word_tokenize(message)

	not_flag = 0 
	working_flag = 0
	submit_flag = 0
	bid_flag = 0
	confrm_flag = 0
	status_flag = 0
	edit_flag = 0
	one_flag = 0
	two_flag = 0

	for word in keywords:
		word = word.lower() #convert to lowercase

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
				if key == 'webpage' or key == 'website':
					return solutions['website']
				if key == 'tenders':
					return solutions['all tenders']
				if key == 'tender':
					return solutions['particular tender']
				if key == 'bid' or key == 'bidding':
					bid_flag = 1
				if key == 'submit' or key == 'submitted' or key == 'submitting':
					submit_flag = 1
				if key == 'confirmation' or key == 'confirm' or key == 'confirmed':
					confrm_flag = 1
				if key == 'status':
					status_flag = 1
				if key == 'not':
					not_flag = 1
				if key == 'working' or key == 'worked' or key == 'work':
					working_flag = 1
				if key == 'edit' or key == 'change':
					edit_flag = 1
				if key == '1' or key == 'one' or key == 'single':
					one_flag = 1
				if key == '2' or key == 'two' or key == 'double':
					two_flag = 2

		if not_flag == 1 and working_flag == 1 :
			return solutions['working']

		if bid_flag == 1 and submit_flag == 1:
			return solutions['submit bid']

		if bid_flag == 1 and confrm_flag == 1 and status_flag == 1:
			return solutions['confirm bid status']

		if bid_flag == 1 and one_flag == 1:
			return solutions['1 stage bid']

		if bid_flag == 1 and two_flag == 2:
			return solutions['2 stage bid']

		if bid_flag == 1 and edit_flag == 1:
			return solutions['edit bid']

		'''for key in vendor_list:
			if key == word:
				return solutions['vendor']

		for key in tender_list:
			if key == word:
				return solutions['tender']'''

	return "Keyword not found!"
