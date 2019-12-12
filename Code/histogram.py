import re
import random

source_text = 'one fish two fish red fish blue fish'.split(' ')


def scrubbed_words(source_text):
    with open(source_text, 'r') as file:
        words = file.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', words)
        return scrubbed_words.split()


def list_histogram(source_text):
    words = scrubbed_words(source_text)

    histogram = []

    for word in words:
        instance = [word, 0]
        print(instance)
        for word2 in words:
            if word == word2:
                instance[1] += 1
        if instance not in histogram:
            histogram.append(instance)

    return histogram


def tuple_histogram(source_text):
    histogram = list_histogram(source_text)

    tuple_histogram = []

    for item in histogram:
        tuple_histogram.append(tuple(item))

    return tuple_histogram


def diction_histogram(source_text):

    histogram = {}

    words = scrubbed_words(source_text)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1

    for key in list(histogram.keys()):
        print(key, histogram[key])


def unique_words(source_text):

    histogram = {}

    words = scrubbed_words(source_text)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1

    print(len(histogram))


def frequency(search_word, source_text):

    histogram = {}

    words = scrubbed_words(source_text)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else:
            histogram[word] = 1

    print (histogram.get(search_word, 0))

def stochastic_sampling(histogram): #random selection

    percent_histogram = {}
    # tokens = sum(histogram.values())
    # word_probs = []
    # cumulative = 0
    # for word,freq in histogram.items():
    #     word_probs.append((word, freq/tokens, cumulative))
    #     cumulative += freq/tokens

    types = len(histogram)

    pick = random.randint(1, types)

    sum = 0

    chosen_one = None

    for histo_word in histogram:
        percent = histogram[histo_word]/total
        #percent_histogram[histo_word] = percent
        sum += percent
        if pick < sum:
            chosen_one = histo_word
            return chosen_one



# diction_histogram(source_text)
# unique_words(source_text)
# frequency(source_text)
list_histogram(source_text)
move_histogram = list_histogram(source_text)
stochastic_sampling(move_histogram)
