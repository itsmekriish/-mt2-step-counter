print("🏃‍♂️Step Counter 🏃‍♂️")
daily_goal = int(input("🤷‍♂️ What is your daily step goal? "))
current_step = int(input("✨ How many steps have you taken today? "))

remaining = daily_goal - current_step
if remaining > 0:
    print(f"💪 You need {remaining} more steps to reach your goadl!")
else:
    print(f"🎉 Congratulations! You've excceede your goal by {-remaining} steps!")
