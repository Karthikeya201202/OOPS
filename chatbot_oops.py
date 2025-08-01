'''
We are craeting a class to implement our learnings of OOPS
Following are implemented in this file
1. Class, objects
2. Encapsulation- get and set methods
3. understading of "self" keyword
4. Inheritance - MRO, Method Overriding
5. Polymorshipsm-> Duck typing, Operator overloading, Method overriding, Functional Polymorpism
'''
import sys
class Chatbot:
    login=False
    user_name='' # Class variables
    user_pwd=''
    def __init__(self):
        self.user_input=input("""
                              1. Enter 1 to signup
                              2. Enter 2 to signin
                              3. Enter 3 to post
                              4. Enter 4 to send a message to a friend
                              5. Enter any key to exit
                              
                              """)
        if self.user_input=="1":
            self.signup()
        elif self.user_input=="2":
            self.signin()
        elif self.user_input=="3":
            self.create_post()
        elif self.user_input=="4":
            friend_name=input("Enter friend name")
            self.send_message(friend_name)
        else:
            sys.exit()
        self.__init__()
    def signup(self):
        Chatbot.user_name=input("Enter User name")
        Chatbot.user_pwd=input("Enter Password")
        print("Sign up successful")
    
    def signin(self):
        self.name=input("Enter Username")
        self.pwd=input("Enter Password")
        if self.user_name!="":
            if (self.name==Chatbot.user_name) &(self.pwd==Chatbot.user_pwd):
                Chatbot.login=True
                print("Sign in sucessful")
            else:
                print("User doesn't exit")
            
        else: 
            print("Account is not created! Signup first")
    def create_post(self):
        if Chatbot.login:
            self.post=input("Enter the text to post")
            print("Posted sucessfully!")
        else:
            print("User has to sign in first to create a post")
    def send_message(self,friend_name):
        if Chatbot.login:
            self.friend_name=friend_name
            self.message=input("Enter Message")
            print(f"Message sent to {friend_name}")
        else:
            print("User has to sign in first to send a message")
    
    @staticmethod
    def version():
        print("Current system version is 5.0")

# obj1=Chatbot()
Chatbot.version()
    
            
        
        