#ハングマンを作成
import random
def hangman(word):
    wrong = 0
    stages = ['',
              '      * *      * *   ',
              '    *     * *     *  ',
              '    *      *      *  ',
              '     *           *   ',
              '       *       *     ',
              '         *   *       ',
              '           *         '
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('♪　ハングマンへようこそ　♪')
    print('絵が完成する前に答えをあてよう！')
    
    while wrong < len(stages) - 1:
        char = input('どうぶつの名前だよ！文字を予想してね！>>>')
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('あなたの勝ち！88888')
            print(' '.join(board))
            win = True
            break
        
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け！正解は...{}'.format(word))

answer = ['dog', 'cat', 'bird','pig', 'wolf']
a = random.choice(answer)
hangman(a)
#music = ['紅蓮華', 'はなかっぱ', '勇気100％']　日本語タイトルでもできたー！
#m = random.choice(music)
#hangman(m)
            
            