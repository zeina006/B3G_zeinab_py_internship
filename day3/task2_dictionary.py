students=[
        {"name":"Zeinab Malek","marks":100},
        { "name":"Ilma","marks":90},
        {"name":"Riya","marks":80}
        ]
top=students[0]
for student in students:
    if student["marks"]>top["marks"]:
        top=student
print("Topper Name is:",top["name"])
print("Marks:",top["marks"])