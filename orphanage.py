import tkinter as tk
import mysql.connector
from datetime import date
import csv
import os
from tkinter import PhotoImage
from PIL import Image,ImageTk

#MySQL database details
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '19122004'
MYSQL_DATABASE = 'orphanage'


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
        cursor.execute("SELECT * FROM users WHERE username='{}' AND password='{}'".format(username, password))
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

def save_donation_details(name, amount, notes):
    try:
        with open('donations.csv', 'r', newline='\n') as csvfile:
            pass
    except:
        with open('donations.csv', 'w', newline='\n') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(["name","amount","notes"])
    
    with open('donations.csv', 'a', newline='\n') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([name, amount, notes])
    show_main_screen()

def save_child_details(cid,name,dob,bloodg,medcon):
    con= mysql.connector.connect(host="localhost",username="root",password="19122004",database="orphanage")
    cur=con.cursor()
    cur.execute("create table IF NOT EXISTS children(cid int primary key not null, name varchar(20) not null, dob date not null, bloodg varchar(5) not null,medcon varchar(20) not null)")
    cur.execute("insert into children values({},'{}','{}','{}','{}')".format(int(cid),name,dob,bloodg,medcon))
    con.commit()
    con.close()
    show_main_screen()


def save_adoption_details(cid,pname,address,contact):
    con= mysql.connector.connect(host="localhost",username="root",password="19122004",database="orphanage")
    cur=con.cursor()
    cur.execute("create table IF NOT EXISTS adoption(cid int primary key not null, cname varchar(20) not null,adopter_name varchar(20) not null, address varchar(50) not null, contact varchar(15) not null, date_of_adoption date not null)")
    cur.execute("select name from children where cid={}".format(int(cid)))
    data=cur.fetchone()[0]
    cur.execute("insert into adoption values({},'{}','{}','{}','{}','{}')".format(int(cid),data,pname,address,contact,date.today()))
    cur.execute("delete from children where cid={}".format(int(cid)))
    con.commit()
    con.close()
    show_main_screen()
    

        
def show_main_screen():
    hide_all_sections()
    main_screen_frame.pack(fill=tk.BOTH, expand=True)
    root.attributes("-fullscreen", True)
    root.geometry("800x600")  # Set a fixed window size
    root.title("Main Screen")
    
    label_welcome.pack(pady=50)   

    
    button_adoption.pack(side=tk.LEFT, padx=20, pady=20)

    
    button_children.pack(side=tk.LEFT, padx=20, pady=20)

    
    button_donation.pack(side=tk.LEFT, padx=20, pady=20)

    login_frame.pack_forget()  # Ensure login frame is hidden when showing the main screen
    hide_all_sections()  # Ensure all section frames are hidden initially

def hide_main_screen_buttons():
    button_adoption.pack_forget()
    button_children.pack_forget()
    button_donation.pack_forget()
    label_welcome.pack_forget()
    
def show_adoption_screen():
    main_screen_frame.pack_forget()
    hide_main_screen_buttons()
    hide_all_sections()
    adoption_frame.pack(fill=tk.BOTH, expand=True)
    
    label_adoption.pack(pady=50)
    label_cid1.pack()
    
    entry_cid1.pack(pady=10)
    label_pname.pack()
    
    entry_pname.pack(pady=10)
    label_address.pack()
    
    entry_address.pack(pady=10)
    label_contact.pack()
    
    entry_contact.pack(pady=10)
    button_save_adoption.pack(pady=10)
                         
    button_open_adoption.pack(pady=10)

    button_back1.pack(pady=20)
    

    # Add other content and buttons specific to the Adoption section

def show_children_screen():
    main_screen_frame.pack_forget()
    hide_main_screen_buttons()
    hide_all_sections()
    children_frame.pack(fill=tk.BOTH, expand=True)

    label_children.pack(pady=50)

    label_cid.pack()
    entry_cid.pack(pady=10)
    
    label_cname.pack()
    entry_cname.pack(pady=10)
    
    label_dob.pack()
    entry_dob.pack(pady=10)
    
    label_bloodg.pack()
    entry_bloodg.pack(pady=10)
    
    label_med.pack()
    entry_med.pack(pady=10)

    button_save_child.pack(pady=10)

    button_open_child.pack(pady=10)

    button_back2.pack(pady=20)

    # Add other content and buttons specific to the Children section

def show_donation_screen():
    main_screen_frame.pack_forget()
    hide_main_screen_buttons()
    hide_all_sections()
    
    donation_frame.pack(fill=tk.BOTH, expand=True)


    label_donation.pack(pady=50)

    
    label_name.pack()
    entry_name.pack(pady=10)

    
    label_amount.pack()
    entry_amount.pack(pady=10)

    
    label_notes.pack()
    entry_notes.pack(pady=10)

    button_save.pack(pady=20)

    button_opendon.pack(pady=20)

    button_back3.pack(pady=20)

    # Add other content and buttons specific to the Donation section

def hide_all_sections():
    
    adoption_frame.pack_forget()
    children_frame.pack_forget()
    donation_frame.pack_forget()

def open_donations():
    os.system("donations.csv")

    

def open_children():
    con= mysql.connector.connect(host="localhost",username="root",password="19122004",database="orphanage")
    cur=con.cursor()
    cur.execute("select * from children")
    data=cur.fetchall()

    with open("temp_children.csv",'w',newline='\n') as f:
        writer=csv.writer(f)
        writer.writerow(['cid','name','dob','blood group','medical conditions'])
        writer.writerows(data)
    os.system("temp_children.csv")



