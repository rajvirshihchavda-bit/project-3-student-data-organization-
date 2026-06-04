print("Welcome to student data organizer")
student=[]
while True:
    choose=int(input("1. Add student\n2. Show student\n3. Update student\n4.delete student\n5. Exit\n"))
    match choose:
        case 1:
                student_id=int(input("Enter student id: "))
                student_name=input("Enter student name: ")
                student_dob=input("Enter student dob: ")  
                student_age=int(input("Enter student age: "))
                grade=input("Enter student grade: ")
                subject=input("Enter student subject: ")
                id_dob=(student_id,student_dob)
                s_subject={subject}
                student.append({'student_id': student_id, "name": student_name, "dob": student_dob, "age": student_age, "grade": grade, "subject": s_subject})
        case 2:          
             print(student)
        case 3:
            update_id=int(input("Enter student id to update: "))
            if update_id in student:
                student_id=int(input("Enter student id: "))
                student_name=input("Enter student name: ")
                student_dob=input("Enter student dob: ")  
                student_age=int(input("Enter student age: "))
                grade=input("Enter student grade: ")
                subject=input("Enter student subject: ")
                s_subject={subject}
                student[update_id]={"name": student_name, "dob": student_dob, "age": student_age, "grade": grade, "subject": s_subject}
            else:
                print("Student not found")   
        case 4:
            delete_id=int(input("Enter student id to delete: "))
            if delete_id in student:
                del student[delete_id]
                print("Student deleted successfully")
            else:
                print("Student not found")   
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice")