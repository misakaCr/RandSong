# coding: utf-8
import random
beat=7 #拍子
noten=0
prenoten=0
#notenl=["C","D-","D","E-","E","F","G-","G","A-","A","B-","B"]  #音のリスト
notenl=["C","D","E","F","G","A","B"]  #音のリスト
for h in range(4): 
    for i in range(beat*2): 
        noten=random.randint(0,6)  #音程の乱数。
        if (i>0) and (noten==prenoten): #前の音と同じだったら1足す。ただし最大値だったらオーバーするので1引く
            if(noten==6):
                noten-=1
            else: 
                noten+=1
        print(notenl[noten],end=" ")
        prenoten=noten
    print()