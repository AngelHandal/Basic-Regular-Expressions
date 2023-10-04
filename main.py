import re 

#PATTERN 
# 3 lowercase letters 
# 3-5 diggits
# one symbol 
# up to two uppercase characters (optional)

pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")

print(pattern.search("ahd2331#AJ"))
print(pattern.search("lll44511.k"))
print(pattern.search("lll44511."))
print(pattern.search("abc123456#JJ"))

#Regular exprssion for emails 

pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$") 

print(pattern.search("asdasda@gmail.com"))
print(pattern.search("anh12ik@gmail.comasd"))
print(pattern.search("anH123@gmail.com"))
print(pattern.search("kkkie123l@gmail.??_"))
