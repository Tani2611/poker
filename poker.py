import random


def check(cards):
    '''手札の役をstrでreturnする'''
    hand = ''
    
    clear1 = [
           ['A',2,3,4,5],
           [10,'J','Q','K','A'],
           ]
    clear2 = [
            # ['A',2,3,4,5],!
           [2,3,4,5,6],
           [3,4,5,6,7],
           [4,5,6,7,8],
           [5,6,7,8,9],
           [6,7,8,9,10],
           [7,8,9,10,'J'],
           [8,9,10,'J','Q'],
           [9,10,'J','Q','K'],
            # [10,'J','Q','K','A'],
           ]


    count1 = 0
    count2 = 0
    count3 = 0

    # ロイヤルストレートフラッシュ
    for i in range(len(clear1)):
        count2 == 0
        for j in range(len(clear1[i])):
            for k in range(len(cards)):
                if clear1[i][j] == cards[k][1]:
                    count2 += 1
                    if count2 == 5:
                        hand = 'ロイヤルストレートフラッシュ'
                        break
        if count2 == 5:
            break
        
    if hand != '':
        return hand

    
    # ストレートフラッシュ
    for i in range(len(clear2)):
        for j in range(len(clear2[i])):
            count3 = 0
            for k in range(len(cards)):
                if clear2[i][j]== cards[k][1]:
                    count3 += 1
                    if count3 == 5:
                        hand = 'ストレートフラッシュ'
                        break
            
        if count3 == 5:
            break
            
    if hand != '':
        return hand


    # フラッシュ
    for i in range(len(cards)):
        if cards[-1][0] == cards[i][0]:
            count1 += 1
            if count1 == 5:
                hand = 'フラッシュ'
                break
            
    if hand != '':
        return hand
            
    

    # ストレート
    clear = [
           ['A',2,3,4,5],
           [2,3,4,5,6],
           [3,4,5,6,7],
           [4,5,6,7,8],
           [5,6,7,8,9],
           [6,7,8,9,10],
           [7,8,9,10,'J'],
           [8,9,10,'J','Q'],
           [9,10,'J','Q','K'],
           [10,'J','Q','K','A'],
           ]

    count = 0


    for i in range(len(clear)):
        if count == 5:
            break
        count = 0
        
        for j in range(len(clear[i])):
            if count == 5:
                break
            
            for k in range(len(cards)):
                if cards[k][1] == clear[i][j]:
                    count += 1
                    break

    if count == 5:
        hand = 'ストレート'
        
    if hand != '':    
        return hand


    

    list1 = []
    count = 0
    for i in range(5):
        for j in range(5):
            if cards[i][1] == cards[j][1]:
                count += 1
        list1.append(count)
        count = 0
        
    
    # 0ペアからフルハウスまで
    if max(list1) == 4:
        hand = '4カード'
    elif max(list1) == 3:
        if sum(list1) == 13:
            hand = 'フルハウス'
        else:
            hand = '3カード'
    elif max(list1) == 2:
        if sum(list1) == 9:
            hand = '2ペア'
        else:
            hand = '1ペア'
    elif max(list1) == 1:
        hand = '0ペア'
     
    if hand != '':
        return hand

    
        

    

# カードの準備
mark = ('♥','♦','♠','♣')
num = ('A',)
num += tuple(range(2,11))
num += ('J','Q','K')

# リストにカードを並べる
deck = []
for i in mark:
    for j in num:
        deck.append((i,j))
deck.append(('Joker',''))
deck = tuple(deck)  # タプルに変換


# カードを5枚引く
cards = []
i = 0
while i < 5:
    t = deck[random.randint(0,52)]
    if t in cards:
        continue
    cards.append(t)
    i += 1

# 0ペア
# cards = [deck[1],deck[3],deck[15],deck[19],deck[50]]

# 1ペア
# cards = [deck[0],deck[13],deck[7],deck[30],deck[51]]

# 2ペア
# cards = [deck[12],deck[13],deck[26],deck[16],deck[51]]

# 3カード
# cards = [deck[0],deck[13],deck[26],deck[5],deck[51]]

# ストレート
# cards = [deck[16],deck[15],deck[1],deck[30],deck[44]]

# フラッシュ
cards = [deck[9],deck[5],deck[0],deck[11],deck[3]]

# フルハウス
# cards = [deck[0],deck[13],deck[26],deck[4],deck[17]]

# 4カード
# cards = [deck[0],deck[13],deck[26],deck[39],deck[3]]

# ストレートフラッシュ
# cards = [deck[1],deck[2],deck[3],deck[4],deck[5]]

# ロイヤルストレートフラッシュ
# cards = [deck[9],deck[10],deck[11],deck[12],deck[0]]


# 表示
print('あなたのカード：', end = '')
for i in range(5):
    for j in range(2):
        print(cards[i][j],end = '')
    print(' ',end = '')      
print()


# 役を判定して出力
print(check(cards))


