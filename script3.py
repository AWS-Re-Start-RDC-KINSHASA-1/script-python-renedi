import os
def new_user():
    confirm="N"
    while confirm !="Y":
        username = input("indiquez le nom de l'utilisateur à ajouter: ")
        print("utliser username '" +username + "'? (Y/N)")
        confirm = input().upper()
        os.system("sudo adduser " + username)
        
new_user()   
