import random

database = {}

def homePage():
     print('Welcome to Neveda Bank')

     haveAccount = int(input('Do you have an account with us: 1 (yes) 2 (no) \n'))

     if(haveAccount == 1):
           login()

     elif(haveAccount == 2):
           register()

     else:
          print('Invalid selection, try again')
          homePage()

def login():
     print('********** login **********')

     userAccount = int(input('Please input your account number: \n'))
     password = input('Please input your password: \n')

     for userAccountNumber, userDetails in database.items():
          if(userAccountNumber == userAccount):
               if(userDetails[3] == password):
                    bankOperation()

     print('Invalid input, Please try again')
     login()

def register():
     print('******** Please register *******')

     email = input('What is your email address? \n')
     first_Name = input('What is your first name? \n')
     last_Name = input("What is your last name? \n")
     password = input('create a password \n')
     
     userAccountNumber = accountNumberGenerator()
     database[userAccountNumber] = [ first_Name, last_Name, email, password ]
    
     print('This is your account number %d ' % userAccountNumber)

     login()
            
def bankOperation():
     print('Welcome')

     selectOption = int(input('Please select an option (1) Deposit (2) withdrawal (3) logout (4)exit \n'))

     if(selectOption == 1):
          depositOp()
     
     elif(selectOption == 2):
          withdrawalOP()
     
     elif(selectOption == 3):
          login()
     
     elif(selectOption == 4):
          goodbyePage()
     
     else:
          print('***** Invalid Selection *****')
          bankOperation()


def  withdrawalOP():
     withdrawAmount = int(input('Input withdrawal amount: \n'))
     
     if(withdrawAmount <= 500000):
          print('Please take your cash')
          goodbyePage()

     elif(withdrawAmount < 500):
          print('lowest amount withdrawable is 500')
          withdrawalOP()

     elif(withdrawAmount > 500000):
          print('Withdrawable amount limit reached')
          withdrawalOP()
     
     print('Make your withdrawal')
     

def depositOp():
     print('Make your deposit ')

def accountNumberGenerator():

     return random.randrange(0000000000,9999999999)

def goodbyePage():
     print('Goodbye')
     print('Thank you for banking with us')


homePage()
