import csv
for i in range(0,150):
    print('-',end='')
print('\n')
print('\t\t\t\tWELCOME\n')
for i in range(0,150):
    print('-',end='')
print('\n')
print('1.Login')
print('2.Register\n')
x=int(input('Enter your choice : '))

t1=0
t2=0

def validation(user_name,pswd):
    with open('passwords.csv','r') as userFile:
        userFileReader = csv.reader(userFile)
        for row in userFileReader:
            if row[0]==user_name:
                if row[1]==pswd:
                    return 1
    return 0

def login(t1):
    print('\t\t\t\tLogin')
    user_name=input('\nUsername : ')
    pswd=input('Password : ')
    if(t1==2):
        print('Maximum attempts reached please try after sometime')
        return 
    if validation(user_name,pswd):
        return 1
    else:
        print("Wrong username or password, Try again")
        return login(t1+1)

def func(str,a,b):
    for i in str:
        if ord(i)>=int(a) and ord(i)<= int(b):
            return 1
    return 0 

def valid_pswd(pswd):
    if func(pswd,45,45) and func(pswd,65,90) and func(pswd,97,122) and func(pswd,48,57):
        return 1
    return 0

def wirte_pswd(user_name,pswd):
    with open('passwords.csv', mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow([user_name,pswd])


def registerr(t1):
    if t1==3:
        print('Maximum atempts reached please try after sometime')
        return
    
    for i in range(0,150):
        print('-',end='')
    print('\n')
    print('\tNOTE : Password should be of minimum 8 characters containing an    \t\t\tuppercase, a lowercase,a number and a symbol '+'-')
    user_name=input('\nUsername : ')
    pswd=input('password : ')
    if(valid_pswd(pswd)) :
        print('\t\t\t\tsucess\n')
        for i in range(0,150):
            print('-',end='')
        print('\n')
        wirte_pswd(user_name,pswd)
        return login(0)
    else :
        print('\t\t\t\tpassword not valid')
        registerr(t1+1)
    
if(x==1):
    q=login(t1)
    if q==1 :
        for i in range(0,150):
            print('-',end='')
        print('\n\t\t\t\tlogin sucessful')
        for i in range(0,150):
            print('-',end='')
        print('\n')
        while 1:
            print('\n1.face recognisation')
            print('2.face detection')
            print('3.Exit')
            y=int(input('\nenter your choice : '))
            if y==1:
                import face_recognition
            elif y==2:
                import face_detection
            else :
                print('\n\t\t\t\tTHANK YOU\n')
                break
else:
    q=registerr(t1)
    if q==1 :
        for i in range(0,150):
            print('-',end='')
        print('\n\t\t\t\tlogin sucessful')
        for i in range(0,150):
            print('-',end='')
        print('\n')
        while 1:
            print('\n1.face recognisation')
            print('2.face detection')
            print('3.Exit')
            y=int(input('\nenter your choice : '))
            if y==1:
                import face_recognition
            elif y==2:
                import face_detection
            else :
                for i in range(0,150):
                    print('-',end='')
                print('\n\t\t\t\tTHANK YOU\n')
                for i in range(0,150):
                    print('-',end='')
                break