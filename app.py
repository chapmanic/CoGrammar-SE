password = input("Enter a password: ")
loop = True
password_vault = []
guesses = 0
while loop:
    password_2 = input("Enter a password: ")
    if password == password_2:
        print(f"Correct, You password is {password}")
        print(f"Correct! {password} is the right password")
        print(password_vault)
        again_ = input("Play again? Y or N").upper()
        if again_ == "N":
            loop = False
    else:
        guesses += 1
        print(f"Thats incorrect, {password_2} is wrong. total guesses:{guesses}")
        password_vault.append(password_2)
    