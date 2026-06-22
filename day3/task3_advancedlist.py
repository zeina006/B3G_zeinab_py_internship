n=[15,50,11,40,35,77,50,11,95,99,79,65,6,53,6]

unique_order=[]

for n1 in n:
    if n1 not in unique_order:
        unique_order.append(n1)
print("Original Values:",n)
print("After removing Duplicate values list:",unique_order)