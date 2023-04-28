"""
------Methods------
remove(element) - removes the specific element
pop() - removes the final element and pass into var
pop(index) - removes a specific index and pass into var
list_var.clear() - clears all the elements in the list
del list_var - deletes the entire list
del list_var[index] - deletes a specific index
"""
s = ["sun",100000,True,22.2,3]
s.remove(22.2) #var.remove(element)
print(s)
s.extend([1,2,34,33,5,54])
print("now the var s is",s)
a=s.pop() # removes the last element a assigns to var
print(a)
print("now the var s is",s)
a = s.pop(3) #var = var.pop(index)
print(a)
print("now the var s is",s)
s.clear()
print(s) #empty list
s= ["sun",100000,True,22.2,3]
print("recreated the list",s)
print("Deleting....")
del s[0]
print(s)
del s
print(s) #error bcs whole list deleted