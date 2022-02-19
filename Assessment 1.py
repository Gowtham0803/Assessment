#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
def Choices():
    print("Welcome")
    Choice=input("Enter 1 for Register or 2 for Login or 3 for Forgot Password: ")
    if Choice == "1":
        return Checkcredentials()
    elif Choice =="2":
        return Getcredentials()
    elif Choice =="3":
        return Getpassword()
    else:
        print("Invalid Entry")
def Checkcredentials():
    Mailid=input("Mail_ID: ")
    pat='[a-zA-z0-9#%&*_-]+@[a-zA-z0-9]+.[a-zA-z0-9]'
    if re.match(pat,Mailid):
        Password=input("Password: ")
        length=len(Password)
        pat='[A-Z]+[a-z]+[@#%$*&_-]+[0-9]'
        if (length>=5) and (length<=16):
            if re.match(pat,Password):
                file = open("User_Data.txt",'r')
                Res = file.read()
                if Mailid in Res:
                    return "Email Already Exists. Please Try Login"
                file.close()
                file = open("User_Data.txt",'w')
                Res = Res + " " + Mailid + " " + Password
                file.write(Res)
            else:
                print("Invalid Entry.Try Again")
        else:
            print("Invalid Entry.Try Again")
    else:
        print("Invalid Entry.Try Again")
        
def Getcredentials():
    print("Enter vaild Mail ID and Password")
    Mailid=input("Mail_ID: ")
    Password=input("Password: ")
    file = open("User_Data.txt",'r')
    Res = file.read()
    Res = Res.split()
    if Mailid in Res:
        index = Res.index(Mailid) + 1
        usr_password = Res[index]
        if usr_password == Password:
            return "Welcome Back, " + Mailid
        else:
            return "Password entered is wrong"
    else:
        print("Details not found. Please Sign Up.")
        return Checkcredentials()

def Getpassword():
    Mailid=input("Enter Mail ID: ")
    file = open("User_Data.txt",'r')
    Res = file.read()
    Res = Res.split()
    if Mailid in Res:
        index = Res.index(Mailid) + 1
        usr_password = Res[index]
        print("Password: ",usr_password)
        print("Success")  
    else:
        print("Mail ID not available. Try Register ")
        return Checkcredentials()
      
print(Choices()) 

