


class Markov(corpus):
    def __init__(self, corpus, diction):
        self.corpus = corpus
        self.diction = diction
    
    def chain(self):

        for word in corpus:
            if word in diction:
                self.diction += 1 

        for word in corpus:
            if last:
                if last in res[last]:
                    res[last][word] += 1
                else:
                    res[last][word] = 1 
            else:
                res[last] = {word: 1}
        last = word

