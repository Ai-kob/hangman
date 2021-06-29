#独学プログラマーチャレンジ問題２
#クラス化以降

'''
class Apple():
    def __init__(self, c, t, k, m):
        self.color = c
        self.taste = t
        self.kind = k
        self.money = m
        
    def apple_name(self):   
        print('私は{}'.format(self.kind))
        
    def apple_count(self, a):
        return self.money * a

apple1 = Apple('red', 'sweet', 'ふじ', 100)
apple2 = Apple('green','sweet', '王林', 120)
apple3 = Apple('red&yellow', 'sour', 'ジョナゴールド',95)

apples = [apple1, apple2, apple3]
for apple in apples:
    apple.apple_name()

import math

class Circle():
    def circle_area(self, a):
        self.area = a * a * math.pi
        return self.area
small = Circle()
print(small.circle_area(5))

class Hexagon():
    def all_round(self, a):
        self.gaisyu = a * 6
        return self.gaisyu
b = Hexagon()
print(b.all_round(4))

class Shape:
    def what_am_i(self):
        return 'I am a Shape'

class Rectangle(Shape):
    def calculate_perimeter(self, a):
        self.long = a * 4
        return self.long

class Squre(Shape):
    def change_size(self, h, w):
        self.height = h
        self.width = w
        return self.height * 2 + self.width * 2
    
a = Rectangle()
b = Squre()
print(a.what_am_i())
print(b.what_am_i())
print(b.change_size(50,-10))

class Horse:
    def __init__(self,name, color, sex, owner):
        self.name = name
        self.color = color
        self.sex = sex
        self.owner = owner
        
class Rider:
    def __init__(self,rider):
        self.rider = rider

suho = Rider('suho')
hakuba = Horse('hakuba', 'white', 'male', suho)
print(suho.rider)
print(hakuba.color)
print(hakuba.owner.rider)

class Squre:
    squre_list = []
    
    def __init__(self, edge):
        self.edge = edge
        self.squre_list.append(self.edge)
        print(self.edge)
     
    def re_new(self):
        print('{} by{} by{} by{}'.format(self.edge,self.edge,self.edge, self.edge))
    
a = Squre
squre1 = a(10)
squre2 = a(30)
squre3 = a(9)
a.squre_list
squre2.re_new()

import this
import re
#print(this)        

#l = 'Beautiful is better than ugly'
#matches = re.findall('beautiful', l, re.IGNORECASE)
#print(matches)

zen =  Althogh never is 
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the imprementation
is easy to explain.,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those 

m = re.findall('^If', zen, re.MULTILINE)
print(m)
string ='Two too'
n = re.findall('t[ow]o', string, re.IGNORECASE)
print(n)

line = '123 hi 34 hello'
l = re.findall('\d', line, re.IGNORECASE)
print(l)

t = '__one__ __two__ __three__'
found = re.findall('__.*?__', t)
for match in found:
    print(match)

text =  キリンは大昔から　__複数名詞__　興味の対象でした。
キリンは　__複数名詞__　の中で一番背が高いですが、科学者たちはそのような
長い　__身体の一部__をどうやって獲得したのか説明できません。
キリンの身長は __数値__　__単位__　近くあり、その高さのほとんどは脚と　__身体の一部__に
よるものです。

def mad_libs(mls):
    
    :param mls:　文字列で、ユーザーに入力してもらいたい単語（＝ヒント）の部分は後を二つの
    アンダースコアではさんでください。ヒントのt名護にはアンダースコアを含めないでください。
    __hint_hint__はダメです。__hint__はOKです。
    
    hints = re.findall('__.*?__', mls)
    if hints is not None:
        for word in hints:
            q = '{}を入力:'.format(word)
            new = input(q)
            mls = mls.replace(word, new)
        print('\n')
        mls = mls.replace('\n', '')
        print(mls)
    else:
        print('引数'+ mls + 'が無効です')
mad_libs(text)

line = 'I love $'
l = re.findall('\\$', line, re.IGNORECASE)
print(l)

zen2 =  Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! 
#b = re.findall('Dutch', zen2, re.MULTILINE)
#print(b)
#text = 'Arizona 479, 501, 870. California 209, 213, 650.'
#new = re.findall('\d{3}', text, re.IGNORECASE)
#print(new)

string = 'The ghost that says boo haunts the loo'
restr = re.findall('[b,l]oo', string, re.IGNORECASE)
print(restr)
'''

