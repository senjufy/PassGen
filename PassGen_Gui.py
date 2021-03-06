import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
import string


def pass_fun():
    entry.delete(0, END)
    password = []
    special_character = string.punctuation
    digits = string.digits
    alphabets_lower = string.ascii_lowercase
    alphabets_upper = string.ascii_uppercase

    if var_special.get() == 1:
        password += random.choice(special_character)
        if var_num.get() == 1:
            password += random.choice(digits)
            password += random.choice(special_character)
            password += random.choice(digits)
            if var_lower.get() == 1:
                password += random.choice(alphabets_lower)
                password += random.choice(digits)
                password += random.choice(special_character)
                password += random.choice(alphabets_lower)
                if var_upper.get() == 1:
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_lower)
                    password += random.choice(digits)
                    password += random.choice(alphabets_lower)
                else:
                    pass

            else:
                if var_upper.get() == 1:
                    password += random.choice(alphabets_upper)
                    password += random.choice(digits)
                    password += random.choice(special_character)
                    password += random.choice(alphabets_upper)
                    password += random.choice(digits)
                else:
                    pass
        else:
            if var_lower.get() == 1:
                password += random.choice(special_character)
                password += random.choice(alphabets_lower)
                password += random.choice(alphabets_lower)
                if var_upper.get() == 1:
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
        if var_num.get() == 1:
            password += random.choice(digits)
            if var_lower.get() == 1:
                password += random.choice(alphabets_lower)
                password += random.choice(digits)
                password += random.choice(digits)
                password += random.choice(alphabets_lower)
                if var_upper.get() == 1:
                    password += random.choice(alphabets_lower)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                    password += random.choice(digits)
                else:
                    pass

            else:
                if var_upper.get() == 1:
                    password += random.choice(digits)
                    password += random.choice(alphabets_upper)
                    password += random.choice(digits)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                else:
                    pass
        else:
            if var_lower.get() == 1:
                password += random.choice(alphabets_lower)
                password += random.choice(alphabets_lower)
                if var_upper.get() == 1:
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_lower)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_lower)
                else:
                    pass

            else:
                if var_upper.get() == 1:
                    password += random.choice(alphabets_upper)
                    password += random.choice(alphabets_upper)
                else:
                    pass
    return password


def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def generate():
    data = list_to_string(pass_fun())
    entry.insert(0, data)


def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)


def save_file():
    password = entry.get()
    file = open("Password.txt", "a")
    file.write("Password is " + password + " \n")


root = Tk()
var_num = IntVar()
var_special = IntVar()
var_lower = IntVar()
var_upper = IntVar()

root.title("PassGen")
root.geometry("250x180")
label_num = Label(root, text="Includes Number?").place(x=10, y=10)
radio_num_y = Radiobutton(root, text="Yes", variable=var_num, value=1).place(x=100, y=8)
radio_num_n = Radiobutton(root, text="No", variable=var_num, value=2).place(x=145, y=8)

label_special = Label(root, text="Includes Special Character?").place(x=10, y=30)
radio_special_y = Radiobutton(root, text="Yes", variable=var_special, value=1).place(x=145, y=28)
radio_special_n = Radiobutton(root, text="No", variable=var_special, value=2).place(x=190, y=28)

label_upper = Label(root, text="Includes Upper Case Letters?").place(x=10, y=50)
radio_upper_y = Radiobutton(root, text="Yes", variable=var_lower, value=1).place(x=155, y=48)
radio_upper_n = Radiobutton(root, text="No", variable=var_lower, value=2).place(x=200, y=48)

label_lower = Label(root, text="Includes Lower Case Letters?").place(x=10, y=70)
radio_lower_y = Radiobutton(root, text="Yes", variable=var_upper, value=1).place(x=155, y=68)
radio_lower_n = Radiobutton(root, text="No", variable=var_upper, value=2).place(x=200, y=68)

entry = Entry(root, foreground="black")
entry.place(x=60, y=95)

generate_button = Button(root, command=generate, text="Generate")
generate_button.place(x=89, y=115)

copy_button = Button(root, command=copy1, text="Copy")
copy_button.place(x=50, y=142)

save_button = Button(root, command=save_file, text="Save")
save_button.place(x=130, y=142)
root.mainloop()