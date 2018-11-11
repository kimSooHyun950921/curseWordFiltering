import levenshtein as km
import mapping_word
import sys
import numpy     as np
import math
from sklearn.metrics.pairwise import cosine_similarity

from konlpy.tag import Twitter
twitter = Twitter()


def file_read():
    center_words = list()
    with open('./csv_file/offensive_word_db.csv', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line=line.replace('\n','')
            center_words.append(line)
    return center_words
def get_distance(x,y):
    return math.sqrt(x*x + y*y)

def test_inputs(center_words):
    length =len(center_words)
    input_words= input_read()
    print(input_words)
    smallest_input = sys.maxsize
    smallest_word = ''
    x_array = list()
    i = 0
    y_array = list()
    for center_word in center_words:
        leven_input=km.levenshteins(center_word,input_words)
        result = get_distance(leven_input[0],leven_input[1])

            #x_array.append(leven_input[0])
            #y_array.append(leven_input[1])
        if smallest_input >result:
            smallest_input = result
            smallest_word = center_word
            #print(smallest_word,i)
        i+=1
    print("result",smallest_input,smallest_word)
            #dist = km.get_distance(leven_input[0],leven_input[1])

        #print(smallest_input)
        #print(count)
        #print(count/length*100 )








def print_distance(x):
    for distance in distances:
        if distance < 3:
            return dist

def input_read():
    mapping = mapping_word.mapping_word()

    input_word = input()
    compare_word = list()

    #poss = twitter.pos(input_word,norm = True)

    result = mapping.preprocessing(input_word)
    result = mapping.multi_eumso_to_single_eumso(result)
    return result

def main():
    mapping = mapping_word.mapping_word()

    center_words = file_read()
    result = list()
    for word in center_words:
        word = mapping.preprocessing(word)
        word = mapping.multi_eumso_to_single_eumso(word)
        result.append(word)


    test_inputs(result[:-2])
main()
