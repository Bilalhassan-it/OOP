# ======================
# Example Program Runner
# ======================

from LMS import Instructor, Student, Course

# Create an instructor
teacher1 = Instructor("Dr. Ayesha", "ayesha@school.edu", 2001)

# Create students
st1 = Student("Bilal Ahmed", "bilal@gmail.com", 101)
st2 = Student("Zara Khan", "zara@gmail.com", 102)
st3 = Student("Hamza Ali", "hamza@gmail.com", 103)

# Create courses
python_course = Course("Python Programming", "CS101")
dsa_course = Course("Data Structures & Algorithms", "CS102")

# Assign instructor to courses
teacher1.assign_course(python_course)
teacher1.assign_course(dsa_course)

# Enroll students
st1.enroll_course(python_course)
st2.enroll_course(python_course)
st3.enroll_course(dsa_course)

# Show information
python_course.show_details()
dsa_course.show_details()

teacher1.view_courses()
st1.view_courses()
st2.view_courses()
st3.view_courses()
