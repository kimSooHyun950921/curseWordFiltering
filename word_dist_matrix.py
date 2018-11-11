#import levenshtein as l_leven
import eumjel_levenshtein as leven

def get_distance(x,y):
    return math.sqrt(x*x + y*y)

def get_levenshtein(word_list,leven_kind,debug=True):
    add_for_graph_x = list()
    add_for_grapy_y = list()

    add_matrix = list()
    i = 0
    n = 0
    while i < len(word_list):
        center_word = word_list[i]
        row_list = list()
        while j < len(word_list):
            compare_word = word_list[j]
            leven_result = leven.levenshteins(center_word,compare_word)
            if leven_kind == 'leven':
                leven_result = get_distance(leven_result[0],leven_result[1])
            row_list.append(leven_result)
        add_matrix.append(row_list)









            if debug:
                print("거리 행렬 만들기")
                print("word",word_list[i],leven_result)

        print(leven_result)
        if leven_result[0] !=0 and leven_result!=0:
            add_for_graph_x.append(leven_result[0])
            add_for_grapy_y.append(leven_result[1])
            add_tag.append(word_list[i])
            j+=1
        i+=1
    return (add_for_graph_x,add_for_grapy_y)
    #return[(add_for_graph_x,add_for_grapy_y,add_tag),(
def is_which_leven(leven_result):
    try:
        i = leven_result[0]
        j = leven_result[1]
        return 'leven'
    except IndexError:
        return 'eumjel'


def make_matrix_for_clustering():
    matrix = list()



def make_matrix_for_clustering():
