def gettime():
    import datetime
    s1=datetime.datetime.now()
    return s1
#######################################################################################################
def HMSystem():
    a=int(input('type 1 to log or type 2 to retrive: '))
    if a==1:
        choice=int(input('Select:\n 1=Food\n 2=Exercise\n '))
        if choice==1:
            username=int(input('Select user to log: \n 1=Sumedh \n 2=Rutu \n 3=Tejas \n'))
            if username==1:
                val=input("enter food:\n")
                with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/sumedh_food.txt",'a') as file:
                    file=file.write(val+" "+ str(gettime()) +" \n")
                print("Successfully Written")
            elif username==2:
                val=input("enter food:\n")
                with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/rutu_food.txt",'a') as file:
                    file=file.write(val+" "+ str(gettime()) +" \n")
            else:
                val=input("enter food:\n")
                with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/tejas_food.txt",'a') as file:
                    file=file.write(val+" "+ str(gettime()) +" \n")
        elif choice==2:
            username=int(input('Select user to retrive: \n 1=Sumedh \n 2=Rutu \n 3=Tejas \n'))
            if username==1:
                val=input("enter exercise:\n")
                with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/sumedh_exercise.txt",'a') as file:
                    file=file.write(val+" "+ str(gettime()) +" \n")
            elif username==2:
                val=input("enter exercise:\n")
                with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/rutu_exercise.txt",'a') as file:
                    file=file.write(val+" "+ str(gettime()) +" \n")
            else:
                val=input("enter exercise:\n")
                with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/tejas_exercise.txt",'a') as file:
                    file=file.write(val+" "+ str(gettime()) +" \n")
        else:
            print('Invalid input')
#######################################################################################################
    elif a==2:
        choice=int(input('Select:\n 1=Food\n 2=Exercise\n '))
        if choice==1:
            username=int(input('Select user to retrive: \n 1=Sumedh \n 2=Rutu \n 3=Tejas \n'))
            if username==1:
                with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/sumedh_food.txt",'rt') as file:
                 file=file.read()
            elif username==2:
                 with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/rutu_food.txt",'rt') as file:
                  file=file.read()
            else:
                 with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/tejas_food.txt",'rt') as file:
                  file=file.read()
            return file
        elif choice==2:
            username=int(input('Select user to retrive: \n 1=Sumedh \n 2=Rutu \n 3=Tejas \n'))
            if username==1:
                with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/sumedh_exercise.txt",'rt') as file:
                 file=file.read()
            elif username==2:
                 with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/rutu_exercise.txt",'rt') as file:
                  file=file.read()
            else:
                 with open("/Users/sumedh/Desktop/Python Practice/base/Health Management System/tejas_exercise.txt",'rt') as file:
                  file=file.read()
            return file
        else:
            print('Invalid input')
    else:
            print('\n Invalid input \n')
#######################################################################################################
print(HMSystem())
