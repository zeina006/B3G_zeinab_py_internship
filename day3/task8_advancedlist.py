s=[]

s.append(("Riya",88))
s.append(("Aman",90))
s.append(("Zeinab",99))
s.append(("Sara",72))
s.append(("Ali",85))

print("Before Removing:",s)
for s1 in s:
    print("=",s)

s.remove(("Sara",72))
s.remove(("Zeinab",99))

for s in s:
    print("After removing:",s)