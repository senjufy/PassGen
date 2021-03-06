import sys
import random
import string


def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


print("Welcome to PassGen!")
print("We will generate passwords for you.")

answer = input("Answer few questions? y/n : ")
if answer == "y":
    pass
else:
    sys.exit("Thanks Again!")


def pass_fun():
    password = []
    special_character = string.punctuation
    digits = string.digits
    alphabets_lower = string.ascii_lowercase
    alphabets_upper = string.ascii_uppercase

    ask_character = input("Want your password to hold special character? y/n ")
    if ask_character == "y":
        password += random.choice(special_character)
        ask_digit = input("Want your password to hold digit? y/n ")
        if ask_digit == "y":
            password += random.choice(digits)
            password += random.choice(special_character)
            password += random.choice(digits)
            ask_lower = input("Do you want lower case? y/n ")
            if ask_lower == "y":
                password += random.choice(alphabets_lower)
                password += random.choice(digits)
                password += random.choice(special_character)
                password += random.choice(alphabets_lower)
                ask_upper = input("Do you want upper case? y/n ")
                if ask_upper == "y":
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_lower)
                    password += random.choice(digits)
                    password += random.choice(alphabets_lower)
                else:
                    pass

            else:
                ask_upper = input("Do you want upper case? y/n ")
                if ask_upper == "y":
                    password += random.choice(alphabets_upper)
                    password += random.choice(digits)
                    password += random.choice(special_character)
                    password += random.choice(alphabets_upper)
                    password += random.choice(digits)
                else:
                    pass
        else:
            ask_lower = input("Do you want lower case? y/n ")
            if ask_lower == "y":
                password += random.choice(special_character)
                password += random.choice(alphabets_lower)
                password += random.choice(alphabets_lower)
                ask_upper = input("Do you want upper case? y/n ")
                if ask_upper == "y":
                    password += random.choice(special_character)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_lower)
                    password += random.choice(special_character)

                else:
                    pass

            else:
                pass
    else:
        ask_digit = input("Want your password to hold digit? y/n ")
        if ask_digit == "y":
            password += random.choice(digits)
            ask_lower = input("Do you want lower case? y/n ")
            if ask_lower == "y":
                password += random.choice(alphabets_lower)
                password += random.choice(digits)
                password += random.choice(digits)
                password += random.choice(alphabets_lower)
                ask_upper = input("Do you want upper case? y/n ")
                if ask_upper == "y":
                    password += random.choice(alphabets_lower)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                    password += random.choice(digits)
                else:
                    pass

            else:
                ask_upper = input("Do you want upper cas? y/n ")
                if ask_upper == "y":
                    password += random.choice(digits)
                    password += random.choice(alphabets_upper)
                    password += random.choice(digits)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                else:
                    pass
        else:
            ask_lower = input("Do you want lower case? y/n ")
            if ask_lower == "y":
                password += random.choice(alphabets_lower)
                password += random.choice(alphabets_lower)
                ask_upper = input("Do you want upper case? y/n ")
                if ask_upper == "y":
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_lower)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_lower)
                else:
                    pass

            else:
                ask_upper = input("Do you want upper case? y/n ")
                if ask_upper == "y":
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                else:
                    pass

    return password


final_password = list_to_string(pass_fun())
print(final_password)

while True:
    acceptable = input("Acceptable Password? y/n ")
    if acceptable == "n":
        final_password = list_to_string(pass_fun())
        print(final_password)
    else:
        break

save = input("Would you like to save your password in a file? y/n ")

if save == "y":
    file = open("Password.txt", "a")
    title = input("Enter title for Password: ")
    file.write("Password for " + title + " is " + final_password + " \n")
    print("Password Saved")
    sys.exit("Thanks for using PassGen!")
else:
    sys.exit("Thank You For Using PassGen!")

