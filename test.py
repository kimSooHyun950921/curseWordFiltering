import levenshtein
import mapping_word


first = input("첫번째 단어 - ")
second = input("두번쨰 단어 - ")

def change_word_to_num(first):
    mapping = mapping_word.mapping_word()
    word = mapping.preprocessing([first])
    word = mapping.multi_eumso_to_single_eumso(word)
    return word
first = change_word_to_num(first)
second = change_word_to_num(second)

result = levenshtein.levenshteins(first,second)
print(result)
