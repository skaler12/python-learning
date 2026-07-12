def calculate_weekly_minutes(hours):
    return hours * 60


def calculate_monthly_hours(weekly_hours):
    return weekly_hours * 4


weekly_minutes = calculate_weekly_minutes(12)
monthly_hours = calculate_monthly_hours(12)

print("Weekly learning minutes:")
print(weekly_minutes)

print("Monthly learning hours:")
print(monthly_hours)
