str1='''If you trouble the trouble ,trouble will trouble you.
I am not the trouble ,I am the truth ---by JAI Ballaya@9999'''

lower=str1.lower()
print(lower)
capitalize=str1.capitalize()
print(capitalize)
print(str1.title())
#upper=str1.upper()
#print(upper)

print(str1.islower())
print(str1.islower())
print(str1.isalnum())
print("dhbhsbhhIDJSKHS".isalnum())
print("23784638".isdigit())
print(str1.count("trouble"))

print(str1)
#strip functions
#print(str1.strip())
#print(str1.lstrip())
#print(str1.rstrip())

#split
word=str1.split()
print(word)
print(len(word))

#join
combined_string=" ".join(word)
print(combined_string)

#string indexing
name="tharuny"
print(name[2])

#string slicing
s1="python"
s1=s1[0:6:2]
print(s1)






