#LIST OPERATIONS

l = [1,2,3,4,5]

#append
l.append([6,7])
print(l)

#extend
l.extend([6,7])
print(l)

#copy
li = l # this is the same list but into new variable changes made will reflect in both of them
li.append(8)
print(li)
print(l)
li1= l.copy() #this is replica of list l
li1.append(8)
print(li1)
print(l)

#clear
li.clear()
print(li)

#count
lst = [1,2,3,2,4,2,1,3,6,3,2,4]
print(lst.count(2))

#index()
print(lst.index(2)) # prints the index of a particulare element

#insert
lst.insert(0,9)
print(lst)

#pop
lst.pop(2) # it delete the element at particular index
print(lst)
#remove
lst.remove(3) # it removes the particular element
print(lst)
#reverse
lst.reverse()# it print alll the elements in the reverse order
print(lst)
#sort
lst.sort()#it prints the elements in ascending order
print(lst)

lst.sort(reverse=True)# it prints the descending order
print(lst)

