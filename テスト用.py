import os
import phonenumbers
import re
#pattern = '0\d{10,11}' 
#pattern2 = '\d{11}'
#new_pattern = pattern1 and pattern2
class FileOperation(object):
    def __init__(self, arg1):
        self.regist = arg1
        
    def read_file(self):#regist,delete,searchに使用
        with open(filename, 'r', encoding = 'UTf-8') as f: 
            file_text = f.read()
        return file_text
    
    def write_file(self):
        with open(filename, 'a', encoding = 'UTF-8') as f:
            f.write(str(self.regist) + '\n')

class FileOperation4(object):                    
    def readlines_file(self):#searchに使用
            with open(filename, 'r', encoding = 'UTF-8') as f:
                phone_lists = f.readlines()
                return phone_lists
                
file_open = FileOperation("")

#a = FileOperation3()
b = FileOperation4()
filename = 'new.txt'

class NameNum(object):
    def __init__(self):
        print('名前を入力してください')
        self.name = input('名前：')
        print('電話番号をハイフンなしで入力してください')
        self.phone_num = input('電話番号：')
        try:
            hyphen = phonenumbers.parse(self.phone_num, 'JP')
            self.phone_num = phonenumbers.format_number(hyphen, phonenumbers.PhoneNumberFormat.NATIONAL)
            #print(self.phone_num)
        except:
            print('電話番号を正しく入力してください')
        self.regist = ["名前：" + self.name, "電話番号:" + self.phone_num]

class Search(object):
    def search_phone(self):
        fileOpenSearch = FileOperation4()
        fileOpenSearch.readlines_file()
        ret = os.path.getsize(filename)
        if ret == 0:
            print('ファイルは空です ' + '\n')
        else:
            print('名前で検索する場合は１、電話番号で検索する場合は2、終了する場合は３をおしてください')
            search = input('番号：')
            if search == str(1) and 1:
                self.name = input('名前をいれてください：')
                if len(self.name) > 0:
                    fileOpenSearch.readlines_file()
                    for phone_list in fileOpenSearch.readlines_file():
                        #print(phone_list)
                        if self.name in phone_list:
                            print(phone_list + 'がみつかりました')
                            #if phone_list.find(self.name) >= 0:
                             #   print(phone_list[:-1] + 'がみつかりました' + '\n') 
                              #  break
                    file_open.read_file()
                    if self.name not in file_open.read_file():
                        print(self.name + 'はみつかません'+ '\n')
                else:
                    print('名前を正しく入力してください')
            elif search == str(2) and 2:
                try:
                    self.phone_num = input('電話番号：')
                    hyphen = phonenumbers.parse(self.phone_num, 'JP')
                    self.phone_num = phonenumbers.format_number(hyphen, phonenumbers.PhoneNumberFormat.NATIONAL)
                except:
                    print('電話番号を正しく入力してください')
                else:
                    fileOpenSearch.readlines_file()
                    for phone_list in fileOpenSearch.readlines_file():
                         if self.phone_num in phone_list:
                            print(phone_list + 'がみつかりました')
                        #if phone_list.find(self.phone_num) >= 0:
                         #   print(phone_list[:-1] + 'がみつかりました' + '\n') 
                          #  break
                    file_open.read_file()
                    if self.phone_num not in file_open.read_file():
                        print(self.phone_num + 'はみつかません' + '\n')
            elif search == str(3) and 3:
                print('検索を終了しました' + '\n')
                #break
            else:
                print('番号が正しくありません' + '\n')

i = Search()
i.search_phone()
                

'''#名前と電話番号入力の土台を作成
class NameNum(object):
    def __init__(self):
        print('名前を入力してください')
        self.name = input('名前：')
        print('電話番号をハイフンなしで入力してください')
        self.phone_num = input('電話番号：')
        if re.fullmatch(pattern1, self.phone_num) or re.fullmatch(pattern2, self.phone_num):
            try:
                hyphen = phonenumbers.parse(self.phone_num, 'JP')
                self.phone_num = phonenumbers.format_number(hyphen, phonenumbers.PhoneNumberFormat.NATIONAL)
            except:
                 print('電話番号を正しく入力してください')
        else:
            print('電話番号を正しく入力してください')
        self.regist = ["名前：" + self.name, "電話番号:" + self.phone_num]

#機能別にクラスを作成（Regist、Deleteは継承）
class Regist(NameNum):
    def regist_phone(self):
        if len(self.name) == 0:
            print('名前を正しく入力してください')
        else:
            file_open.read_file()
            if self.name in file_open.read_file():
                if re.fullmatch(pattern1, self.phone_num) or re.fullmatch(pattern2, self.phone_num):
                    if self.phone_num in file_open.read_file() or self.phone_num != '':
                        print('すでに登録があります')
            elif self.regist:
                print(self.regist)
                fileOpenWrite = Fileope.FileOperation(self.regist)
                fileOpenWrite.write_file()
                print('登録が完了しました' + '\n')
            else:
                print('登録できませんでした')
class Search(object):
    def search_phone(self):
        with open(filename, 'r', encoding = 'UTF-8') as f:
            phone_lists = f.read().split(',')
            for phone_list in phone_lists:
                if phone_list:
                    print('名前で検索する場合は１、電話番号で検索する場合は2、終了する場合は３をおしてください')
                    search = input()
                    if search == str(1) and 1:
                        self.name = input('名前をいれてください：')
                        if len(self.name) > 0:
                            with open(filename, 'r', encoding = 'UTF-8') as f:
                                phone_lists = f.readlines()
                                for phone_list in phone_lists:
                                    if phone_list.find(self.name) >= 0:
                                         print(phone_list[:-1] + 'がみつかりました' + '\n') 
                                         break
                            with open(filename, 'r', encoding = 'UTF-8') as f:
                                phone_lists = f.read()
                                if self.name not in phone_lists:
                                    print(self.name + 'はみつかません'+ '\n')
                        else:
                            print('名前を正しく入力してください')
                    elif search == str(2) and 2:
                        try:
                            self.phone_num = input('電話番号：')
                            hyphen = phonenumbers.parse(self.phone_num, 'JP')
                            self.phone_num = phonenumbers.format_number(hyphen, phonenumbers.PhoneNumberFormat.NATIONAL)
                        except:
                            print('電話番号を正しく入力してください')
                        else:
                            with open(filename, 'r', encoding = 'UTF-8') as f:
                                phone_lists = f.readlines()
                                for phone_list in phone_lists:
                                    if phone_list.find(self.phone_num) >= 0:
                                        print(phone_list[:-1] + 'がみつかりました' + '\n')
                                        break
                            with open(filename, 'r', encoding = 'UTF-8') as f:
                                phone_lists = f.read()
                                if self.phone_num not in phone_lists:
                                    print(self.phone_num + 'はみつかません' + '\n')
                    elif search == str(3) and 3:
                        print('検索を終了しました' + '\n')
                        break
                    else:
                        print('番号が正しくありません' + '\n')
                else:
                    print('ファイルは空です ' + '\n')
'''