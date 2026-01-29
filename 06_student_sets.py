# The starting lists
math_students = ["ID101", "ID102", "ID105", "ID108"]
science_students = ["ID102", "ID109", "ID101", "ID110"]

math_set = set(math_students)
science_set = set(science_students)
# (a) Students enrolled in both courses.
both_courses = math_set & science_set
print("Students in both courses:", both_courses)

# (b) All unique students enrolled in either course.
either_course = math_set | science_set
print("Students in either course:", either_course)

# (c) Students enrolled in Math but not Science.
only_math = math_set - science_set
print("Students only in Math:", only_math)

# (d) Students enrolled in Science but not Math.
only_sience = science_set - math_set
print("Students only in Science:", only_sience)

# conclusion: the set operations are "&" for intersection, "|" for union, and "-" for difference.
