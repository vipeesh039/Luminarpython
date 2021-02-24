import re

rule="[K][L]\d{2}[A-Z]{2}\d{4}"

var_name=input("enter variable name")

matcher=re.fullmatch(rule,var_name)
if matcher==None:
    print("invalid variable")
else:
    print("valid variable name")