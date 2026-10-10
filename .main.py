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