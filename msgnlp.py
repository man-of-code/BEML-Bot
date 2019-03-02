import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

#1
vendor_list = {
	"Processed vendor"
	"vendors",
	"vendor"
}

def process(message):
	nltk.download('punkt')
	keywords = word_tokenize(message)
	print(keywords)
	for word in keywords:
		for key in vendor_list:
			if key == word:
				return key
	return "Keyword not found!"