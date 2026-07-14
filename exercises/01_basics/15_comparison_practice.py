def check_learning_level(weekly_hours):
    if weekly_hours >= 15:
        return "intensive"
    if weekly_hours >= 10:
        return "solid"
    if weekly_hours >= 5:
        return "basic"
    return "too low"


print(check_learning_level(16))
print(check_learning_level(12))
print(check_learning_level(7))
print(check_learning_level(2))
