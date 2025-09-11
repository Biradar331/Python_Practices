#write a program to enter marks of 3 subjects from the user and store them in the dictionary.
#start with an empty dictionary and add one by one.use subject name as key and marks as value.
marks={}

chem=int(input("enter your chemistry marks:"))
marks.update({"chem":chem})

phy=int(input("enter your chemistry marks:"))
marks.update({"physics":phy})

math=int(input("enter your chemistry marks:"))
marks.update({"mathematics":math})

print(marks)