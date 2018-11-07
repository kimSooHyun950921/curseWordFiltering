import kmeansClustering as km
import MappingWord
import sys
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from konlpy.tag import Twitter
twitter = Twitter()
def file_read():
    center_words = list()
    with open('center_words.csv','r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line=line.replace('\n','')
            center_words.append(line)
    return center_words


def test_inputs(center_words):
    length =len(center_words)
    input_words= input_read()
    smallest_input = sys.maxsize
    x_array = list()
    y_array = list()
    for input_word in input_words:
        count = 0
        for center_word in center_words:
            word = km.split_jamo(center_word)
            leven_input=km.levenshtein(word,input_word)
            result = km.get_distance(leven_input[0],leven_input[1])

            #x_array.append(leven_input[0])
            #y_array.append(leven_input[1])
            if smallest_input >result:
                smallest_input = result

        print("result",smallest_input)
            #dist = km.get_distance(leven_input[0],leven_input[1])

        #print(smallest_input)
        #print(count)
        print(count/length*100 )








def print_distance(x):
    for distance in distances:
        if distance < 3:
            return dist

def input_read():
    mapping = MappingWord.MappingWord()

    input_word = input()
    compare_word = list()

    #poss = twitter.pos(input_word,norm = True)
    poss = input_word

    result = mapping.preprocessing(input_word)
    compare_word.append(km.split_jamo(result))
    return compare_word

def main():
    center_words = file_read()
    test_inputs(center_words)
main()
