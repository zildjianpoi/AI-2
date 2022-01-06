# Name:       Date:         Version:
# Teacher:        Period:
import sys
idx = int(sys.argv[1])-31
myRegexList = [
   "Junk", 
   "/Junk", 
   "Junk/y", 
   "\\bJunk", 
   r"\bJunk", 
   "", 
   "", 
   "",
   "", 
   ""
   ]
print(myRegexList[idx])

#Hint for how to write each RegEx
#Sample answer to check a string is 'a': "/^a$/"
#Sample answer to check each line start with a word character: "/^\\w/m"

'''
X means syntax error
E means script error
T means time out
M means missing
D means no trailing /
O means bad option
I means invalid regular expression
P means shouldn't be doing this
N means internal error
r'\ makes no \\
'''
