def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = lowercase + uppercase + digits + symbols
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)
    
    return ''.join(password)

length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated password:", password)
