# main_script.py

from employee_management import *

# Example usage
if __name__ == "__main__":
    register_employee()
    class Mentor:
        def __init__(self, mentor_id, name, designation, department, employee_ids):
            self.mentor_id = mentor_id
            self.name = name
            self.designation = designation
            self.department = department
            self.employee_ids = employee_ids
class Employee:
    def __init__(self, employee_id, name, designation, department, password, goals):
        self.employee_id = employee_id
        self.name = name
        self.designation = designation
        self.department = department
        self.password = password
        self.goals = goals
class Course:
    def __init__(self, course_id, course_name, department, goals):
        self.course_id = course_id
        self.course_name = course_name
        self.department = department
        self.goals = goals        

    user_id = int(input("Enter your employee ID for further options: "))
    password = input("Enter your password: ")
    employee = employee_login(user_id, password)

    if employee:
        print(f"Welcome, {employee.name}!")

        while True:
            print("\nOptions:")
            print("1. View Employee Goals")
            print("2. View Recommended Courses")
            print("3. View Matched Mentor")
            print("4. View Course Details")
            print("5. delete employee record")
            print("6. Exit")# Added option
           
            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                view_employee_goals(user_id)
            elif choice == '2':
                view_employee_courses(user_id)
            elif choice == '3':
                view_employee_motivation(user_id)
            elif choice == '4':  # Added option to view course details
                course_id = int(input("Enter the Course ID: "))
                view_course_details(course_id,user_id)
            elif choice=='5':
                 delete_employee(user_id)
                 
            elif choice == '6':
                print("Exiting the program. Goodbye!")
                break
           
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
    else:
        print("Invalid employee ID or password. Exiting.")