def open_adoption():

    con= mysql.connector.connect(host="localhost",username="root",password="19122004",database="orphanage")
    cur=con.cursor()
    cur.execute("select * from adoption")
    data=cur.fetchall()


    with open("temp_adoption.csv","w",newline='\n')as f:
        writer=csv.writer(f)
        writer.writerow(['cid','child name','adopter name','address','contact','date of adoption'])
        writer.writerows(data)
    os.system("temp_adoption.csv")




# Create the main Tkinter window
root = tk.Tk()
root.title("Login Screen")
main_screen_frame = tk.Frame(root)
img=Image.open("orphanage.jpg")
background_img=ImageTk.PhotoImage(img)
background_label = tk.Label(main_screen_frame, image=background_img)
background_label.image = background_img
background_label.place(x=0,y=0,relwidth=1,relheight=1)

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

login_frame.pack(fill=tk.BOTH, expand=True)  # Pack the login frame initially

label_welcome = tk.Label(root, text="Welcome to the main screen!", font=("Helvetica", 24))
button_frame = tk.Frame(root)
button_frame.pack(expand=True)
button_adoption = tk.Button(button_frame, text="Adoption", command=show_adoption_screen, font=("Helvetica", 18))
button_children = tk.Button(button_frame, text="Children", command=show_children_screen, font=("Helvetica", 18))
button_donation = tk.Button(button_frame, text="Donation", command=show_donation_screen, font=("Helvetica", 18))
    

# Create frames for each section and keep them hidden initially
adoption_frame = tk.Frame(root)

#adoption elements
label_adoption = tk.Label(adoption_frame, text="Adoption Section", font=("Helvetica", 24))
label_cid1 = tk.Label(adoption_frame, text="CID:", font=("Helvetica", 18))
entry_cid1 = tk.Entry(adoption_frame, font=("Helvetica", 18))
label_pname = tk.Label(adoption_frame, text="Adopter's Name:", font=("Helvetica", 18))
entry_pname = tk.Entry(adoption_frame, font=("Helvetica", 18))
label_address = tk.Label(adoption_frame, text="Address:", font=("Helvetica", 18))
entry_address = tk.Entry(adoption_frame, font=("Helvetica", 18))
label_contact = tk.Label(adoption_frame, text="Contact No:", font=("Helvetica", 18))
entry_contact = tk.Entry(adoption_frame, font=("Helvetica", 18))
button_save_adoption = tk.Button(adoption_frame, text="Save Details", command=lambda: save_adoption_details(entry_cid1.get(),entry_pname.get(), entry_address.get(), entry_contact.get()), font=("Helvetica", 18))
button_open_adoption = tk.Button(adoption_frame, text="Adoption Records", command=open_adoption, font=("Helvetica", 18))
button_back1 = tk.Button(adoption_frame, text="Back to Main", command=show_main_screen, font=("Helvetica", 18))


#children elements
children_frame = tk.Frame(root)
label_children = tk.Label(children_frame, text="Children Section", font=("Helvetica", 24))
label_cid = tk.Label(children_frame, text="CID:", font=("Helvetica", 18))
entry_cid = tk.Entry(children_frame, font=("Helvetica", 18))
label_cname = tk.Label(children_frame, text="Name:", font=("Helvetica", 18))
entry_cname = tk.Entry(children_frame, font=("Helvetica", 18))
label_dob = tk.Label(children_frame, text="DOB(YYYY-MM-DD):", font=("Helvetica", 18))
entry_dob = tk.Entry(children_frame, font=("Helvetica", 18))
label_bloodg = tk.Label(children_frame, text="Blood Group:", font=("Helvetica", 18))
entry_bloodg = tk.Entry(children_frame, font=("Helvetica", 18))
label_med = tk.Label(children_frame, text="Medical Conditions(if not mention null):",font=("Helvetica", 18))
entry_med = tk.Entry(children_frame, font=("Helvetica", 18))
button_save_child = tk.Button(children_frame, text="Save Details", command=lambda: save_child_details(entry_cid.get(),entry_cname.get(), entry_dob.get(), entry_bloodg.get(),entry_med.get()), font=("Helvetica", 18))
button_open_child = tk.Button(children_frame, text="Children Record", command=open_children, font=("Helvetica", 18))
button_back2 = tk.Button(children_frame, text="Back to Main", command=show_main_screen, font=("Helvetica", 18))

#donation elements
donation_frame = tk.Frame(root)
label_donation = tk.Label(donation_frame, text="Donation Section", font=("Helvetica", 24))
label_name = tk.Label(donation_frame, text="Name:", font=("Helvetica", 18))
entry_name = tk.Entry(donation_frame, font=("Helvetica", 18))
label_amount = tk.Label(donation_frame, text="Amount:", font=("Helvetica", 18))
entry_amount = tk.Entry(donation_frame, font=("Helvetica", 18))
label_notes = tk.Label(donation_frame, text="Notes:", font=("Helvetica", 18))
entry_notes = tk.Entry(donation_frame, font=("Helvetica", 18))
button_save = tk.Button(donation_frame, text="Save Donation", command=lambda: save_donation_details(entry_name.get(), entry_amount.get(), entry_notes.get()), font=("Helvetica", 18))
button_opendon = tk.Button(donation_frame, text="Past Donations", command=open_donations, font=("Helvetica", 18))
button_back3 = tk.Button(donation_frame, text="Back to Main", command=show_main_screen, font=("Helvetica", 18))


root.mainloop()
