import random

# কিছু চেনা শব্দ যা মনে রাখা সহজ
words = ["baaler", "password", "kothin", "mama", "coding", "python", "safari"]

# পাইথন নিজে থেকে ৩টি শব্দ বেছে নিয়ে মাঝখানে '-' দিয়ে জোড়া দেবে
my_passphrase = "-".join(random.choice(words) for i in range(3))

print("Your easy but secure password is:", my_passphrase)