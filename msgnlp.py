import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

solutions = {
	'java' : 'Please visit https://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html . Recommended specification is 32bit',
	'microsoft' : 'Please visit https://www.microsoft.com/en-in/download/details.aspx?id=5555 . ',
	'browser' : 'Always use Internet Explorer and run as administrator.',
	'vendor' : 'recognized vendor',
	'tender' : 'recognized tender',
	'working' : 'Restart the browser. The version should be 11 or above. All the pop-up blog should be off and both the java should be enabled.'
}

greetings = {
	'Hello',
	'hello',
	'Hey',
	'hey',
	'Hi',
	'hi'
}

dependencies = {
	'Java',
	'java',
	'visual',
	'microsoft',
	'browser'
}

queries = {
	'not',
	'working'
}

'''vendor_list = {
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
}'''

def process(message):
	nltk.download('punkt')
	keywords = word_tokenize(message)
	print(keywords)
	for word in keywords:

		for key in greetings:
			if key == word:
				return solutions['hi']

		for key in dependencies:
			if key == word:
				return solutions[key]

		not_flag = 0 
		working_flag = 0

		for key in queries:
			if key == word:
				if key == 'not':
					not_flag = 1
				elif key == 'working' :
					working_flag = 1

		if not_flag == 1 and working_flag == 1 :
			return solutions['working']

		'''for key in vendor_list:
			if key == word:
				return solutions['vendor']

		for key in tender_list:
			if key == word:
				return solutions['tender']'''

	return "Keyword not found!"