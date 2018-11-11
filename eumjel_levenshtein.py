import mapping_word
import levenshtein
import cost
mapping = mapping_word.mapping_word()

def split_emjeoul(word,debug=True):
    if debug ==True:
        print("음절리벤슈타인 /음절단위로 나누기")
        print(list(word))
    return list(word)

def levenshteins(center,compare,debug=True):
    center = split_emjeoul(center)
    compare = split_emjeoul(compare)
    dif = levenshtein(center[0],compare[0])
    if debug:
        print("음절 리벤슈타인 시작 부분/")
        print(center,compare)
        print("dif : ",dif)
    return dif

def substitution_cost(center_c,compare_c,debug=True):
    result = 0
    if c1 == c2:
        result = 0
    else:
        result = compare_char(center_c,compare_c)
    if debug:
        print("음절 리벤슈타인/cost 확인")
        print(result)
    return result


def compare_char(center_c,compare_c,debug=True):
    center_c = mapping.preprocessings(center_c)
    compare_c = mapping.preprocessings(compare_c)
    result = 0
    if is_all_diff(center_c,compare_c):
        result =  enum.beta
    else:
        result = levenshtein.levenshteins(ceter_c,compare_c)
    if debug:
        print("음절 리벤슈타인/compare_char")
        print("center_c ",center_c,"compare_c ",compare_c)
        print(result)
    return result

def is_all_diff(c1,c2):
    c1_leng = len(c1)
    c2_leng = len(c2)
    count =0
    if c1_leng != c2_leng:
        return False
    for i in range(c1_leng):
        if c1[i] == c2[i]:
            count+=1
    if count != c2_leng:
        return False
    return True


def levenshtein(s1,s2,cost=None, debug=True):
    if debug:
        print("center- ",s1,"comapre - ",s2)

    if len(s1) < len(s2):
        levenshtein(s2,s1,debug=debug)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2)+1)
    for i,c1 in enumerate(s1):
        current_row = [i+1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j+1] + 1
            deletions = current_row[j] +1
            substitutions = previous_row[j] +substitution_cost(c1,c2)
            current_row.append(min(insertions,deletions,substitutions))
        if debug:
            print(current_row[1:])
        previous_row = current_row
    return previous_row[-1]
