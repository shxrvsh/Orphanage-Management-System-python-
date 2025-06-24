from adoption import *
from children import *
from donation import *

import tkinter as tk
import mysql.connector
import csv

# Replace these credentials with your own MySQL database details
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '19122004'
MYSQL_DATABASE = 'orphanage'


# Define global variables for frames and initialize them as empty frames


def check_credentials(username, password):
    try:
        # Connect to MySQL and fetch the stored credentials
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )

        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result is not None

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)
        return False

def login():
    username = entry_username.get()
    password = entry_password.get()

    if check_credentials(username, password):
        login_frame.pack_forget()  # Hide the login frame
        show_main_screen()
    else:
        label_status.config(text="Invalid login credentials.", fg="red")

def save_adoption_record(name, age, gender):
    with open('adoption_rec.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([name, age, gender])

def remove_child_from_database(name):
    # Implement the logic to remove the child from the database
    pass

def adopt_child():
    child_name = entry_child_name.get()
    child_age = entry_child_age.get()
    child_gender = entry_child_gender.get()

    save_adoption_record(child_name, child_age, child_gender)
    remove_child_from_database(child_name)

    # Add a message box to show successful adoption

def show_adoption_records():
    # Implement the functionality to show the adoption records from 'adoption_rec.csv'
    pass

def save_child_details(name, age, gender):
    with open('children.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([name, age, gender])

    # Save the child details to the database
    # Implement the logic to save the child details to the database

def show_children_details():
    # Implement the functionality to show the children details from 'children.csv'
    pass

def save_donation_details(name, amount, notes):
    with open('donations.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([name, amount, notes])

def show_donation_records():
    # Implement the functionality to show the donation records from 'donations.csv'
    pass

def show_main_screen():
    root.attributes("-fullscreen", True)
    root.geometry("800x600")  # Set a fixed window size
    root.title("Main Screen")

    label_welcome = tk.Label(root, text="Welcome to the main screen!", font=("Helvetica", 24))
    label_welcome.pack(pady=50)

    button_frame = tk.Frame(root)
    button_frame.pack(expand=True)

    button_adoption = tk.Button(button_frame, text="Adoption", command=show_adoption_screen, font=("Helvetica", 18))
    button_adoption.pack(side=tk.LEFT, padx=20, pady=20)

    button_children = tk.Button(button_frame, text="Children", command=show_children_screen, font=("Helvetica", 18))
    button_children.pack(side=tk.LEFT, padx=20, pady=20)

    button_donation = tk.Button(button_frame, text="Donation", command=show_donation_screen, font=("Helvetica", 18))
    button_donation.pack(side=tk.LEFT, padx=20, pady=20)

    login_frame.pack_forget()  # Ensure login frame is hidden when showing the main screen
    hide_all_sections()  # Ensure all section frames are hidden initially

def show_adoption_screen():
    hide_all_sections()
    adoption_frame.pack(fill=tk.BOTH, expand=True)

    label_adoption.pack(pady=50)

    entry_child_name.pack(pady=10)
    entry_child_age.pack(pady=10)
    entry_child_gender.pack(pady=10)

    button_adopt.pack(pady=20)
    button_view_adoption_records.pack(pady=20)

def show_children_screen():
    hide_all_sections()
    children_frame.pack(fill=tk.BOTH, expand=True)

    label_children.pack(pady=50)

    entry_child_name.pack(pady=10)
    entry_child_age.pack(pady=10)
    entry_child_gender.pack(pady=10)

    button_add_child.pack(pady=20)
    button_view_children_details.pack(pady=20)

def show_donation_screen():
    hide_all_sections()
    donation_frame.pack(fill=tk.BOTH, expand=True)

    label_donation.pack(pady=50)

    entry_donation_name.pack(pady=10)
    entry_donation_amount.pack(pady=10)
    entry_donation_notes.pack(pady=10)

    button_donate.pack(pady=20)
    button_view_donation_records.pack(pady=20)

def hide_all_sections():
    adoption_frame.pack_forget()
    children_frame.pack_forget()
    donation_frame.pack_forget()

# Create the main Tkinter window
root = tk.Tk()
root.title("Login Screen")

login_frame = tk.Frame(root)  # Create the login frame

label_username = tk.Label(login_frame, text="Username:", font=("Helvetica", 18))
label_username.pack()

entry_username = tk.Entry(login_frame, font=("Helvetica", 18))
entry_username.pack(pady=5)

label_password = tk.Label(login_frame, text="Password:", font=("Helvetica", 18))
label_password.pack()

entry_password = tk.Entry(login_frame, show="*", font=("Helvetica", 18))
entry_password.pack(pady=5)

button_login = tk.Button(login_frame, text="Login", command=login, font=("Helvetica", 18))
button_login.pack(pady=30)

label_status = tk.Label(login_frame, text="", fg="red", font=("Helvetica", 14))
label_status.pack()

# Create frames for each section and keep them hidden initially
adoption_frame = tk.Frame(root)
children_frame = tk.Frame(root)
donation_frame = tk.Frame(root)

# Elements for the Adoption section
label_adoption = tk.Label(adoption_frame, text="Adoption Section", font=("Helvetica", 24))
entry_child_name = tk.Entry(adoption_frame, font=("Helvetica", 18))
entry_child_age = tk.Entry(adoption_frame, font=("Helvetica", 18))
entry_child_gender = tk.Entry(adoption_frame, font=("Helvetica", 18))
button_adopt = tk.Button(adoption_frame, text="Adopt", command=adopt_child, font=("Helvetica", 18))
button_view_adoption_records = tk.Button(adoption_frame, text="View Adoption Records", command=show_adoption_records, font=("Helvetica", 18))

# Elements for the Children section
label_children = tk.Label(children_frame, text="Children Section", font=("Helvetica", 24))
button_add_child = tk.Button(children_frame, text="Add Child", command=lambda: save_child_details(entry_child_name.get(), entry_child_age.get(), entry_child_gender.get()), font=("Helvetica", 18))
button_view_children_details = tk.Button(children_frame, text="View Children Details", command=show_children_details, font=("Helvetica", 18))

# Elements for the Donation section
label_donation = tk.Label(donation_frame, text="Donation Section", font=("Helvetica", 24))
entry_donation_name = tk.Entry(donation_frame, font=("Helvetica", 18))
entry_donation_amount = tk.Entry(donation_frame, font=("Helvetica", 18))
entry_donation_notes = tk.Entry(donation_frame, font=("Helvetica", 18))
button_donate = tk.Button(donation_frame, text="Donate", command=lambda: save_donation_details(entry_donation_name.get(), entry_donation_amount.get(), entry_donation_notes.get()), font=("Helvetica", 18))
button_view_donation_records = tk.Button(donation_frame, text="View Donation Records", command=show_donation_records, font=("Helvetica", 18))

root.mainloop()
