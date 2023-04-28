para = []
print("enter your paragraph")
while True:
    line = input()
    if line:
        para.append(line)
    else:
        break
print(para)
print('\n'.join(para)) #enna o/p varanum.join(list_var)
