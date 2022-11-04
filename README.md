# Salting-Passwords-Python-Project
Note slating and salting_algo are 2 diffrent files.





signup process

interfaceFile-takes the input and and makes the interface and returns the username and password which is input

login->logs in which means compares the credentials used and the credentials stored

phish_check->location and email requirment for  logining in is cheked here



Result_firing->used to fire the result-another interface ->Fires Accepted or denied


Saltin_algo-> computes a salt for a given set of password and username  used whlile login and  singup


signup->file is used to sign up  calls the interface file  from where is gets the detials and then it is fedup to the database;

slating->adds salt and password and then does sha256 encryption 
