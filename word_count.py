"""word count"""

# recieve the text
# split to words and save in a list
# loop thro the list conting and saving the out 

def words(words):
	try:
		words = words.split()
		dic_out = {}
		for word in words:
			if word in dic_out:
				dic_out[word] = dic_out[word]+1
			else:
				dic_out[word] = 1
		return dic_out
	except Exception:
		return 'invalid'

# print(word_count("hello there we hello we are people from planet earth!"))