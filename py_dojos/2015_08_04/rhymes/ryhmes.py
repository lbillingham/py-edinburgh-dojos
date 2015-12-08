# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:10:42 2015

@author: laurence
"""
import nltk
from nltk.parse.generate import generate
from numpy.random import choice

def get_rhymes(inp, n_phonemes):
     entries = nltk.corpus.cmudict.entries()
     syllables = [(word, syl) for word, syl in entries if word == inp]
     rhymes = []
     for (word, syllable) in syllables:
             rhymes += [word for word, pron in entries if pron[-n_phonemes:] == syllable[-n_phonemes:]]
     return set(rhymes)
     

def main():
    zen = """ Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""
        
    tagged = nltk.pos_tag(nltk.word_tokenize(zen))
    tagged = [(tag, word) for word, tag in tagged]
    #
    #tag_word_map = defaultdict(list)
    #[(tag, word) for word, tag in tagged]
    tags = set([tag for tag, _  in tagged])
    tag_word_map = {tag: {word for key, word in tagged if key == tag} for tag in tags}
                
           
    gram_head = """
      S -> NNP VBZ JJR IN RB
    """
    cats = ['NNP', 'VBZ', 'JJR', 'IN', 'RB']
    gram = [cat + ' -> ' + '|'.join([repr(x) for x in tag_word_map[cat]]) for cat in cats]
    
    grammar = gram_head + '\n'.join(gram)
    grammar = nltk.CFG.fromstring(grammar)
    
    poem = []    
    for sentence2 in generate(grammar, depth=5):
        poem.append(' '.join(sentence2))
        
    out =  "\n".join(choice(poem, size=10))
    print(out)


if '__main__' == __name__:
    main()