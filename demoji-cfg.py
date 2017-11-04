from nltk.parse.generate import generate
from nltk import CFG

grammar = """ 
S -> NP VP 
NP -> Det AP 
Det -> 'The' 
AP -> ADJ N 
ADJ -> 'sad' 
N -> 'dog' 
VP -> V ADV 
V -> 'ran'
ADV -> 'sadly'
"""


for sentence in generate(CFG.fromstring(grammar), n=100): 
    print(' '.join(sentence)) 
