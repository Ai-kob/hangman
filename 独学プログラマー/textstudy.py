#独学プログラマーのチャレンジ問題
'''
def number_get(a):
    return a ** 2

print(number_get(5))

apple = 'リンゴは赤くて甘い食べ物です'

def apple_print():
    return apple

print(apple_print())

def people_pattern(age, height, weight, name='guest', sex='both'):
    return '私の名前は' + name +'。性別は'+ sex + 'です。年齢は' + str(age) + '才です。身長と体重は' + str(height) +'cm' + str(weight) + 'kgです。' 
print(people_pattern(30, 164, 45))

#二つの関数からなるプログラムを書いてみよう
#１つ目の関数は引数に整数を、それを２で割って求められる整数を出力として返そう
#2つ目の関数は整数を引数に４でかけた数を返そう　プログラム内で１つめの関数を呼び戻り値を変数として保存、２つ目の関数の引数として渡そう
a = 10
def num_one():
    return a / 2

def num_two():
    return num_one() * 4

print(num_one())
print(num_two())

b = 'chanage!'

def num_change():
    try:
        print(float(b))
    except ValueError:
        print('変換できません！')
num_change()

def f(x):
    return x + 1
z = f(4)
print(z)

myfavorite = ['ジュディマリ', '尾崎豊', 'LM.C','Official髭男dism','あいみょん']
myfavorite_jisyo = {'ジュディマリ':'そばかす', '尾崎豊':'15の夜', 'LM.C':'88','Official髭男dism':'HELLO','あいみょん':'ハレノヒ'}
mymap = ('HONOLULU', '18°55 - 29°', '154°40 - 162°')
myinfo = {'color':'green', 'food':'chocholate', 'tvshow':'有吉の壁'}

def ans_input():
    info_get = input('キーを入力してください：')
    return myinfo[info_get]

#print(ans_input())
c = list(myfavorite_jisyo.values())
print(c)

a = 'カミュ'
for i in a:
    print(i)
    
what = input('何を:')
who = input('誰に：')
print('私は昨日{}を書いて{}に送った！'.format(what, who))

b = 'aldous Huxley was born in 1894.'
print(b.capitalize())

c = '誰が？,いつ？,どこで？'
print(c.split('?'))

d = ['The', 'fox', 'jumped', 'over', 'the', 'fence', '.']
print(' '.join(d)[:29] + '.'.join(d)[30:31]

e = 'A screaming comes across the sky'
print(e.replace('s', '$'))

f = 'Hemingway'
print(f.index('m'))

g = '私はその犬に"タイ"という名前をつけた'
print(g)

h = 'Three' + 'Three' + 'Three'
print(h)
print(h * 3)

i = '四月の晴れた寒い日で、時計がどれも十三字を打っていた。'
print(i[0:10])

videolists = ['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
for videolist in videolists:
    print(videolist)

for i in range(25,51):
    print(i)

videolists = ['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
for i, videolist in enumerate(videolists):
    print(i, videolist)

while True:
    try:
        num = input('数字を入力してください：')
        num_b = int(num)
        if num_b == 5:
            print('正解！！')
            continue
        elif num_b != 5:
            print('残念、不正解')
            continue
    except ValueError:
        if num == 'q':
            print('終了します！')
            break
        else:
            print('数字を入力するか、ｑで終了してください')

la = [8, 19, 148, 4]
lb = [9, 1, 33, 83]
lc = []
for i in la:
    for j in lb:
        lc.append(i * j)
print(lc)

import statistics
print(statistics.mean(lc))
print(statistics.harmonic_mean(lc))

def num_in(a):
    if __name__ == '__main__':
        return a ** 3

filepath = '志望動機test.txt'

question = input('好きな食べ物は？：') + '\n'
with open(filepath, 'a', encoding='utf-8') as f:
    f.write(question)
with open(filepath, 'r', encoding='utf-8') as f:
    a = f.read()
    print(a)
    
import csv
movie = [['Top Gun', 'Risky Buisiness', 'Minority Report'],
         ['Titanic', 'The Revenant', 'Inception' ],
         ['Training Day', 'Man on Fire', 'Flight']]
movie2 = [['トップガン', '卒業白書', 'マイノリティ・リポート'],
         ['タイタニック', 'レヴェナント: 蘇えりし者', 'インセプション' ],
         ['トレーニング デイ', 'マイ・ボディガード', 'フライト']]
  
with open('test.csv', 'w', newline ='') as f:
    wf = csv.writer(f, delimiter=',')
    wf.writerow(movie[0])
    wf.writerow(movie[1])
    wf.writerow(movie[2])

with open('test.csv', 'a',encoding='utf-8') as of:
    wc = csv.writer(of, delimiter=',')
    wc.writerow(movie2[0])
    wc.writerow(movie2[1])
    wc.writerow(movie2[2])
    
with open('test.csv', 'r', encoding='utf-8') as nf:
    rf = csv.reader(nf, delimiter=',')
    for i in rf:
        print(i)
'''


        



