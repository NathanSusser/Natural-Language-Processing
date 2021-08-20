def build_successors_table(tokens):
	dict={}
	prev=tokens[-1]
	for i in tokens:
		if prev in dict:
			dict[prev].append(i)
		else:
			dict[prev]=[i]
		prev=i
	return dict


text = ['We', 'came', 'to', 'code', ',', 'to',
'have', 'fun', ',', 'and', 'to', 'eat', 'pie', '.']

import random

def construct_sent(word, table):
	sent=''
	word1=word
	while not word in ['.','!','?']:
		if word1==word:
			sent = sent + word
			word = random.choice(table[word])
		else:
			sent = sent + ' '+ word 
			word = random.choice(table[word])
	sent.strip()
	return sent + word

table = {'Wow': ['!'], 'Sentences': ['are'], 'are':['cool'], 'cool': ['.'], '.':['suck']}

f=open('Shakespeare.txt','r')
text=f.read()
f.close()
shakespeare_tokens=text.split()

table = build_successors_table(shakespeare_tokens)

def sent(table):
	return construct_sent('The',build_successors_table(table))

def random_sent(table):
	return construct_sent(random.choice(table),build_successors_table(table))