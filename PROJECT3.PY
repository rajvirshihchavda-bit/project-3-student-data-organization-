print("Welcome to Student Data Organizer")

student = []

while True:

    choose = int(input("""
1. Add Student
2. Show Student
3. Update Student
4. Delete Student
5. Exit

Enter Choice: """))

    match choose:

        # Add Student
        case 1:
            student_id = int(input("Enter Student ID : "))
            student_name = input("Enter Student Name : ")
            student_dob = input("Enter Student DOB : ")
            student_age = int(input("Enter Student Age : "))
            grade = input("Enter Student Grade : ")
            subject = input("Enter Student Subject : ")

            student.append({
                "student_id": student_id,
                "name": student_name,
                "dob": student_dob,
                "age": student_age,
                "grade": grade,
                "subject": {subject}
            })

            print("Student Added Successfully.")

        # Show Student
        case 2:

            if len(student) == 0:
                print("No Student Found.")

            else:
                print("\nStudent Details\n")

                for s in student:
                    print("Student ID :", s["student_id"])
                    print("Name       :", s["name"])
                    print("DOB        :", s["dob"])
                    print("Age        :", s["age"])
                    print("Grade      :", s["grade"])
                    print("Subject    :", s["subject"])
                    print("-" * 30)

        # Update Student
        case 3:

            update_id = int(input("Enter Student ID to Update : "))

            found = False

            for s in student:

                if s["student_id"] == update_id:

                    s["name"] = input("Enter New Name : ")
                    s["dob"] = input("Enter New DOB : ")
                    s["age"] = int(input("Enter New Age : "))
                    s["grade"] = input("Enter New Grade : ")
                    s["subject"] = {input("Enter New Subject : ")}

                    found = True
                    print("Student Updated Successfully.")
                    break

            if found == False:
                print("Student Not Found.")

        # Delete Student
        case 4:

            delete_id = int(input("Enter Student ID to Delete : "))

            found = False

            for s in student:

                if s["student_id"] == delete_id:
                    student.remove(s)
                    found = True
                    print("Student Deleted Successfully.")
                    break

            if found == False:
                print("Student Not Found.")

        # Exit
        case 5:
            print("Thank You...")
            break

        # Invalid Choice
        case _:
            print("Invalid Choice")
