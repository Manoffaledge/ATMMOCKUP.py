import random

def homePage():
    print('Welcome to Neveda bank')
    haveAccount = int(input('Do you have an account with us (1) yes (2) no \n'))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        registration()

    else:
        print('Invalid option selected try again')
        homePage()

def login():
    userAccountNumber = int(input('Please input your account number: \n'))
    password = input('Please input your password: \n')


def registration():
    print('***** Register *****')
    email = input('What is your email address? \n')
    firstName = input('What is your first name? \n')
    lastName = input('What is your last name? \n')
    password = input('create a password: \n')
    
def bankOperations():
    print ('includes withdrawal, deposit and log out option')

def accountNumberGenerator():
    print('generates new account number for who signs in ')
    return random.randrange(0000000000,9999999999)

homePage()