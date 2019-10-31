import random, sys

def random_order(words):
    if words:
        print(words)
        new_array = []
        for index in range(len(words)-1): # we remove word from words
            for word in words:
                rnd = random.choice(words) #random word from list
                new_array.append(rnd) # add that word to a new array
                words.remove(rnd) # remove word from original list
        print(new_array)
    else:
        return print("add 4 arguments")

if __name__ == '__main__':
    words = sys.argv[1:]
    random_order(words)
