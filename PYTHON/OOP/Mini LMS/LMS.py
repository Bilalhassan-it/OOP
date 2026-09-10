# ==========================
# School Management Entities
# ==========================

# Base class
class Person:
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email

    def get_info(self):
        return f"Name: {self.full_name}, Email: {self.email}"


# Derived class - Student
class Student(Person):
    def __init__(self, full_name, email, student_id):
        super().__init__(full_name, email)
        self.student_id = student_id
        self.enrolled_courses = []  # composition (student has courses)

    def enroll_course(self, course):
        """Enroll student into a course"""
        self.enrolled_courses += [course]
        course.add_student(self)

    def view_courses(self):
        """View all courses enrolled by the student"""
        if not self.enrolled_courses:
            print(f"{self.full_name} is not enrolled in any courses.")
        else:
            print(f"\nCourses for {self.full_name}:")
            for course in self.enrolled_courses:
                print(f"- {course.course_title}")


# Derived class - Instructor
class Instructor(Person):
    def __init__(self, full_name, email, teacher_id):
        super().__init__(full_name, email)
        self.teacher_id = teacher_id
        self.assigned_courses = []  # aggregation (teacher teaches courses)

    def assign_course(self, course):
        """Assign teacher to a course"""
        self.assigned_courses += [course]
        course.set_instructor(self)

    def view_courses(self):
        """View all assigned courses"""
        if not self.assigned_courses:
            print(f"{self.full_name} has no assigned courses.")
        else:
            print(f"\nCourses taught by {self.full_name}:")
            for course in self.assigned_courses:
                print(f"- {course.course_title}")


# Course class
class Course:
    def __init__(self, course_title, course_code):
        self.course_title = course_title
        self.course_code = course_code
        self.instructor = None
        self.students = []

    def add_student(self, student):
        self.students += [student]

    def set_instructor(self, instructor):
        self.instructor = instructor

    def show_details(self):
        """Display complete course information"""
        print(f"\nCourse: {self.course_title} ({self.course_code})")
        print(f"Instructor: {self.instructor.full_name if self.instructor else 'Not Assigned'}")
        print("Students:")
        if self.students:
            for s in self.students:
                print(f"- {s.full_name}")
        else:
            print("No students enrolled yet.")
