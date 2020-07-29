import pymongo
from pymongo import MongoClient

#################
client = MongoClient('mongodb+srv://nexxon028:1234@cluster0.ejxgy.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = client['loginsystem_db']        
coll = db['users_list']
#################

#--------------------------------------------------------------------------------

class User(): # class for login/create  profile
    
    global coll

    def __init__(self):
        pass
    

    def LogIn(self, post):
        check = coll.find_one(post)
        if check == None:
            return False;
        else:
            return True;

    def SignUp(self):
        check = self.coll.find_one(post)




#--------------------------------------------------------------------------------







