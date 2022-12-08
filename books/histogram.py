t = {'a': 2, 'b': 3}

from fractions import Fraction

import random

def histogram1(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d


h = histogram1(t)
def choose_from_hist(hist):
    values = []
    for key, value in hist.items():
        for i in range(value):
            values.append(key)
    return random.choice(values)

import string





def process_file(filename):
    hist = dict()
    fp = open(filename, encoding='latin-1')
    for line in fp:
        words = line.split()
        for word in words:
            word = word.replace('-', ' ')
            word = word.lower().strip(string.punctuation + string.whitespace + '.,')
            hist[word] = hist.get(word, 0) + 1   
    return hist



def total_words(hist):
    return sum(hist.values())
# print(total_words(hist))

def different_words(hist):
    return len(hist)

# print(different_words(hist))

def most_common_words(hist, number = 10):
    t = []
    for word, freq in hist.items():
        t.append((freq, word))
    t.sort(reverse=True)
    
    return t[:number]



def print_mcw(mcw):
    for freq, word in mcw:
        print(word, freq, sep='\t')


# print(choose_from_hist(t))
# hist = process_file('emma.txt')
# mcw = most_common_words(hist)
#
# print('Total number of words: ', total_words(hist))
# print('Number of different words: ', different_words(hist))
# print('\nMost common words: ')
# print_mcw(mcw)



