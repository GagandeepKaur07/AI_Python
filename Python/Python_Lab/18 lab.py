a=10
b=8
c=7

#AND
res = (a<b) and (b<c)
print(res)

#OR
res1 = (a<b) or (b<c)
print(res1)

# NOT
res2 = not (b>a)
print(res2)

#concate
str1="hello"
str2="world"
str3="python"

A= (str1=="hello") and (str2 == "world")
print(A)

R= (str1=="hello") or (str3 == "python")
print(R)

N= not (str1=="world")
print(N)
