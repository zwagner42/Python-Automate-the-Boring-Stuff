#! python3
# madLibs.py - Reades sentenceStructure.txt files and fills in the keywords (ADJECTIVE, ADVERB, NOUN, VERB)

#Function to replace keywords with the user's choice
def replace_Keywords(sentence):
	newSentence = []
	for word in sentence:
		if(word == "ADJECTIVE" or word == "ADJECTIVE."):
			newSentence.append(input('Enter an adjective:\n'))
		elif(word == "ADVERB" or word == "ADVERB."):
			newSentence.append(input('Enter an adverb:\n'))
		elif(word == "NOUN" or word == "NOUN."):
			newSentence.append(input('Enter a noun:\n'))
		elif(word == "VERB" or word == "VERB."):
			newSentence.append(input('Enter a verb:\n'))
		else:
			newSentence.append(word)
			
	return newSentence

#Open the sentence to be read
sentenceFile = open('sentenceStructure.txt', 'r')
sentence = (sentenceFile.read()).split(' ')

#Replace the keywords and print the new sentence
sentence = replace_Keywords(sentence)
print(' '.join(sentence))

#Write the new sentence to the reconstructedSentece.txt file
writeFile = open('reconstructedSentence.txt', 'w')
writeFile.write(' '.join(sentence))

#Close all files
writeFile.close()
sentenceFile.close()