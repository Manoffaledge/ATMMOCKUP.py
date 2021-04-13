import random

database = {}
userDetails = database

def homePage():
     print('Welcome to Neveda Bank')

     haveAccount = int(input('Do you have an account with us: 1 (yes) 2 (no) \n'))

     if(haveAccount == 1):
           login(userDetails)

     elif(haveAccount == 2):
           register()

     else:
          print('Invalid selection, try again')
          homePage()

def login(userDetails):
     print('********** login **********')

     userAccount = int(input('Please input your account number: \n'))
     password = input('Please input your password: \n')

     for accountNumber, userDetails in database.item():
          if(accountNumber == userAccount):
               if(userDetails[3] == password):
                     bankOperation(userDetails)
      
     print('Invalid option selected, Please try again')

def register():
     print('********Please register*******')

     email = input('What is your email address? \n')
     first_Name = input('What is your first name? \n')
     last_Name = input("What is your last name? \n")
     password = input('create a password \n')
     
     accountNumber = accountGenerator()

     database[accountNumber] = [ first_Name, last_Name, email, password,  ]
     userDetails = database[accountNumber]

     print('Your account has been created %d ' % accountNumber)

     login(userDetails)


def bankOperation(userDetails):

     selectOption = int(input('Please select an option (1) Deposit (2) withdrawal (3) logout \n'))

     if(selectOption == 1):
          depositOp()
     
     elif(selectOption == 2):
          withdrawalOP()
     
     elif(selectOption == 3):
          login(userDetails)
     
     else:
          print('********** invalid operations **********')
          bankOperation(userDetails)

def  withdrawalOP():
     print('Make your withdrawal')


def depositOp():
     print('Make your deposit ')

def accountGenerator():

     return random.randrange(0000000000,9999999999)

homePage()





 
      
