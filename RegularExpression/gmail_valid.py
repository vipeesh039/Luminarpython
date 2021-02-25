import re

rule="\w+[@]gmail.com"

var_name=input("enter gmail id")

matcher=re.fullmatch(rule,var_name)
if matcher==None:
    print("invalid variable")
else:
    print("valid")