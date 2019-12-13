from random import choice
from pprint import pprint
from dictogram import Dictogram


class Markov:
    def __init__(self, corpus):
        self.corpus = corpus
        self.states = {}
        self.chain()

    def chain(self):
        last_word = None
        # Loop over all words in the corpus
        for word in self.corpus:
            # Skip the first iteration if we don't have a last_word
            if last_word is not None:
                # If we haven't seen last_word before
                if last_word not in self.states:
                    # Create a new empty histogram object as value
                    self.states[last_word] = Dictogram()
                # Add a count for the next word after last_word
                self.states[last_word].add_count(word)
            # Keep track of this word for the next iteration
            last_word = word
    
    def __str__(self):
        return str(self.states)

def random_walk(words, markov):
    """Use a random word from the states to "walk" around the markov chain to create a sentence"""
    sentence = [] # add all of the words to this list to create a sentence
    random_key = [key for key in markov.keys()]
    # print(random_key)

    i = 0
    while i < 5:
        output = choice(random_key)
        # psrint(output)
        sentence.append(output)
        i += 1

    return " ".join(sentence)

def second_order_markov(words):
    states ={}

    for i in range(len(words) -2):
        first_word = words[i]
        second_word = words[i +1]
        # pairs = (first_word, second_word)
        # print(pairs)
        third_word = words[i + 2]
        # states[first_word] = marcov_dict
        if first_word not in states.keys():
            histo = []
            states[(first_word, second_word)] = histo
            
            
        states[(first_word, second_word)].append(third_word)
         
    values = states.items()
    for key, value in values:
        # markov_dict = {}  # can't use a regular dict
        states[key] = Dictogram(value)  # to use a dictogram method (add_count), we must first establish a Dictogram() object
        # markov_dict.add_count(second_word)
        # print(markov_dict)
    return states
    # print(states)



if __name__ == '__main__':
    corpus = ("one fish two fish red fish blue fish").split(' ')

    markov_instance = Markov(corpus)
    pprint(markov_instance.states)