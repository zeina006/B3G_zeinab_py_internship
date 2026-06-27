e={"Riya":5000,"zeinab":6000,"John":7000,"malek":8000}
sorted_e=sorted(e.items(),key=lambda x:x[1],reverse=True)
for name,salary in sorted_e[:3]:
    print(name,salary)