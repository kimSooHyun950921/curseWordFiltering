# coding=utf-8
import hgtk
import decompose
import Dic


class MappingWord:
    def __init__(self):
        pass

    def read_word(self):
        split_result = list()
        all_list = list()
        with open('slang1.csv') as slang_file:
            while True:
                word= slang_file.readline()
                if word is '\n':
                    break
                result = self.preprocessing(word)
                all_list.append(result)
        return all_list
    def preprocessing(self,word):
        result = hgtk.text.decompose(word)


        result = result.replace("\n","")
        result = result.replace(" ","")
        result = result.replace('ᴥ','')
        return result
    def multi_eumso_to_single_eumso(self,word):
        single_eumso = list()
        multi_eumso = Dic.multi_eumso
        for i in range(len(word)):
            if word[i] in multi_eumso:
                changing_word = multi_eumso[word[i]]
                single = self.add_eumso(single_eumso,changing_word)
                #single_eumso +=single
            else:
                single_eumso.append(word[i])
        return single_eumso

    def add_eumso(self,single_eumso,changing_word):
        for i in range(len(changing_word)):
            single_eumso.append(changing_word[i])
        return single_eumso

    # 보류
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

if  __name__ == '__main__':
    map = MappingWord()
    map.mapping_number()
