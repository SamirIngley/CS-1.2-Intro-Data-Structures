import random, sys

def random_order(word_list):
    if word_list:
        new_array = []
        for index in word_list:
            rnd = random.choice(word_list) #random word from list
            new_array.append(rnd) # add that word to a new array
            word_list.remove(word_list(rnd)) # remove word from original list
        return print(new_array)
    else:
        print("add 4 arguments")

if __name__ == '__main__':
    words = sys.argv[1:]
    random_order(words)
