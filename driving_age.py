print(' please enter your age:')
age = int(input())

if age == 18:
    print('give education test to get basic lisence')
    
elif age > 18 and age<30:
    print('you get lisence with test 1')
    
elif age>=30:
    print('No exam and get lisence')    
    
else:
    print('please wait to turn 18')