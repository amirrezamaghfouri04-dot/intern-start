score = 0
print("🎮 کوییز سه سؤالی هارمونیا")

answer = input("1) Agent هارمونیا اسمش چیست؟ ")
if answer.lower() == "echo":
    print("درسته! ✅")
    score += 1
else:
    print("نه؛ جواب Echo بود.")

answer = input("2) 7 ضربدر 8 چند می‌شود؟ ")
if answer == "56":
    print("درسته! ✅")
    score += 1
else:
    print("نه؛ جواب 56 بود.")

answer = input("3) منظومه‌ی شمسی چند سیاره دارد؟")
if answer == "8":
    print("درسته! ✅")
    score += 1
else:
    print("نه؛ جواب 8 بود.")

print(f"امتیاز تو: {score} از 3")
if score == 3:
    print("🏆 عالی! تو آماده‌ای.")
elif score >= 1:
    print("👍 خوب بود؛ یک بار دیگر امتحان کن.")
else:
    print("💪 اشکالی ندارد؛ همه از همین‌جا شروع کرده‌اند.")