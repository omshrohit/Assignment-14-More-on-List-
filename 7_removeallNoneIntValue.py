# write  a python script to remeove all non  int value from the list
list=[1,1.2,True,3+4j,"Python",10,20,23.34,"Javascript"]
list2=[e for e in  list if  type(e)==int]
print(list2)