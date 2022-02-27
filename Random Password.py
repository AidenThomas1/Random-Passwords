#Subscribe to Aiden Thomas 
#Check out My Website - https://io.aidens.in/

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]{}#()*; ._-"

all = lower + upper + number + symbol

length = 15
password = "".join(random. sample (all,length))
print(" The Password You Generated is :",password)