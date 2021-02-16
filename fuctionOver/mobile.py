

mobilename=input("enter mobile name")
spec=input("enter specification")
if mobilename in mobile:
    print(mobles[mobilename]["price"])
    if spec in mobiles[mobilename]:
        print(mobiles[mobilename][spec])