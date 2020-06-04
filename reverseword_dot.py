import re
str1=input("Enter the String:")
string=re.sub(" ",".",str1)
print("String:",string)
word=string.split(".")
reverse=word[::-1]
dot="."
print(dot.join(reverse))

