# coding: utf-8

#目次 
    #曲基本設定 
    #音程など 

#パラメータを減らせば修正は要らないのか?  

import random  #乱数を使えるようにする 
from fractions import Fraction  #分数を使えるようにする 

#ここから曲の基本設定 
beat=4  #拍子を4拍子に固定
print("拍子:"+str(beat)+"/4")

bpm=random.randint(150,200)  #BPMの乱数。150から200 
print("BPM:"+str(bpm))

keyl=["C","D-","D","E-","E","F","G-","G","A-","A","B-","B"]  #調のリスト。長調と短調とは区別していない 
key=random.randint(0,11)  #調の乱数。リスト"keyl"の何番目かを決める。ちなみに1番目からではなく0番目からスタートする 
print("調:"+keyl[key])
#ここまでの出力例: 
    #拍子:4/4 
    #BPM:160 
    #調:G 

#ここから音程など 
list1=[]  #全体のリスト  
lenl=[Fraction("1/8"),Fraction("1/4"),Fraction("3/8"),Fraction("1/2")]  #音の長さのパターン 
notel=["C","D-","D","E-","E","F","G-","G","A-","A","B-","B"]  #音のリスト。今思うとkeylと共通化できそう 
notenl=[0,2,4,7,9]  #↑の何番目かのリスト。今回はペンタトニックでやる
#こんなことをする必要があるかって? 構造を使いまわしたかった 
basel=["C","D","E","F","G","A"]  #ベースの音のリスト 

lenn=0  #変数の初期化  
for h in range(4): 
    for i in range(8):
        list1.clear()  #list1を空にする
        
        len1=random.randint(0,3)  #音の長さの乱数
        lenn+=lenl[len1]  #何してるか後でわかる 
        list1.append(str(lenl[len1])) 
    
        noten=random.randint(0,4)  #音程の乱数 
        note=notenl[noten]
        list1.append(notel[note])  #半音上げ下げするためにnotenlというリストを作った 
        #har=random.randint(3,6)  #ハーモニーの乱数。3,4,5,6度から選択。上か下かはご自由に 
        #list1.append(har) 

        if lenn<beat/4:  #lennは音の長さの合算。
        #1小節未満なら[音の長さ,音程,ハーモニーの度数]というリスト(list1)を出力して for i に戻る 
            print(list1,end=" ")
        else:  #lennが1小節以上ならlist1を出力して for i のループを抜ける
            print(list1,end=" ") 
            lenn=0
            break
    #oct1=random.randint(3,4)  #その小節の音のオクターブの乱数。C4みたいにアルファベットの後につく数字
    #oct1=3
    #print(oct1, end=" ") 
    base=random.randint(0,5)  #その小節のベースの音の乱数
    print(basel[base])
    #['長さ', '音程']  ベース音 のように出力される
