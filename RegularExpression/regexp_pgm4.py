import re

# pattern="a"
# pattern="a+"
# pattern="a*"      #any number
# pattern='a{2}'    #two group
# pattern="a{2,3}"  #min two max three

matcher=re.finditer(pattern,"aaaaaaabaaaabaabb")

for match in matcher:
    print(match.start())
    print(match.group())