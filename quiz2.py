fname = input('enter your name ' )
lname = input("Enter Your Last name ")
uname = input("Enter Your User name ")
email = input("Enter Your Email ")
address = input("Enter Your Address ")
pincode = input("Enter Your Pincode ")
city = input("Enter Your City ")
state = input("Enter Your state ")
country = input("Enter Your Country ")
gname = input("Enter your name in the Game ")
age = int(input("Enter your age "))
if age>=18:
    print('Welcome to the Game!')
    password=input('Enter your Password ')
    cpass=input('Confirm your Password ')
    if password==cpass:
        print("You need to accept the following Terms and Conditions")
        user=input( " Do u accept our terms and conitions : ")
        if user == 'yes' or user =='YES':
            print(" Welcome to the GameHUb")
            ques = ('Q1: do variables exist in python ?',
                   'Q2.what is the primary purpose of python?', 
                    'Q3.which of the following is the valid Python data type?',
                     'Q4.which oprator is used for assignment in python?',
                    'Q5.what does print(type(5)) output?',
                     'Q6.what will be the output of print(3+2*4)?'
                     )
            opt=( ('A.yes',  'B.YES' , 'C.no', 'D.NO'),
                ( 'A.for web application ',  'B.for mobile application',  'C.genral purpose program ane script' , 'D.desigh 3D graphics',),
                ('A.string ',  'B.float ' , 'C.integer' , 'D.all of above'),
                ( 'A.=', 'B.:',  'C.==',  'D.!',),
                ("A.int' , 'B.<class'int'> , 'C.5' , 'D.error"),
                ('A.11',  'B.10', 'C.12','D.20'))

            ques_no=0
            ans =  ('A','C','D','C','B','A')
            score = 0 
            guesses = []

            for questions in ques:
                print("****************************")
                print(questions)
            for options in opt[ques_no]:
                print(options)
    

            guess=input("Enter A, B, C, D: ") 
            guesses.append(guess)
            if guess == ans[ques_no]:
                score+=1
                print("your answer is correct!")
          
                print("your score is", score)
          
            
            else:
                print("your answer is Incorrect!")   
            ques_no+=1
            print("your total score is", score,"out of 6")
            
            
        else:
            print(" sorry ! You need to accept the terms and conditions to Play !!")
    else:
        chance=0
        while chance<2:
            print("Try again! ")
            password=input("Enter password ")
            cpass=input("Confirm password ")
            if password == cpass:
                print(" Passowrd match ")
            else:
                print("Sorry! Password dont matched again !")
                chance+=1


else:
    print('Invalid User')  