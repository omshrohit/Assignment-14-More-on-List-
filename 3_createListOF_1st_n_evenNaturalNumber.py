# write  a  python script to create a list of first N even natural numbsers
num=int(input("enter the number"))
list=[e for e in range(2,num*2+1,2)]
print(list)