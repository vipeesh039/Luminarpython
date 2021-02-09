lst1=[10,20,21,22,23]
lst2=[8,9,20,21,24]
pos1=0
pos2=0
#cnt=0
while(pos1<len(lst1)) & (pos2<len(lst2)):
    #cnt += 1
    if lst1[pos1]==lst2[pos2]:
        print(lst1[pos1])
        pos1+=1
        pos2+=1

    elif lst1[pos1]>lst2[pos2]:
        pos2+=1
    else:
        pos1+=1
#print(cnt)