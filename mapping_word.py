import csv

import hgtk

import dic


DATAFILE = './csv_file/offensive_word_db.csv'


class mapping_word():
    def __init__(self):
        self.word_list = self.read_word()


    def read_word(self):
        word_list = list()
        with open(DATAFILE) as f:
            reader = csv.reader(f)
            for row in reader:
                word_list.append(row[0])
        return word_list

    def preprocessing(self, word_list):
        replace_char = ['\n', ' ', 'ᴥ']
        decompose_list = ''
        for word in word_list:
            decompose_list+=hgtk.text.decompose(word)

        for char in replace_char:
            result = decompose_list.replace(char, '')

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

    def mapping_number(self):
        #result = self.preprocessing(self.word_list)
        all_list = list()

        for word in self.word_list:
            #print(word)
            word = self.preprocessing(word)
            word = self.multi_eumso_to_single_eumso(word)
            all_list.append(word)
        return all_list[:-2]


def main():
    map = mapping_word()
    map.mapping_number()


if __name__ == '__main__':
    main()
