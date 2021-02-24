import re

# ====predefined character=====

# pattern="\s"     #space
# pattern="\d"     #0-9
# pattern="\D"     #^0-9
# pattern="\w"      #a-zA-Z0-9 all
pattern="\W"


matcher=re.finditer(pattern,"abc _Z4K@")

for match in matcher:
    print(match.start())
    print(match.group())