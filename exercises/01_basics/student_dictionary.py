student = {
    "name": "Grzegorz",
    "level": "beginner",
    "goal": "Junior Data Engineer",
    "weekly_hours": 12,
    "uses_git": True,
}

print("Student name:")
print(student["name"])

print("Goal:")
print(student["goal"])

print("Weekly hours:")
print(student.get("weekly_hours"))

print("Uses Git:")
print(student.get("uses_git"))

print("Cloud:")
print(student.get("cloud", "Not selected yet"))
