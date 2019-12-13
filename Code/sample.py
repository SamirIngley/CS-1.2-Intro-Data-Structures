import sys
import random
import operator
from random import randint
from clean import clean
from histogram import dic_histogram, dic_histogram_test, list_histogram

# Declare the source of knowledge
#source_text = sys.argv[1]
source_text = 'fish.txt'

# Clean up the source of knowledge
raw_corpus = clean(source_text)

# Reformat the source of knowledge into a list histogram
corpus = list_histogram(source_text)

# Declare the length of the source of knowledge
total = len(raw_corpus)

# Declare the storage for results when you run run_test()
result = []

# Function for regular use; will return one word
def run():
    # Generate our 'dart'
    lucky_number = randint(1,total)

    # Declare the counter we use to sum up to lucky_number
    counter = 0

    # The setup for when iterating over the list corpus
    index = 0

    # While True, sum the counter with the values in the corpus histogram
    while len(corpus) > 0:
        counter += corpus[index][1]

        # When the counter is hit, declare the lucky number at that point
        if counter >= lucky_number:
            lucky_word = (corpus[index][0])
            break
        
        # If counter not hit, keep adding to the index by 1
        else:
            index += 1

    # Return the lucky number
    return(lucky_word)


# The test function
def run_test():
    lucky_number = randint(1,total)
    counter = 0
    index = 0
    while len(corpus) > 0:
        counter += corpus[index][1]

        if counter >= lucky_number:
            lucky_word = (corpus[index][0])
            break

        else:
            index += 1

    result.append(lucky_word)

    counter = 0
    index = 0


#for _ in range(100):
#    run_test()

#s = ' '.join(result).split()

#dic_histogram_test(s)
run()