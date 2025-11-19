#name = "David"
#print(name)

#decimal = 3.142
#print(decimal)

#boolean = True
#print(boolean)

#interger = 42
#print(interger)

#Num1 = 100
#Num2 = 60

#sum = Num1 == Num2
#print(sum)

#student_name = ["David", "Amake", "Kisha"]
#print(student_name[2])

#courses = ("Math", "Science", "History")
#print(courses)

#student_lastname = {"John", "Dafe", "Victor", "Johnson",}
#print(len(student_lastname))
 

#car = {
    #"color": "Red",
    #"model": "Toyota",
    #"year": 2020
 
# Print (car["model"])
#print (car)


#def send_message(user):
    #print("Hello " + user + ", Welcome to your dashboard,")

    #send_message("David")
    #send_message("Emma")
    #send_message("John")
    #send_message("Dafe")

    #send message()



# def send_welcome_email(user):

#     print("Welcome,", user + " Welcome to your dashboard.")

# send_welcome_email("John")
# send_welcome_email("David")
# send_welcome_email("Divine")


# Assigment on Creating a python Directory
student = {
    "student1": {"name": "Dafe", "age": 15, "grade": "A"},
    "student2": {"name": "Kish", "age": 16, "grade": "B"},
    "student3": {"name": "Akomaye", "age": 17, "grade": "C"}
}
# print all student records
for Key, record in student.items():
    print(f"{Key}: {record}")
