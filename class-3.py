
#/ If Else (control flow)

num = 10

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero") #/ (output:positive number)
    
##Nested if statements

age = 20

if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are a young adult.")
else:
    print("You are a minor")
    
## The output (You are an adult.)
## (You are a young adult.)    

#/  for loop

for a in range(7):
    print("Iteration:", a)
#/ (output : 0,1,2,3,4,5,6)

#/  while loop

count = 1
while count <= 5:
    print("Count:", count)
    count += 1
#/ (output : count:1, count:2, count:3, count:4, count:5)

#/ Nested Loops

for a in range(1, 4):
    for b in range(1, 4):
        print(f"a={a}, b={b}")

#/  Loop with else

for c in range(3):
    print(c)
else:
    print("Loop finished")
#/ (output : 0,1,2,Loop finished )

#/  Break Statement (Loop Control)

for j in range(5):
    if j == 3:
        break
    print(j)
#/ (output : 0,1,2)

#/ List 

names = ["sumbul", "anusha", "ifra"]
names.append("aiman")  # Adding an item
print(names)  # Output: ['sumbul', 'anusha', 'ifra', 'aiman']

#/ Tuple

colors = ("yellow", "purple", "grey")
print(colors[1])  # Output: purple

#/  Dictionary

student = {
    "name": "Anusha",
    "age": 21,
    "course": "Python"
}
student["age"] = 22  # Updating value
print(student["name"])  # Output: Anusha
print (student["age"])  # output : 22

 #/ set (Mutable)(unordered collection of unique elements)
 #/ creating a set 

my_set={4,5,6}
print(my_set)

#/ add number
my_set.add(7)
print (my_set)

#/ remove number
my_set.remove(5)
print(my_set)

## The Frozen set
## (Immutable)(unordered collection of unique elements)
## (cannot be changed after creation)(unique elements)
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)
# Output: frozenset({1, 2, 3, 4, 5})

# Frozen set methods
frozenset()
 # union() do sets ka milana
 # intersection() common elements
 # difference() ek set se dusre set ki elemnts ko hataana
 # issubset() kya ek set doosre ka subset hai
 # issuperset() kya ek set doosre ka superset hai
