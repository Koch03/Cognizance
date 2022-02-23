list=[]

list.append(['RollNo  Name  Marks'])
list.append([18 ,  'Kowtham' , 98])
list.append([21 ,  'Praveena'  ,91])
list.append([31 , 'Ghiri'  ,79])


for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j],end=" ")
    print("")


for k in range(len(list[2])):
    print(list[2][k],end="\t")