# write a python script to print   indices of all occurrences of a given elements in a given list.

my_list=[1,2,4,2,1,2,5]
n=2
j=0
list=[]
for i in my_list:
    if  n==i:
        list.append(j)
        j+=1
    else:
        j+=1
print("occurrences of {} are {}".format(n,list))
