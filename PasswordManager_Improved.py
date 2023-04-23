import os
import random
import pyperclip
import json
import argparse

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def GenerateRandomPassword():
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    special_characters = """!@#$&*"""
    password_length = random.randint(6, 10)
    output_string = f"{random.choice(list(alphabets.lower()))}{random.choice(list(alphabets.upper()))}{random.choice(list(numbers))}{random.choice(list(special_characters))}"
    for _ in range(password_length):
        alphabet_or_number_or_special_character = random.randint(1, 20)
        if alphabet_or_number_or_special_character > 18:
            # SpecialCharacter
            output_string += random.choice(list(special_characters))
        elif alphabet_or_number_or_special_character > 14:
            # Numbers
            output_string += random.choice(list(numbers))
        elif alphabet_or_number_or_special_character > 10:
            # Capital Alphabets
            output_string += random.choice(list(alphabets.upper()))
        else:
            # Lower Case Alphabets
            output_string += random.choice(list(alphabets.lower()))
    output_string_list = list(output_string)
    random.shuffle(output_string_list)
    output_string_shuffled = "".join(output_string_list)
    return output_string_shuffled


def GeneratePasswordText():
    password_text_bar.delete(0, END)
    GeneratedPassword = GenerateRandomPassword()
    password_text_bar.insert(END, string=GeneratedPassword)
    pyperclip.copy(GeneratedPassword)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_json_file(SAVED_PASSWORDS_FILE_PATH, OUTPUT_DICT):
    try:
        file_ptr_read = open(SAVED_PASSWORDS_FILE_PATH, "r")
    except FileNotFoundError:
        file_ptr_write = open(SAVED_PASSWORDS_FILE_PATH, "w")
        json.dump(fp=file_ptr_write, obj=OUTPUT_DICT, indent=4)
        file_ptr_write.close()
        # write_to_json_file(SAVED_PASSWORDS_FILE_PATH, OUTPUT_DICT)
    else:
        input_dict = json.load(fp=file_ptr_read)
        input_dict.update(OUTPUT_DICT)
        file_ptr_read.close()
        file_ptr_write = open(SAVED_PASSWORDS_FILE_PATH, "w")
        json.dump(fp=file_ptr_write, obj=input_dict, indent=4)
        file_ptr_write.close()


def read_from_json_file(SAVED_PASSWORDS_FILE_PATH, website):
    try:
        with open(SAVED_PASSWORDS_FILE_PATH) as i_file:
            input_dict = json.load(i_file)
        matched_dict = input_dict[website]
    except FileNotFoundError:
        messagebox.showerror(title="OOPs", message="No Entry Found")
    except KeyError as error_message:
        messagebox.showerror(
            title="OOPs",
            message=f"No Website Corresponding to {error_message} found.\n Please check the spaces ,Cases and Special characters",
        )
    else:
        try:
            username = matched_dict["username"]
            password = matched_dict["password"]
        except KeyError as error_message:
            messagebox.showerror(
                title="OOPs",
                message=f"{error_message} NOT Found for the Website {website}",
            )
        else:
            output_message = f"The Following are the details\nUser Name : {username}\nPassword : {password}\n"
            messagebox.showinfo(title=website, message=output_message)


def search_details():
    global SAVED_PASSWORDS_FILE_PATH
    read_from_json_file(SAVED_PASSWORDS_FILE_PATH, website_text_bar.get())


def SavePasswords():
    global SAVED_PASSWORDS_FILE_PATH
    website = website_text_bar.get()
    username = email_username_text_bar.get()
    password = password_text_bar.get()

    if len(website) == 0:
        messagebox.showerror(
            title="OOPs", message="Please Enter a Website name to avoid confusion"
        )
    elif len(username) == 0:
        messagebox.showerror(title="OOPs", message="User Name Cannot be vacant")
    elif len(password) == 0:
        messagebox.showerror(
            title="OOPs",
            message="Password cannot be empty. Please Click on Generate Password",
        )
    else:
        ok_to_save = messagebox.askokcancel(
            title=website,
            message=f"The following Info is to be saved:\nUsername : {username}\nPassword : {password}\nAre you sure to save the information?",
        )
        if ok_to_save:
            OUTPUT_DICT = {website: {"username": username, "password": password}}
            write_to_json_file(SAVED_PASSWORDS_FILE_PATH, OUTPUT_DICT)

            website_text_bar.delete(0, END)
            password_text_bar.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
