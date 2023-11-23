# bmi
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
bmi_int = int(bmi)


# your life in weeks
age = print("What is yor current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
month_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"You have {years_remaining}, {month_remaining}, {weeks_remaining}, {days_remaining} left")


# calculator
#- if the bill was 150, split between 5 people, with 12% tip
# - each person should pay (150 / 5) * 1.12
print("Welcome to the calculator")
bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

tip_as_persent = tip / 100
total_tip_amount = tip * tip_as_persent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / person
final_amount = around(bill_per_person, 2)
final_amount = ":.2f".format(bill_per_person)

print(final_amount)


            
