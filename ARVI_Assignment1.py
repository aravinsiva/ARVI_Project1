#Random Password Generator

import string
import random


special=['-','|','@','.',',','?','/','!','~','#','%','^','&','*','(',')','{','}','[',']']

x= random.randint(10,20)
y= random.randint(0,len(special))

final_string=''

for i in range (x):
    final_string=final_string+random.choice(string.ascii_letters+string.digits+special[y])
    

print final_string
