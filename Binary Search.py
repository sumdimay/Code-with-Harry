def binary(list,n):
    low = 0
    high = len(list)-1
    mid=0
    flag = False
    
    while low<=high and not flag:
        mid=(low+high)//2
        
        if n<list[mid]:
            high = mid-1
            
        elif n>list[mid]:
            low = mid+1
        
        else:
            return mid
        
    return -1
            
        
    if flag==True:
        print('found')
    else:
        print('not found')
        
        
        
list = [1,23,65,34,78,34,30,98,23,76,90,65,56]
n=30
list.sort()
print(list)
binary(list,n)
