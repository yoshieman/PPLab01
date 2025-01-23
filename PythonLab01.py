import math


print ("problem1")
a = math.pi * 5**2

r = 3
v = (4 / 3) * math.pi * r**3

a_side = 3
b_side = 4
c_side_sq = a_side**2 + b_side**2
pyt = math.sqrt(c_side_sq)
print (a)
print (v)
print (pyt)

print ("problem 2")
first_name = "Josh"
last_name = "kohl"
full_name = first_name + " " + last_name
name_len = len(full_name)

print (full_name)
print (name_len)
print (full_name.upper())
print ( full_name.lower ())

print ("problem 3")

age = 37
height =6
heightinches = height * 12
weight = 167
print (type(age), type(height), type(weight))
bmi = (weight / heightinches**2) *703
print (bmi)