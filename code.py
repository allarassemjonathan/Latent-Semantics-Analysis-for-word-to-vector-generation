stop_words =  """
    a about above across after afterwards again against all almost alone along
    already also although always am among amongst amount an and another any anyhow
    anyone anything anyway anywhere are around as at b c d e f g h i j k l m n o p q r s t u v w x y z
    back be became because become becomes becoming been before beforehand behind
    being below beside besides between beyond both bottom but by
    call can cannot ca could
    did do does doing done down due during
    each eight either eleven else elsewhere empty enough even ever every
    everyone everything everywhere except
    few fifteen fifty first five for former formerly forty four from front full
    further
    get give go
    had has have he hence her here hereafter hereby herein hereupon hers herself
    him himself his how however hundred
    i if in indeed into is it its itself
    keep
    last latter latterly least less
    just
    made make many may me meanwhile might mine more moreover most mostly move much
    must my myself
    name namely neither never nevertheless next nine no nobody none noone nor not
    nothing now nowhere
    of off often on once one only onto or other others otherwise our ours ourselves
    out over own
    part per perhaps please put
    quite BOOK \n
    rather re really regarding
    same say says said see seem seemed seeming seems serious several she should show side
    since six sixty so some somehow someone something sometime sometimes somewhere
    still such
    take ten than that the their them themselves then thence there thereafter
    thereby therefore therein thereupon these they third this those though three
    through throughout thru thus to the together too top toward towards twelve twenty
    two
    under until up unless upon us used using
    various very very via was we well were what whatever when whence whenever where
    whereafter whereas whereby wherein whereupon wherever whether which while
    whither who whoever whole whom whose why will with within without would
    yet you your yours yourself yourselves"""

def set_vocabulary(filename):
    text = open(filename, 'r', encoding="utf-8").read().lower()
    punc = '''±¬¤¸£×¥¿*¶¼¦¹¯§¾´ª½¢¡®…³=²º­¨0123456789!→°()-[]{};:'"«»\,+<>./?@#$%^&*_~©'''
    for x in text:
        if x in punc:
            text = text.replace(x,' ')
    arr = text.split(' ')
    keys = [word for word in arr if not word in stop_words]
    for word in keys:
        if '\n' in word:
            ar = word.split('\n')
            keys.remove(word)
            keys.extend(ar)
    keys_u ={'\head'}
    f = open("vocabulary_" + filename, 'w', encoding='utf-8')
    for el in keys:
        el = el.strip()
        keys_u.add(el)
        f.write(el + '\n')
    f.close()
    return keys_u

def clean_vocabulary(filename):
    f = open("vocabulary_" + filename, 'r', encoding="utf-8")
    text = f.read().lower()
    f.close()
    arr = text.split('\n')
    keys_u = {'\head'}
    for el in arr:
        keys_u.add(el)
    f = open("vocabulary_" + filename, 'w', encoding="utf-8")
    for el in keys_u:
        f.write(el+'\n')
    f.close()
    
def load_vocabulary(filename):
    f = open("vocabulary_" + filename, 'r', encoding="utf-8").read().lower()
    vocab = {'\head'}
    for el in f.split('\n'):
        vocab.add(el)
    return vocab

def generate_vocab(filename):
    set_vocabulary(filename)
    clean_vocabulary(filename)
    return load_vocabulary(filename)

def matrix(vocabulary):
    dic = {'\head':{'\head':0}}
    sentences = open(filename, 'r', encoding="utf-8").readlines()
    for sentence in sentences:
        arr = sentence.split(' ')
        for word in vocabulary:
            if word in arr:
                for el in arr:
                    if el in dic.keys():
                        dic[word][el] = dic[word][el]+1
                    else:
                        dic[word][el] = 1

    return dic
    
    
    
s = generate_vocab("Odyssey.txt")
print(len(s))

