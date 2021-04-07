import random
game_count=1
list=[]
list2=[] 
print('***Best out of ten games***')
user_name = input('Enter your name:')
while game_count<=10:
    if game_count<11:
        choice_user=int(input('Enter:\n1. Rock\n2. Paper\n3. Scissor\n'))
        print('User chose: '+str(choice_user))
        choice_computer = random.randint(1,3)
        print('Computer chose: '+str(choice_computer))

        if choice_user==1 and choice_computer==2:
            print('Winner is Computer')
            list.append(1)
        elif choice_user==1 and choice_computer==3:
            print('Winner is '+user_name)
            list2.append(1)
        elif choice_user==2 and choice_computer==1:
            print('Winner is '+user_name)
            list2.append(1)
        elif choice_user==2 and choice_computer==3:
            print('Winner is Computer')
            list.append(1)
        elif choice_user==3 and choice_computer==1:
            print('Winner is Computer')
            list.append(1)
        elif choice_user==3 and choice_computer==2:
            print('Winner is '+user_name)
            list2.append(1)
        else:
            print('Its a draw | Point shared')
            list.append(1)
            list2.append(1)
            
        print('End of game: '+str(game_count))   
        game_count = game_count + 1

    else:
        print('Game Over')

if len(list2)>len(list):
    print('Final winner is '+user_name)
elif len(list)>len(list2):
    print('Final winner is Computer')
else:
    print('Its a DRAW')                  
