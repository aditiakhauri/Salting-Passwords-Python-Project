from hashlib import*
import hashlib

from salting_algo import*


def  hash_salt(username,password):

    # username="anu2dude" 
    # password="thisis password";

    salt=salting(username,password);


    new_pass=password+salt;

    hash_pass= hashlib.sha256(new_pass.encode())

    return hash_pass.hexdigest();
    






