def break_words(stuff):
	"""This function will break up words for us"""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words"""
	return sorted(words)
	
def print_first_word(words):
	"""Prints the first word after popping it off"""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off"""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sortes words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

phrases = break_words('Hello world')
print phrases

phrases_sort = sort_words(phrases)
print phrases_sort
print phrases
print_first_word(phrases)
print phrases
print_last_word(phrases)
print phrases
phrase2 = sort_sentence('Good morning Vietnam')
print phrase2
print_first_and_last('Good morning Vietnam')
print_first_and_last_sorted('Good morning Vietnam')
