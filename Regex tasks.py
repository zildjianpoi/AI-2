import sys

idx = int(sys.argv[1])-41
myRegexList = [
   "/^[.xo]{64}$/i", 
   "/^[xo]*\.[xo]*$/i", 
   "/^(x+o*)?\.|\.(o*x+)?$/i", 
   "/^(..)*.$/s", 
   "/^(0([01]{2})*|1([01]{2})*[01])$/", 
   "/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i", 
   "/^(1?0)*1*$/", 
   "/^([bc]*a[bc]*|[bc]+)$/", 
   "/^((([bc]*a){2})+[bc]*|[bc]+)$/",
   "/^(((20*)*1){2})+|2)[02]*)$/",
   
   "/\w*(\w)\w*\1\w*/i",
   "/\w*(\w)(\w*\1){3}\w*/",
   "/^([01])[01]*\1$/",
   "/\b(?=\w*cat)\w{6}\b/i",
   "/\b(?=\w*bri)(?=\w*ing)\w{5,9}\b/i",
   "/\b((?!cat)\w){6}\b/",
   "/\b((\w)(?!\w*\2))*/i",
   "/^((?!10011)[01])*$/",
   "/\w*([aeiou])(?!\1)[aeiou]\w*/i",
   "/^(?!.*1[01]1)[01]*$/",
   
   "",
   "",
   "",
   "",
   "",
   "",
   "",
   "",
   "",
   "",
   
   "/^(?=(.)+(.*\\1){3})\w{,6}$/im", #1 24
   "/^(?=(.*([aeiou])(?!.*\\2)){5})\w{,8}$/im",
   "/(?=([^aeiou]*[aeiou]){5}[^aeiou]*$).{18,}/im", #3   41
   "/^(.)(.)(.).{6,}\\3\\2\\1$/im", #4    22
   "/(?=.*(.)(\\1){1}).{22,}/i", #5      21
   #"/(?=(.)+(.*\\1){5,})\w{14,}/i", #6    25 **19
   "/(\w)+(\w*\\1){5,}/",
   "/(?=(.*(.)\\2){3})\w{14,}/i", #7     24
   "//i", #8 none
   "//i", #9 none
   "/^((\w)(?!(.*?\\2){2,})){18,}/im" #10 27 ch 234
   
   ]
print(myRegexList[idx])

#228>217>189