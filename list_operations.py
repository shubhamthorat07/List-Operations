l2 = [100,200,300]
print(id(l2))
l2.append([400,500])
print(l2)



l2.extend([600,700,"Python"])
print(l2)
print(l2[-1])


l2.insert(2,1000)
print(l2)




l3 = [1,2,3,4,5]
print(id(l3))
l3[3] = 300
print(l3) 
print(id(l3))
l3.append(6)
print(l3)





l4 = [100,200,300,400]
r = l4.pop()
print(l4,r)




l4.remove(300)
print(l4)



l4.clear()
print(l4)



l5 = [6,3,5,7,1,9,2]
print(l5[::2])
l5.sort()
print(l5)
print(l5[::2])

l5.reverse()
print(l5)


l6 = ["Python", "Java", "Html", "Python"]

print(l6.count("Python"))

print(l5 + l6)

print("Python " * 5)

