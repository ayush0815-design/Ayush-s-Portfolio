"""
Project Title: Daily Calorie Tracker CLI
Course: Programming for Problem Solving using Python
Student Name: [Your Name]
Date: [Insert Date]

Description:
A command-line tool to help users track daily calorie intake,
compare it with a daily limit, and optionally save a session log.
"""

import datetime

# --- Task 1: Setup & Introduction ---
print("=======================================")
print("   Welcome to Daily Calorie Tracker!   ")
print("=======================================")
print("Track your meals, calculate total and average calories,")
print("and see if you're within your daily calorie goal.\n")

# --- Task 2: Input & Data Collection ---
meal_names = []
meal_calories = []

num_meals = int(input("How many meals did you have today? "))

for i in range(num_meals):
    print(f"\nMeal {i+1}:")
    meal = input("Enter meal name (e.g., Breakfast): ")
    calories = float(input("Enter calorie amount: "))
    meal_names.append(meal)
    meal_calories.append(calories)

# --- Task 3: Calorie Calculations ---
total_calories = sum(meal_calories)
average_calories = total_calories / len(meal_calories)
daily_limit = float(input("\nEnter your daily calorie limit: "))

# --- Task 4: Exceed Limit Warning System ---
if total_calories > daily_limit:
    status_message = "⚠️ You have exceeded your daily calorie limit!"
else:
    status_message = "✅ Great job! You are within your daily limit."

# --- Task 5: Neatly Formatted Output ---
print("\n========== Daily Calorie Summary ==========\n")
print("Meal Name\tCalories")
print("-------------------------------------------")
for meal, cal in zip(meal_names, meal_calories):
    print(f"{meal:<15}\t{cal:.2f}")
print("-------------------------------------------")
print(f"Total:\t\t{total_calohries:.2f}")
print(f"Average:\t{average_calories:.2f}")
print(f"Daily Limit:\t{daily_limit:.2f}")
print("-------------------------------------------")
print(status_message)
print("\n===========================================\n")

# --- Task 6 (Bonus): Save Session Log to File ---
save_log = input("Do you want to save this session to a file? (yes/no): ").strip().lower()

if save_log == "yes":
    filename = "calorie_log.txt"
    with open(filename, "a") as f:
        f.write("====== Daily Calorie Tracker Session ======\n")
        f.write(f"Date & Time: {datetime.datetime.now()}\n\n")
        for meal, cal in zip(meal_names, meal_calories):
            f.write(f"{meal:<15}\t{cal:.2f}\n")
        f.write("-------------------------------------------\n")
        f.write(f"Total:\t\t{total_calories:.2f}\n")
        f.write(f"Average:\t{average_calories:.2f}\n")
        f.write(f"Daily Limit:\t{daily_limit:.2f}\n")
        f.write(f"Status: {status_message}\n")
        f.write("===========================================\n\n")
    print(f"\n✅ Session saved successfully to {filename}!")
else:
    print("\nSession not saved. Thank you for using the tracker!")

# --- End of Program ---
