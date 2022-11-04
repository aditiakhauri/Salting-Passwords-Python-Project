
import mysql.connector as pl
from interface import*

from login import*
from signup import*


from  phish_check import*;

plq=pl.connect(host="localhost",database="cyber",user="root",password="ram123")
# Username=input("Enter the use name")
# Pass=input("Enter the pass");







location_given="vellore"
given_email="rahul@gmail.com"

# sign_up();# sign_up into the system

login();   # login into the system



# mycursor = plq.cursor()

# mycursor.execute("Select * from password")

# res=mycursor.fetchall();

# print(res[0][0])


