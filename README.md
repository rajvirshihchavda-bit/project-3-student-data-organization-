# Student Data Organizer

A simple Python-based command-line application for managing student records. This project allows users to add, view, update, and delete student information through an interactive menu-driven interface.

## Features

* Add new student records
* View all stored student records
* Update existing student information
* Delete student records
* Menu-driven command-line interface
* Data stored using Python data structures (lists, dictionaries, and sets)

## Technologies Used

* Python 3
* Lists
* Dictionaries
* Sets
* Match-Case Statements (Python 3.10+)

## Project Structure

```text
Student-Data-Organizer/
│
├── student_data_organizer.py
├── README.md
└── requirements.txt (optional)
```

## How It Works

The application provides the following options:

1. **Add Student**

   * Student ID
   * Name
   * Date of Birth
   * Age
   * Grade
   * Subject

2. **Show Students**

   * Displays all student records currently stored in the system.

3. **Update Student**

   * Search a student using Student ID.
   * Modify student details.

4. **Delete Student**

   * Remove a student record using Student ID.

5. **Exit**

   * Close the application.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/student-data-organizer.git
```

2. Navigate to the project directory:

```bash
cd student-data-organizer
```

3. Run the program:

```bash
python student_data_organizer.py
```

## Sample Output

```text
Welcome to Student Data Organizer

1. Add Student
2. Show Students
3. Update Student
4. Delete Student
5. Exit

Enter choice: 1

Enter student ID: 101
Enter student name: John Doe
Enter student DOB: 15-05-2005
Enter student age: 19
Enter student grade: A
Enter student subject: Mathematics

Student added successfully!
```

## Learning Objectives

This project helps beginners understand:

* CRUD Operations (Create, Read, Update, Delete)
* Python Lists and Dictionaries
* Data Management in Python
* User Input Handling
* Looping and Conditional Statements
* Match-Case Syntax

## Future Improvements

* Store data permanently using files or databases
* Search students by name or grade
* Multiple subject support
* Input validation
* Graphical User Interface (GUI)
* Export records to CSV or Excel

## Author

Developed by** Rajveersinh**

## License

This project is open-source and available under the MIT License.
