import sys, re

file = open("wordsC.txt")
dic = ''.join(file.readlines())


#Example 3: Find the longest word where no vowel appears more than twice.
#pattern = r'^(?!.*([aeiou])(\w*\1){2})\w{19,}'
pattern = r'^(?=[^a]*a(?!\w*a))(?=[^e]*e(?!\w*e))(?=[^i]*i(?!\w*i))(?=[^o]*o(?!\w*o))(?=[^u]*u(?!\w*u))\w{15,}$'
regex = re.compile(pattern, re.M|re.I)
re_list = [dic[m.start():m.end()] for m in regex.finditer(dic)]
print (re_list)

patternlist = [
   "/^(?=.*(.)(.*\1){3}).{,6}$/i", #1
   "/^(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u){,8}$/i", #2
   "/(?=([^aeiou]*[aeiou]){5}[^aeiou]*$).{19,}/i", #3  
   "/^(.)(.)(.).{6,}\3\2\1$/i", #4
   "/(?=.*(.)(\1){1,}){20,}/i", #5
   "/(?=.*(.)(.*\1){4,}).{20,}/i", #6
   "/(?=.*((.)\2.*){2,}).{17,}/i", #7
   "//i", #8 none
   "//i", #9 none
   "/((.)(?!(.*\2){2,})){19,}/i", #10
   ]


