from tkinter import *
import pymongo
from pymongo import MongoClient
import back


class User_Window():
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.name = None
        self.username_label = Label(self.root, text=f'{LogIn_Window.name}', font='20', fg='black', bg='#d1d3de')
        self.quit_button = Button(self.root, text='Log Out', fg='red', command=self.log_out)
        self.root.geometry('500x250')
        self.root.title(f'Profile: {LogIn_Window.name}')
        self.root.wm_attributes('-alpha', 0.9)
        self.root['bg'] = '#d1d3de'
        self.root.iconbitmap(r'D:\Python\my_projects\Login-System\icon.ico')
        self.quit_button.place(x=440, y=10)
        self.username_label.pack()
        self.root.mainloop()

    def log_out(self, window):
        self.root.destroy()
        window.withdraw()


# sadboy123
# qwerty123   

    
class LogIn_Window(User_Window):
    def __init__(self, root=None, name='s'):
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.window.geometry('500x250')
        self.window.title('Login System 2.0')
        self.window.wm_attributes('-alpha', 0.9)
        self.window['bg'] = '#d1d3de'
        self.window.iconbitmap(r'D:\Python\my_projects\Login-System\icon.ico')
        self.text_login = Label(text='Login', font='20', fg='black', bg='#d1d3de')
        self.login = Entry(self.window, font='Consolas 15', relief='solid', justify='center')
        self.text_password = Label(text='Password', font='20', fg='black', bg='#d1d3de')
        self.password = Entry(self.window, font='Consolas 15', relief='solid', justify='center', show='*')
        self.login_button = Button(text='Log in', font='Consolas 13', relief = 'solid', command=self.Log_In)
        self.signUp_button = Button(text='SignUp', font='Consolas 13', relief = 'solid', command=self.Sign_Up)
        self.messageToSignUp = Label(text='Account is not defined\nSign Up, pls!')
        self.text_login.pack()
        self.login.pack()
        self.text_password.pack()
        self.password.pack()
        self.login_button.place(x=170, y=120)
        self.signUp_button.place(x=260, y=120)
        self.window.mainloop()

    def Log_In(self): # Login to profile
        L = self.login.get() # Login 
        P = self.password.get() # Password

        # set username 
        global name
        ##-----------------------------------
        
        post = {"user_login": L, "password": P} # Post for database search
        name = post["user_login"] 
        if back.User.LogIn(post, post) == False: 
            return self.messageToSignUp.place(x=185, y=160)
            
        if back.User.LogIn(post, post) == True:
            self.window.withdraw()
            User_Window.name = L
            return super().__init__()

    def Sign_Up(self):
        L = self.login.get() # Login 
        P = self.password.get() # Password

        ##-----------------------------------
        post = {"user_login": L, "password": P} # Post for database 
        check = back.coll.find_one(post)
        if check is None and len(L + P) >= 2: # if login and password not in db, create profile
            back.coll.insert_one(post)
            return super().__init__()
        else: 
            pass



