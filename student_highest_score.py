students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 99},
    {"name": "Edward", "score": 92},
    {"name": "Fiona", "score": 100},
]

highest_score = -1
top_student = ""

for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        top_student = student["name"]
print(
    f"The student with the highest score is {top_student} with a score of {highest_score}."
)
