
age = input("What is your current age? Enter here: ")

life_time= int(input("How long do you think that you'll live? Enter here: "))
new_age=int(age)
days_left=(life_time-new_age)*365
# print(days_left)

weeks_left=(life_time-new_age)*52
# print(weeks_left)

months_left= (life_time-new_age)*12
# print(months_left)

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left if you were to live till {life_time}.")








