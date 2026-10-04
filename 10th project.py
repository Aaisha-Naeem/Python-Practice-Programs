import random
chars="!@$%^&adcd1234"
password=""
for i in range(8):
    password+=random.choice(chars)
    print("Generated password is:",password)

    
