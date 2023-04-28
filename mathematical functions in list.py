s = [1,10,20,30,22,55,12,32]
print("length",len(s)) #determine the length of the list
print(s)
s.sort() #sort() arranges the list in ascending order
print("in ascending order:",s) 
s.sort(reverse=True) #in the descending order
print("descending order:",s)
s = ["shif","standford"]
s.sort(key=len)
print("s after sorting with len",s)
print(max(s)) #returns the max value in the list
print(min(s)) #returns the min value in the list
s.clear()
s.extend([1,2])
print("now the s is:",s)
print(sum(s))