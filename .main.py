from datetime import date 

print("== My Personal Assistant ===")

name = input("What is your name? ")

print("welcome," , name)

today = date. today()
deadline = date(2026, 12, 10)
days_left = (deadline - today).days

print("days left until the deadline:", days_left)
print("lets build something great!")
goal = input("What is your career goal? ")
print(" Your goal is to", goal)

if "ai" in goal.lower():
    print("Great goal! Start with Python.")
    print("Your first task: Build a simple calculator.")

elif "web" in goal.lower():
    print("Great goal! Start with HTML and CSS.")
    print("Your first task: Build a personal webpage.")

elif "freelance" in goal.lower():
    print("Great goal! Start by building projects.")
    print("Your first task: Upload one project to GitHub.")

else:
    print("Great goal! Stay consistent.")
    print("Your first task: Research the skills your goal requires.")
    
    print("\nLet's check your progress!")

progress = input("Have you started working on your goal? (yes/no): ")

if progress.lower() == "yes":
    print("Excellent! Keep going and stay consistent.")
elif progress.lower() == "no":
    print("No problem! Start today with one small task.")
else:
    print("Please enter yes or no next time.")
