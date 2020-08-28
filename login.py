def creat(user,password):
    with open('account.txt','a') as file:
        file.write(f'{user} {password}\n')

def loginfunction(user,password):
    logininfo = f'{user} {password}'
    with open('account.txt','r') as file:
        users = file.readlines()
        loop = True
        f= 0
        while loop:
            if logininfo in str(users[f]):
                print("login sucssesful")
                break
            f +=1
            if f == users.__len__():
                print("Try Again")
                loop = False

choice = True
while choice:
    print("1.creat")
    print('2.login')
    print('3.exit')
    var = int(input("select opetion:-"))
    if var == 1:
        name = input("Enter name :-")
        password = input("Enter the password:-")
        creat(name,password)
    elif var == 2:
        name = input("Enter name :-")
        password = input("Enter the password:-")
        loginfunction(name,password)
    elif var == 3:
        choice = False
