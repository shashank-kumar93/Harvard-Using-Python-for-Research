import string
import pandas as pd
import numpy as np



#Exercise1

alph = list(alphabet)
num = [i for i in range (0,27)]
positions = dict(zip(alph,num))
alphabet = " " + string.ascii_lowercase

#Exercise2

positions = {}
ind = 0
for ch in alphabet:
    positions[ch] = index
    ind += 1

#Exercise3
    
message = "hi my name is caesar"

res = ''.join([alphabet[i] for i in [(positions[message[j]]+1)%27 for j in range(len(message))]])

#Exercise4

key = 3
res = ''.join([alphabet[i] for i in [(positions[message[j]]+key)%27 for j in range(len(message))]])

#Exercise5
	 
message = "klcpacqdphclvcfdhvdu"

key = -3
res = ''.join([alphabet[i] for i in [(positions[message[j]]+key)%27 for j in range(len(message))]])
