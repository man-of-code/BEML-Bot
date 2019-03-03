import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

solutions = {
	'vendor' : 'recognized vendor',
	'tender' : 'recognized tender',
}

vendor_list = {
	'vendor',
	'Vendor',
	'vendors',
	'Vendors'
}

tender_list = {
	'tender',
	'Tender',
	'tenders',
	'Tenders'
}

def process(message):
	keywords = word_tokenize(message)
	print(keywords)
	for word in keywords:
		for key in vendor_list:
			if key == word:
				return solutions['vendor']
		for key in tender_list:
			if key == word:
				return solution['tender']
	return "Keyword not found!"