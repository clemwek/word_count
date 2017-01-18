# """word count"""

# # recieve the text
# # split to words and save in a list
# # loop thro the list conting and saving the out 

# def word_count(words):
# 	try:
# 		words = words.split()
# 		dic_out = {}
# 		for word in words:
# 			if word in dic_out:
# 				dic_out[word] = dic_out[word]+1
# 			else:
# 				dic_out[word] = 1
# 		return dic_out

# # print(word_count("hello there we hello we are people from planet earth!"))




wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(zip(wordlist, wordfreq)))