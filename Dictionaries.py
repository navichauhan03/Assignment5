# A Program demonstrate the functionality of Dictionaries
dict1 = {'Raman':56,'Aman':68,'Sandeep':70,'Manpreet':55}
student_name = input("Enter student name: ")
if student_name in dict1:
    print(f"{student_name} 's marks are: {dict1[student_name]}")
else:
    print(f"{student_name} doesn't exist")
print("Thanks")