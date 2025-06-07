# Assignment5
Dictionaries and List
# A Program demonstrate the functionality of Dictionaries
dict1 = {'Raman':56,'Aman':68,'Sandeep':70,'Manpreet':55}
student_name = input("Enter student name: ")
if student_name in dict1:
    print(f"{student_name} 's marks are: {dict1[student_name]}")
else:
    print(f"{student_name} doesn't exist")
print("Thanks")

# A program for list items, extracted and reversed items
list = [1,2,3,4,5,6,7,8,9,10]
print('Original List: ',list)
print('Extracted List: ',list[2:6]) # Slice the list
list1 = list[2:6]
list1.reverse() # for reverse the list
print('Reversed Extracted List: ',list1)

