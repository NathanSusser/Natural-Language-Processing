def get_kgram(text, position, k):
	new_text = ''
	for i in (range(position, position + k)):
		new_text = new_text +text[i]
	return new_text

def process_character(m, text, position, k):
	word = get_kgram(text, position, k)
	if word in m:
		let = m[word]
		if {text[position+k]:1}== let or text[position+k] in let:
			m[word][text[position+k]] += 1
		else:
			m[word].update({text[position+k]:1})
	else:
		m[word] = {text[position+k]:1}
	return m


'''
	if k + position > len(text):
		word = get_kgram(text, (position-len(text)), k)
		m[word] = {text[((position+k)-len(text))]:1}
	else:
'''


def build_markov_model(text,k):
	markov_model={}
	for i in range(len(text)-k):
		process_character(markov_model, text, i, k)
	return markov_model

def next_character_frequency(m, kgram, c):
	if c in m[kgram]:
		return (m[kgram][c])
	else:
		return (0)

test = build_markov_model('the theremin in the basement is the theologian’s theft detection device.',3)


import random

def random_character(m, kgram):
	lst = []
	for i in m[kgram].keys():
		for a in range(m[kgram][i]):
			 lst.append([i])
	return random.choice(lst)[0]

def generate_random_text(text, k, n):
	model = build_markov_model(text,k)
	sent = get_kgram(text, random.choice(range(len(text)-k)),k)
	for i in range(n):
		word = get_kgram(sent, i, k)
		new_let = random_character(model, word)
		sent+=new_let
	return sent


f = open('moby_dick.txt', 'r')
text = f.read()
f.close()
moby = text

f = open('Shakespeare.txt', 'r')
text = f.read()
f.close()
Shakespeare = text


f = open('Nathan.txt', 'r')
text = f.read()
f.close()
nathan = text


