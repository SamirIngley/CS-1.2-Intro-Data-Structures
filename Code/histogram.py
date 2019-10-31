import re
import random

source_text = 'source.txt'

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

    total = len(histogram)

    pick = random.randint(1, total)

    sum = 0

    for histo_word in histogram:
        percent = histo_word[occurance]/total
        percent_histogram[histo_word] = percent
        sum += percent
        if pick l








diction_histogram(source_text)
unique_words(source_text)
frequency(source_text)
