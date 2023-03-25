# write a python script to print distincnelementsalong with their frequency in this list
l=[1,2,3,1,5,6,3,6,6]
dict1={}
for item in l:
    if (item in  dict1):
        dict1[item]+=1
    else:
        dict1[item]=1
print(dict1)