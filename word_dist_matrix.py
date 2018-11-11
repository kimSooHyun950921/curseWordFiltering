import levenshtein
import eumjel_levenshtein
import math
def get_distance(x,y):
    return math.sqrt(x*x + y*y)

def get_levenshtein(word_list,leven_kind,leven,debug=True):
    if debug:
        print("거리 행렬 만들기")
    add_for_graph_x = list()
    add_for_grapy_y = list()

    add_matrix = list()
    i = 0
    n = 0
    while i < len(word_list):
        row_list = list()
        j=0
        while j < len(word_list):
            leven_result = leven.levenshteins(word_list[i],word_list[j])
            if leven_kind == 'leven':
                if debug:
                    print("x ",leven_result[0],"y ",leven_result[1])
                leven_result = get_distance(leven_result[0],leven_result[1])
            row_list.append(leven_result)
            if debug:
                print("word",word_list[i],word_list[j],leven_result)
            j+=1
        add_matrix.append(row_list)
        i+=1
    return add_matrix
    #return[(add_for_graph_x,add_for_grapy_y,add_tag),(
def is_which_leven(leven_result):
    try:
        i = leven_result[0]
        j = leven_result[1]
        return 'leven'
    except IndexError:
        return 'eumjel'


def make_matrix_for_clustering(word_list,leven_kind):
    if leven_kind == 'leven':
        return get_levenshtein(word_list,leven_kind,levenshtein)
    elif leven_kind == 'jamo':
        return get_levenshtein(word_list,leven_kind,eumjel_levenshtein)
