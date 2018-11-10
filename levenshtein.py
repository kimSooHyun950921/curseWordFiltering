
import dic


def levenshteins(center,compare):
    print(center, compare)
    jaeum_dif = jamo_levenshtein(center[0],compare[0])*1.5
    moeum_dif = jamo_levenshtein(center[1],compare[1])
    return (jaeum_dif,moeum_dif)


def jamo_levenshtein(s1, s2, cost=None, debug=False):
    if len(s1) < len(s2):
        return jamo_levenshtein(s2, s1, debug)
    if len(s2) == 0:
        return len(s1)
    def substitution_cost(c1, c2):
        if c1 == c2:
            return 0
        elif c1 in dic.jaum_list and c2 in dic.jaum_list:
            return dic.jaeum_cost.get(c1)[dic.jaeum.index(c2)]
        elif c1 in dic.moum_list and c2 in dic.moum_list:
            return 1+abs(dic.moeum_cost.get(c1) - dic.moeum_cost.get(c2))
        else:
            return 2

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1]+1
            deletions = current_row[j]+1
            # Changed
            substitutions = previous_row[j] + substitution_cost(c1, c2)
            #print("jamo:",c1,c2,substitution_cost(c1,c2))

            current_row.append(min(insertions, deletions, substitutions))

        if debug:
            print(['%.3f'%v for v in current_row[1:]])
        previous_row = current_row

    return previous_row[-1]
