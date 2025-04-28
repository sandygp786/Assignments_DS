students ={
    "Alice" : 85,
    "Matt" :  70,
    "Marie" : 83
}

name = input("Enter the student's name :")
if name in students:
    marks = students[name]
#    print("{}'s marks: {:.2f}".format(name,marks))
    print("{}'s marks: {}".format(name, marks))
else:
    print("Student Not Found.")