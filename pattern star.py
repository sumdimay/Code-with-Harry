print('Enter number to print pattern')
num = int(input())
print('TYPE 1 if true or 0 if false')
i = int(input())
a='*'
b=1
flag = True

if i==1:
    flag == True
    while num>0:
        print(a*b)
        num=num-1
        b=b+1

else:
        flag == False
        while num>0:
            print(a*num)
            num=num-1
