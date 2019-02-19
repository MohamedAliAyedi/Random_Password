import string
from random import *
print("\tCreate Random Password By : Mohamed Ali Ayedi")
long=input("Length of Password >> ")
char =  string.digits + string.ascii_letters
passw = "".join(choice(char) for x in range(randint(long,long)))
print "random Password > "+passw
