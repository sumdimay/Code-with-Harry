n=1


count = 10

while count>0:

    n1 = int(input('enter the number: \n'))
    
    if n==n1:
                print('CORRECT GUESS')
                break
            
    else:
        count = count - 1
        print('WRONG GUESS     guess LEFT: '+str(count))

else:
        print('\n GAMEOVER \n')