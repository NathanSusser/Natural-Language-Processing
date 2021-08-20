
classes = ['Physics', 'Computer Science', 'Infinity', 'Sculpture']

boring = ['the', 'and', 'a', 'is']

sentence = 'my name is jeff jeff is.'

f = open('beatles.txt', 'r')
text = f.read()
f.close()
beatles = text
beatles_tokens = text.split()

f = open('jay_z_lyrics.txt', 'r')
text = f.read()
f.close()
jay_z = text
jay_z_tokens = text.split()

f = open('Shakespeare.txt', 'r')
text = f.read()
f.close()
Shakespeare = text
Shakespeare_tokens = text.split()

f = open('moby_dick.txt', 'r')
text = f.read()
f.close()
moby = text
moby_tokens = text.split()

f = open('i_have_a_dream.txt', 'r')
text = f.read()
f.close()
MLK = text
MLK_tokens = text.split()

f = open('democratic_debate_2015.txt', 'r')
text = f.read()
f.close()
dem = text
dem_tokens = text.split()

f = open('republican_debate_2015.txt', 'r')
text = f.read()
f.close()
rep = text
rep_tokens = text.split()



def taken(classes):
	d = []
	for i in classes:
		question = ''.join(['have you taken ',i ])
		take=input(question)
		if take == 'yes':
			d.append([i])
			question = 'have you taken'
		else:
			question = 'have you taken'
	return d


def read_file(file):
	f = open(file, 'r')
	text = f.read()
	f.close()
	return text.split()

import functools

def count_words(sent):
	dict={}
	for word in sent.split( ):
		word = remove_punctuation(word)
		if word in dict:
			dict[word] += 1
		else:
			dict[word]=1
	return dict

def remove_punctuation(str):
	return (''.join([x for x in str if x not in ['.','!','?',',',';',':','/','-','(',')']]))

def top_n_words(text, n):
	count = count_words(text)
	return sorted(count, key = count.get, reverse = True)[0:n]

def top_n_words_except(text, n, boring):
	lst = text.split( )
	sent = [a for a in lst if remove_punctuation(a) not in boring]
	new_sent = ' '.join(sent)
	return top_n_words(new_sent, n)

#needs dictionary

def average_word_length(dict):
	total_letters = sum([len(a)*dict[a] for a in dict.keys()])
	print (total_letters)
	total_words = sum(dict.values())
	print (total_words)
	return total_letters/total_words

#needs tokens
def average_word_length_except(text, boring):
	sent = ' '.join([a for a in text if remove_punctuation(a) not in boring])
	return average_word_length(count_words(sent))

#needs text

def word_diversity(text):
	counts = count_words(text)
	diverse = len(counts)
	print (diverse)
	total = sum(counts.values())
	print (total)
	return diverse/total

#needs text

def word_diversity_except(text, boring):
	sent = ' '.join([a for a in text if remove_punctuation(a) not in boring])
	return word_diversity(sent)



#words_not_boring = ' '.join(top_n_words_except(beatles, len(beatles_tokens), boring))

#print (words_not_boring)


#print (average_word_length(count_words(words_not_boring)))




#print (average_word_length(count_words(' '.join(top_n_words_except(jay_z, len(jay_z_tokens), boring)))))



