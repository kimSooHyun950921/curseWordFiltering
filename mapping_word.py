import csv
import decompose

import hgtk

import dic 


DATAFILE = 'offensive_word_db.csv'


class MappingWord(object):
    def __init__(self):
        self.word_list = self.read_word()

    def read_word(self):
        word_list = list()
        with open(DATAFILE) as f:
            reader = csv.reader(f)
            for row in reader:
                word_list.append(row[0])
        return word_list

    def preprocessing(self, word):
        replace_char = ['\n', ' ', 'ᴥ']

        result = hgtk.text.decompose(word)

        for char in replace_char:
            result = result.replace(char, '')

        return result

    def multi_eumso_to_single_eumso(self, word):
        single_eumso = list()
        multi_eumso = dic.multi_eumso

        for i in range(len(word)):
            if word[i] in multi_eumso:
                changing_word = multi_eumso[word[i]]
                single = self.add_eumso(single_eumso, changing_word)
            else:
                single_eumso.append(word[i])
        return single_eumso

    def add_eumso(self, single_eumso, changing_word):
        for i in range(len(changing_word)):
            single_eumso.append(changing_word[i])
        return single_eumso

    def num_to_hangeul(self,num):
        divide_num = num
        korean = list()
        how_many_divide = 0
        while divide_num > 1:
            rest = divide_num % 10
            divide_num = divide_num/10
            if (len(korean)==0 and num !=0) or num>1:
                korean.append(Dic.one_seat_digit[rest])
            if how_many_divide > 0:
                korean.append(Dic.ten_digit[how_many_divide])
            how_many_divide +=1
        return korean

    def mapping_number(self):
        word_list = self.read_word()
        all_list = list()
        for i in range(len(word_list)):
            word = self.multi_eumso_to_single_eumso(word_list[i])
            all_list.append(word)
        return all_list[:-2]


def main():
    map = MappingWord()
    map.mapping_number()


if __name__ == '__main__':
    main()
