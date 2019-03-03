import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

solutions = {
	'java8' : 'Please visit https://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html . Specification must be 32bit',
	'microsoft' : 'Please visit https://www.microsoft.com/en-in/download/details.aspx?id=5555 . ',
	'browser' : 'Always use Internet Explorer and run as administrator.',
	'vendor' : 'recognized vendor',
	'tender' : 'recognized tender',
	'hi' : "Greeting from BEML SRM. How may I help you?",
	'website' : 'Please visit https://bemlindia.in',
	'login' : 'Please visit https://bemlepci.bemlindia.in:50001/irj/portal. Insert correct credentials(User ID and Password)',
	'working' : 'Restart the browser. The version should be 11 or above. All the pop-up blog should be off and both the java should be enabled.'
}

greetings = {
	'hello',
	'hey',
	'hi'
}

dependencies = {
	'java8',
	'microsoft',
	'browser'
}

queries = {
	'not',
	'working',
	'website',
	'login'
}

'''vendor_list = {
	'vendor',
	'vendors'
}

tender_list = {
	'tender',
	'tenders'
}'''

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
