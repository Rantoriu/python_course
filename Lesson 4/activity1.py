lst=['Orange','Apple','Grapefruit','Pineapple']
print("lenght of the list: ",len(lst))
print("the first element of the list: ",lst[0])
print("the second element of the list: ",lst[1])
print("the third element of the list: ",lst[2])
print("the last element of the list: ",lst[-1])
lst.remove('Apple')
print("after rmoving Apple: ",lst)
lst.reverse()
print("reversed list",lst)
lst=lst[0:2]
print("slice list: ",lst)
