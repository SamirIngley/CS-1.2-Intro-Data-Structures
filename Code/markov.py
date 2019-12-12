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


if __name__ == '__main__':
    corpus = ("one fish two fish red fish blue fish").split(' ')

    markov_instance = Markov(corpus)
    pprint(markov_instance.states)