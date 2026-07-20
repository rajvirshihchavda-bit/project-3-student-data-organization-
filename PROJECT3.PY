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
            s_subject={subject}
            student.append({'student_id': student_id, "name": student_name, "dob": student_dob, "age": student_age, "grade": grade, "subject": s_subject})
        case 2:
            print(student, 'end=\n')
        case 3:
            update_id=int(input("Enter student id to update: "))
            found=False
            for s in student:
                if s["student_id"]==update_id:
                    student_id=int(input("Enter student id: "))
                    student_name=input("Enter student name: ")
                    student_dob=input("Enter student dob: ")
                    student_age=int(input("Enter student age: "))
                    grade=input("Enter student grade: ")
                    subject=input("Enter student subject: ")
                    s_subject={subject}
                    s.update({"student_id": student_id, "name": student_name, "dob": student_dob, "age": student_age, "grade": grade, "subject": s_subject})
                    found=True
                    break
            if not found:
                print("Student not found")
        case 4:
            delete_id=int(input("Enter student id to delete: "))
            found=False
            for s in student:
                if s["student_id"]==delete_id:
                    student.remove(s)
                    print("Student deleted successfully")
                    found=True
                    break
            if not found:
                print("Student not found")
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice")
