def search(list,n):
    list2=[]
    flag = False
    
    for i in range(len(list)):
        if n==list[i]:
            flag = True
            list2.append(i)
            
    if flag==True:
        print('number found in the index value of: ',list2)
        
    else:
        print("NOT FOUND")
            

list = [1,2,3456,6745,234,8567,865,345,456,567,567,2345,2,2,2,234,36,568,679,780]
n=2
search(list,n)

