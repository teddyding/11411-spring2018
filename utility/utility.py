import nltk
import re

from nltk.corpus import wordnet as wn

def text2sentences(text):
    ret = list()
    # remove non-ascii characters
    text = re.sub(r'[^\x00-\x7f]',r'', text)
    for sentence in nltk.sent_tokenize(text):
        ret += re.split('\n+', sentence)
    return ret



# return all possible supersenses for a word
# return type: set
# get the lexname/supersense of the word
#
# E.G.: Input: get_word_supersenses("Tom")
# Output: set(['noun.animal', 'noun.person'])
#
# All type: ['adj.all', 'adj.pert', 'adv.all', 'noun.Tops', 'noun.act', 'noun.animal',
# 'noun.artifact', 'noun.attribute', 'noun.body', 'noun.cognition', 'noun.communication',
# 'noun.event', 'noun.feeling', 'noun.food', 'noun.group', 'noun.location', 'noun.motive',
#  'noun.object', 'noun.person', 'noun.phenomenon', 'noun.plant', 'noun.possession',
# 'noun.process', 'noun.quantity', 'noun.relation', 'noun.shape', 'noun.state',
# 'noun.substance', 'noun.time', 'verb.body', 'verb.change', 'verb.cognition',
#  'verb.communication', 'verb.competition', 'verb.consumption', 'verb.contact',
# 'verb.creation', 'verb.emotion', 'verb.motion', 'verb.perception', 'verb.possession',
# 'verb.social', 'verb.stative', 'verb.weather', 'adj.ppl']

def get_word_supersenses(w):
    synsets = wn.synsets(w)
    if len(synsets) == 0:
        return set([])
    return set([s.lexname().encode("utf-8") for s in synsets])