import os
from tkinter import *
from tkinter import messagebox


# MOST_COMMONLY_USED_EMAIL = "abc@gmail.com"
# STARTING_WEBSITE_TEXT = "www.abc.com"
# SAVED_PASSWORDS_FILE_PATH = os.path.join(
#    os.getcwd(),
#    "mypasswords.json",
# )
# IMAGE_FILE_PATH = os.path.join(
#    os.getcwd(),
#    "logo.png",
# )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Set Default Configuration for the app"
    )
    parser.add_argument(
        "--SAVED_PASSWORDS_FILE_PATH",
        help="The Default Value of the Filtpath to be saved",
        default=".",
    )
    parser.add_argument(
        "--MOST_COMMONLY_USED_EMAIL",
        help="""The Most Comonly UserName That you Use : (Default : 'abc@gmail.com') """,
        default="abc@gmail.com",
    )
    parser.add_argument(
        "--STARTING_WEBSITE_TEXT",
        help="The Default Value of the Starting Website",
        default="www.abc.com",
    )
    parser.add_argument(
        "--IMAGE_FILE_PATH",
        help="The File Path of the Logo Used",
        default=os.path.join(os.getcwd(), "logo.png"),
    )
    args = parser.parse_args()

    global SAVED_PASSWORDS_FILE_PATH
    SAVED_PASSWORDS_FILE_PATH = args.SAVED_PASSWORDS_FILE_PATH

    global MOST_COMMONLY_USED_EMAIL
    MOST_COMMONLY_USED_EMAIL = args.MOST_COMMONLY_USED_EMAIL

    global STARTING_WEBSITE_TEXT
    STARTING_WEBSITE_TEXT = args.STARTING_WEBSITE_TEXT

    global IMAGE_FILE_PATH
    IMAGE_FILE_PATH = args.IMAGE_FILE_PATH

    myscreen = Tk()
    myscreen.title("Password Generator Plus Saver")

    myscreen.config(padx=50, pady=50)

    mycanvas = Canvas(myscreen, width=210, height=210)
    IMAGE_FILE = PhotoImage(file=IMAGE_FILE_PATH)
    mycanvas.grid(row=0, column=1)
    mycanvas.create_image(120, 100, image=IMAGE_FILE)

    ## Creating Labels
    website_label = Label(text="Website:", font=(FONT_NAME, 10, "bold"))
    email_username_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"))
    password_label = Label(text="Password:", font=(FONT_NAME, 10, "bold"))
    website_label.grid(row=1, column=0)
    email_username_label.grid(row=2, column=0)
    password_label.grid(row=3, column=0)

    # Creating Buttons
    add_button = Button(text="Add", width=43, command=SavePasswords)
    generate_button = Button(text="Generate Password", command=GeneratePasswordText)
    add_button.grid(row=4, column=1, columnspan=2)
    generate_button.grid(row=3, column=2)

    # Generating Entry fields
    website_text_bar = Entry(width=25)
    email_username_text_bar = Entry(width=45)
    password_text_bar = Entry(width=25)

    website_text_bar.grid(row=1, column=1)
    email_username_text_bar.grid(row=2, column=1, columnspan=2)
    password_text_bar.grid(row=3, column=1)

    website_text_bar.focus()
    website_text_bar.insert(END, string=STARTING_WEBSITE_TEXT)
    email_username_text_bar.insert(END, string=MOST_COMMONLY_USED_EMAIL)

    # Search Button
    mysearchbutton = Button(text="Search", command=search_details)
    mysearchbutton.grid(row=1, column=2)

    myscreen.mainloop()
