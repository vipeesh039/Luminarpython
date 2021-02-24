import re

rule="[a-k][369][a-zA-z]*"     #RULE start a-k second one digit and divisible by 3 next ant character

var_name=input("enter variable name")

matcher=re.fullmatch(rule,var_name)
if matcher==None:
    print("invalid variable")
else:
    print("valid variable name")