# employee_management.py

class Mentor:
    def __init__(self, mentor_id, name, designation, department, employee_ids):
        self.mentor_id = mentor_id
        self.name = name
        self.designation = designation
        self.department = department
        self.employee_ids = employee_ids

    def is_matched(self, employee):
        return employee.employee_id in self.employee_ids

class Course:
    def __init__(self, course_id,
                 course_name, department, goals):
        self.course_id = course_id
        self.course_name = course_name
        self.department = department
        self.goals = goals

    def is_recommended(self, employee):
        return self.department == employee.department  # Simple recommendation logic based on department

class Employee:
    def __init__(self, employee_id, name, designation, department, password, goals):
        self.employee_id = employee_id
        self.name = name
        self.designation = designation
        self.department = department
        self.password = password
        self.goals = goals

employee_db =  {
    1: {'employee_id': 1001, 'name': 'sinchana', 'designation': 'Developer', 'department': 'IT', 'password': '7103', 'goals': 'Learn Python'},
    2: {'employee_id': 1002, 'name': 'ayman', 'designation': 'Manager', 'department': 'HR', 'password': '1371', 'goals': 'Leadership'},
    3: {'employee_id': 1003, 'name': 'supritha', 'designation':'developer','department':'IT','password':'8503','goals':'web development'},
    4: {'employee_id': 1004, 'name': 'sreevalli', 'designation':'senior manager','department':'IT','password':'8123','goals':'object oriented concepts'},
    
}
mentor_db = {
    1: {'mentor_id': 1, 'name': 'Mentor1', 'designation': 'Senior Developer', 'department': 'IT', 'employee_ids': [1001]},
    2: {'mentor_id': 2, 'name': 'Mentor2', 'designation': 'HR Manager', 'department': 'HR', 'employee_ids': [1002]},
    3: {'mentor_id': 3, 'name': 'Mentor3', 'designation': 'HR Manager', 'department': 'HR', 'employee_ids': [1003]},

}
course_db = {
    1: {'course_id': 1, 'course_name': 'Python Basics', 'department': 'IT', 'goals': 'Fundamental Python skills'},
    2: {'course_id': 2, 'course_name': 'Leadership Skills', 'department': 'HR', 'goals': 'Develop leadership qualities'},
    3: {'course_id': 3, 'course_name': 'object oriented concepts ', 'department': 'IT', 'goals': 'concepts on oops'},

}



def get_employee(employee_id):
    employee_data = employee_db.get(employee_id)
    return Employee(**employee_data) if employee_data else None

def get_mentors():
    return [Mentor(**mentor_data) for mentor_data in mentor_db.values()]

def get_courses():
    return [Course(**course_data) for course_data in course_db.values()]


    def is_matched(self, employee):
        return employee.employee_id in self.employee_ids



    def is_recommended(self, employee):
        return self.department == employee.department  # Simple recommendation logic based on department


def employee_login(user_id, password):
    employee_data = get_employee(user_id)
    if employee_data is not None and employee_data.password == password:
        return employee_data
    return None
def recommend_courses(employee_id):
    employee = get_employee(employee_id)
    if employee is not None:
        courses = get_courses()
        recommended_courses = [course for course in courses if course.is_recommended(employee)]
        return recommended_courses
    return None
def match_mentor(employee_id):
    employee = get_employee(employee_id)
    if employee is not None:
        mentors = get_mentors()
        matched_mentor = next((mentor for mentor in mentors if mentor.is_matched(employee)), None)
        return matched_mentor
    return None


# ...





def get_user_input_employee():
    employee_id = int(input("Enter employee ID          : "))
    name = input("Enter employee name        : ")
    designation = input("Enter employee designation : ")
    department = input("Enter employee department  : ")
    password = input("Enter password             : ")
    goals = input("Enter employee goals       : ")
    return {
        'employee_id': employee_id,
        'name': name,
        'designation': designation,
        'department': department,
        'password': password,
        'goals': goals,
    }

def view_employee_goals(employee_id):
    employee = get_employee(employee_id)
    if employee is not None:
        print(f"Employee {employee.name}'s Goals: {employee.goals}")
def view_employee_courses(employee_id):
    recommended_courses = recommend_courses(employee_id)
    if recommended_courses:
        print(f"Recommended Courses for Employee {employee_id}:")
        for course in recommended_courses:
            print(f"Course ID: {course.course_id}, Course Name: {course.course_name}, Goals: {course.goals}")
    else:
        print("No recommended courses for this employee.")

def view_employee_motivation(employee_id):
    matched_mentor = match_mentor(employee_id)
    if matched_mentor:
        print(f"Matched Mentor for Employee {employee_id}: {matched_mentor.name}, Department: {matched_mentor.department}")
    else:
        print("No mentor matched for this employee.")

def register_employee():
    user_input = get_user_input_employee()
    
    if user_input['employee_id'] in employee_db:
       # print("Employee ID already exists. Please choose a different ID.")
        return
    
    employee = Employee(**user_input)
    employee_db[employee.employee_id] = {
        'employee_id': employee.employee_id,
        'name': employee.name,
        'designation': employee.designation,
        'department': employee.department,
        'password': employee.password,
        'goals': employee.goals,
    }

    print("Employee added successfully.")


def view_course_details(course_id,user_id):
  #  employee = get_employee(employee_id)
    course = next((c for c in get_courses() if c.course_id == course_id), None)
    if course is not None:
        print(f"\nCourse Details for Course {course_id}:")
        print(f"Course Name: {course.course_name}, Department: {course.department}, Goals: {course.goals}")

        # Find matched mentor for the employee taking the course
        employee = get_employee(user_id)
        matched_mentor = match_mentor(employee.employee_id)
        if matched_mentor:
            print(f"Matched Mentor: {matched_mentor.name}, Department: {matched_mentor.department}")
        else:
            print("No mentor matched for this employee.")
    else:
        print(f"Course with ID {course_id} not found.")    

    
    
      
def delete_employee(employee_id):
    if employee_id in employee_db:
        del employee_db[employee_id]
        print(f"Employee with ID {employee_id} deleted successfully.")
    else:
        print(f"Employee with ID {employee_id} not found.")
        
        
# ... (previous code)


# ... (rest of the code)

# Example usage:
# update_course(1)
