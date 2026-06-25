import random
import string

# পাইথনকে বলছি পাসওয়ার্ডে কী কী থাকবে (অক্ষর, সংখ্যা ও চিহ্ন)
উপাদান = string.ascii_letters + string.digits + string.punctuation

# পাইথন নিজ দায়িত্বে ৮ অক্ষরের একটা কঠিন পাসওয়ার্ড বানাবে
পাসওয়ার্ড = "".join(random.choice(উপাদান) for i in range(8))

print("মামা, আপনার আজকের সিক্রেট পাসওয়ার্ড হলো:", পাসওয়ার্ড)