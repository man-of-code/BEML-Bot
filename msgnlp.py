import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

solutions = {
	'vendor' : 'recognized vendor',
	'tender' : 'recognized tender',
}

greetings = {
	'Hello',
	'hello',
	'Hey',
	'hey'
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
	nltk.download('punkt')
	keywords = word_tokenize(message)
	print(keywords)
	for word in keywords:
		for key in greetings:
			if key == word:
				return "Greeting from BEML SRM. How may I help you?"
		for key in vendor_list:
			if key == word:
				return solutions['vendor']
		for key in tender_list:
			if key == word:
				return solutions['tender']
	return "Keyword not found!"