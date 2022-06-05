corpus = open('story1.txt', encoding='utf-8').read()
corpus = corpus.replace('\n', ' ')
li = []
sentences = corpus.split('.')
for sentence in sentences:
    sentence = sentence.strip()
    if len(sentence)>0:
        li.append(sentence[0])

for el in li:
    if el in 'ABCDEFGHIJKLMNOP\'“”]':
        li.remove(el)

print(li)


