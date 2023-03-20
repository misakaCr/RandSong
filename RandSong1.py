# coding: utf-8

#Pythonに関する説明 
    #print()  #()内のものを出力 
    #random.randint()  #整数の乱数 
    #l=[]  #lというリストを作成  
    #l[i]  #lというリストのi番目 
    #l.append()  #lというリストに()内のものを追加 
    #for  #指定回数のループ 

#目次 
    #曲基本設定 
    #音程など 
    #ドラム 

import random  #乱数を使えるようにする 
from fractions import Fraction  #分数を使えるようにする 

#ここから曲の基本設定 
beat=random.randint(2,4)  #拍子の乱数。2/4,3/4,4/4,5/4,6/4,7/4 
#beat=4  #拍子を指定したい場合はこう書く 
print("拍子:"+str(beat)+"/4")

bpm=random.randint(60,250)  #BPMの乱数。60から250 
print("BPM:"+str(bpm))

keyl=["C","D-","D","E-","E","F","G-","G","A-","A","B-","B"]  #調のリスト。長調と短調とは区別していない 
key=random.randint(0,11)  #調の乱数。リスト"keyl"の何番目かを決める。ちなみに1番目からではなく0番目からスタートする 
print("調:"+keyl[key])
#ここまでの出力例: 
    #拍子:4/4 
    #BPM:140 
    #調:G 

#ここから音程など 
list1=[]  #全体のリスト  
lenl=[Fraction("1/8"),Fraction("1/4"),Fraction("3/8"),Fraction("1/2")]  #音の長さのパターン 
notel=["C","D-","D","E-","E","F","G-","G","A-","A","B-","B"]  #音のリスト。今思うとkeylと共通化できそう 
notenl=[0,2,4,5,7,9,11]  #↑の何番目かのリスト。あてはめて見るとわかるが、臨時記号がつかない音である。
#なぜこんなことをしたかって? あとでわかるよ 
basel=["C","D","E","F","G","A"]  #ベースの音のリスト 

lenn=0  #変数の初期化  
for h in range(4): 
    for i in range(8):
        list1.clear()  #list1を空にする
        
        len1=random.randint(0,3)  #音の長さの乱数
        lenn+=lenl[len1]  #何してるか後でわかる 
        list1.append(str(lenl[len1])) 
    
        noten=random.randint(0,6)  #音程の乱数 
        note=notenl[noten]
        notenp=random.randint(0,15)  #臨時記号の乱数
        if notenp==0 and note<11:  #1/16の確率で半音上げる。ただし音がBの場合を除く 
            note+=1
        elif notenp==1 and note>0:  #1/16の確率で半音下げる。ただし音がCの場合を除く 
            note-=1
        list1.append(notel[note])  #半音上げ下げするためにnotenlというリストを作った 
        har=random.randint(3,6)  #ハーモニーの乱数。3,4,5,6度から選択。上か下かはご自由に 
        list1.append(har) 

        if lenn<beat/4:  #lennは音の長さの合算。
        #1小節未満なら[音の長さ,音程,ハーモニーの度数]というリスト(list1)を出力して for i に戻る 
            print(list1,end=" ")
        else:  #lennが1小節以上ならlist1を出力して for i のループを抜ける
            print(list1,end=" ") 
            lenn=0
            break
    oct1=random.randint(3,4)  #その小節の音のオクターブの乱数。C4みたいにアルファベットの後につく数字
    print(oct1, end=" ") 
    base=random.randint(0,5)  #その小節のベースの音の乱数
    print(basel[base])
    #['長さ', '音程', 'ハーモニーの度数'] オクターブの数字 ベース音 のように出力される
    #出力例: ['1/2', 'F', 5] ['1/8', 'B-', 6] ['3/8', 'A-', 3] 3 F


#ここからドラム。大体さっきと同じ 
#ちなみに拍子の情報がないと以降のコードだけ実行してもうまくいかない 
list2=[]
lenl2=[Fraction("1/16"),Fraction("1/8"),Fraction("3/16"),Fraction("1/4")]
notel2=["C","D-","D","E-","E","F","G-","G","A-","A","B-","B"]  #正確には音程はないが便宜上こうしている 
lenn2=0
for k in range(2):
    for j in range(16):
        list2.clear()
           
        len2=random.randint(0,3)
        lenn2+=lenl2[len2]
        list2.append(str(lenl2[len2]))
    
        note2=random.randint(0,11)
        list2.append(notel2[note2])
        if note2<=4:
            oct2=random.randint(1,2)
        else:
            oct2=1
        list2.append(oct2)    
        if lenn2<=beat/4:  #lenn2(音の長さの合算)が1小節「以下」の場合。なぜこうしたかは覚えていない　
            print(list2,end=" ")
        else:
            print(list2,end=" ")
            lenn2=0
            break
    #出力例: ['3/16', 'C', 1] ['1/4', 'D', 1] ['1/4', 'A-', 1] ['1/4', 'E', 2] 
    #['1/4', 'A-', 1] ['1/16', 'G-', 1] ['1/16', 'B-', 1]
    
    
    