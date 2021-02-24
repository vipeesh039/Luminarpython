import re

#===predefined character set=====
#pattern='[abc]'    #just checking matches a b c and position
#pattern='[a-z]'    #only lower a to z
#pattern='[A-Z]'    #only upper A to Z
#pattern='[a-zA-Z]'  #both lower & upp a to z
#pattern='[0-9]'
#pattern='[a-zA-Z0-9]'
pattern='[^a-zA-Z0-9]'


matcher=re.finditer(pattern,"abc _Z4K@")

for match in matcher:
    print(match.start())
    print(match.group())
