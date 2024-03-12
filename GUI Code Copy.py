#Where all of the libraries needed to create the controlled assessment
from tkinter import *
from tkinter import ttk
import csv
import sys
import random
import tkinter.simpledialog
import datetime
import time
from tkinter import messagebox
import math
from datetime import date
import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.simpledialog import askstring
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
import string
from tkinter import Canvas


#changes the users view
def raise_frame(frame):
    frame.tkraise()

#clear the login frame
def clearloginframe():
    username.set('')
    password.set('')

#exit the program fully
def exitprogram():
    response = messagebox.askyesno('Login','Are you sure?')
    if response == True:
        root.destroy()

#login to the system
def gotoregistrationframe():
    #check that all data has been filled in

    if username.get() == '' or password.get() == '':
        messagebox.showinfo('Login','Please enter all data')
    else:

        #search the csv file using the entered data
        found = False
        #connect to the login file
        with open('login.csv', 'r') as csvfile:
            recordreader = csv.reader(csvfile)
            #search each row in the file
            for row in recordreader:
                if row == '':
                    pass
                else:
                    if username.get() == row[0] and password.get() == row[1]:
                        found = True
        csvfile.close()

        if found == True:
            messagebox.showinfo('Login', 'Login was successful')
            raise_frame(RegistrationFrame)
            username.set('')
            password.set('')
        else:
            messagebox.showinfo('Login', 'Login was unsuccessful')
            username.set('')
            password.set('')

#this function registers a team and team members
def registerteam():

    #get all of the data for the team and the members

    #presence
    if teamname.get()== '':
        messagebox.showinfo('Registration','Please enter team name')
    elif teammember1.get()== '':
        messagebox.showinfo('Registration','Please enter team member 1')
    else:
        response = messagebox.askyesno('Registration','Are you happy to register: \n' +
                                       '\n Team Name: ' + teamname.get()
                                       +'\n Team Member 1: ' + teammember1.get()
                                       +'\n Team Member 2: ' + teammember2.get()
                                       +'\n Team Member 3: ' + teammember3.get())

        if response == True:
            #write to a csv file
            with open('teams.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                #write the data
                writer.writerow([teamname.get(), teammember1.get(), teammember2.get(),teammember3.get()])
            csvfile.close()

            messagebox.showinfo('Registration',teamname.get() + ' has been registered')
            messagebox.showinfo('Registration', 'Begin Challenge 1')

            #change the view for the user to challenge 1
            raise_frame(Challenge1Frame)
        else:
            teamname.set('')
            teammember1.set('')

#this clears the registration frame
def clearregistration():
    teamname.set('')
    teammember1.set('')
                   
root = Tk()
root.title('Escape Room')
root.geometry('600x600')
root.config(bg = '#070945')

#Create frames for the program
LoginFrame = Frame(root, bg = '#070945')
RegistrationFrame = Frame(root,bg = '#070945')
Challenge1Frame = Frame(root, bg = '#070945')
Challenge2Frame = Frame(root, bg = '#070945')
Challenge3Frame = Frame(root, bg = '#070945')
LeaderboardFrame = Frame(root, bg = '#070945')


for frame in(LoginFrame,RegistrationFrame,Challenge1Frame,Challenge2Frame,Challenge3Frame,LeaderboardFrame):
    frame.grid(row = 0, column = 0, sticky = 'news')


#components for login
loginmainlabel = Label(LoginFrame, text = 'Decrypt Escape Rooms', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 48 bold')
loginmainlabel.grid(row = 0, column = 0, columnspan = 2)

#insert image
loginimage = 'decrypt_logo.png'
loginlogo = PhotoImage(file = loginimage)
smallerloginlogo = loginlogo.subsample(1,1)
loginlogolabel = Label(LoginFrame, image = smallerloginlogo)
loginlogolabel.grid(row =1, column =0, columnspan = 2)


#enter username and password
username = StringVar()
loginusernamelabel = Label(LoginFrame, text = 'Username: ', fg = '#070945', bg = '#e9cdb3', font = 'Verdana 24 bold')
loginusernamelabel.grid(row = 2, column = 0, sticky ='W', pady =10)
usernameentry = Entry(LoginFrame, textvariable = username, font = 'Verdana 22', width = 20)
usernameentry.grid(row = 2, column = 1, pady = 10)

#enter password
password = StringVar()
loginpasswordlabel = Label(LoginFrame, text = 'Password: ', fg = '#070945', bg = '#e9cdb3', font = 'Verdana 24 bold')
loginpasswordlabel.grid(row = 3, column = 0,sticky = 'W', pady = 10)
passwordentry = Entry(LoginFrame, textvariable = password, font = 'Verdana 22', width = 20)
passwordentry.grid(row = 3, column = 1, pady = 10)

#create buttons for login screen
loginsubmit = Button(LoginFrame, text = 'Submit', fg = '#070945', bg = '#e9cdb3', width = 15, font = 'Verdana 18 bold', command = gotoregistrationframe)
loginsubmit.grid(row = 4, column = 0, pady = 10)
                    
loginclear = Button(LoginFrame, text = 'Clear', fg = '#070945', bg = '#e9cdb3', width = 15, font = 'Verdana 18 bold', command = clearloginframe)
loginclear.grid(row = 4, column = 1, pady = 10)

loginexit = Button(LoginFrame, text = 'Exit Program', fg = '#070945', bg = '#e9cdb3', width = 15, font = 'Verdana 18 bold', command = exitprogram)
loginexit.grid(row = 5, column = 0, pady = 10, columnspan = 2)

#components for registration frame
regmainlabel = Label(RegistrationFrame, text = 'Decrypt Escape Rooms', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 48 bold')
regmainlabel.grid(row = 0, column = 0, columnspan = 2)

#insert image
regimage = 'team logo 1.png'
escapelogo = PhotoImage(file = regimage)
smallerescapelogo = escapelogo.subsample(1,1)
reglogolabel = Label(RegistrationFrame, image = smallerescapelogo)
reglogolabel.grid(row = 1, column = 0, columnspan = 2)

#insert labels and entry boxes
teamnamelabel = Label(RegistrationFrame, text = 'Enter team name: ', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 24 bold')
teamnamelabel.grid(row = 2, column = 0, sticky = 'W', pady = 10)
teamname = StringVar()
teamnameentry = Entry(RegistrationFrame, textvariable = teamname, font = 'Verdana 22', width = 20)
teamnameentry.grid(row = 2, column = 1, pady = 10)

teammember1label = Label(RegistrationFrame, text = 'Team member 1: ', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 24 bold')
teammember1label.grid(row = 3, column = 0, sticky = 'W', pady = 10)
teammember1 = StringVar()
teammember1entry = Entry(RegistrationFrame, textvariable = teammember1, font = 'Verdana 22', width = 20)
teammember1entry.grid(row = 3, column = 1, pady = 10)

teammember2label = Label(RegistrationFrame, text = 'Team member 2: ', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 24 bold')
teammember2label.grid(row = 4, column = 0, sticky = 'W', pady = 10)
teammember2 = StringVar()
teammember2entry = Entry(RegistrationFrame, textvariable = teammember2, font = 'Verdana 22', width = 20)
teammember2entry.grid(row = 4, column = 1, pady = 10)

teammember3label = Label(RegistrationFrame, text = 'Team member 3: ', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 24 bold')
teammember3label.grid(row = 5, column = 0, sticky = 'W', pady = 10)
teammember3 = StringVar()
teammember3entry = Entry(RegistrationFrame, textvariable = teammember3, font = 'Verdana 22', width = 20)
teammember3entry.grid(row = 5, column = 1, pady = 10)

registerteambutton = Button(RegistrationFrame, text = 'Register', fg = '#070945', bg = '#e9cdb3', width = 15, font = 'Verdana 18 bold', command = registerteam)
registerteambutton.grid(row = 6, column = 0)

clearteambutton = Button(RegistrationFrame, text = 'Clear', fg = '#070945', bg = '#e9cdb3', font = 'Verdana 18 bold', command = clearregistration)
clearteambutton.grid(row = 6, column = 1)

#############################################################################################################################################################################################
#Insert title to Challenge 1 Frame

challenge2title_label = Label(Challenge2Frame, text = 'Decrypt Escape Rooms - Quiz', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 36 bold')
challenge2title_label.grid(row = 0, column = 0, columnspan = 2)


# Define the quiz questions and answers
quiz_data = [
    {"question": "Question 1: Who won the 1938 Football World Cup?", "options": ["West Germany", "Italy", "France", "Brazil"], 'correct_option': 'Italy'},
    {"question": "Question 2: Which M&M colour is the rarest?", "options": ["Colourless", "Brown", "Blue", "Orange"], "correct_option": 'Brown'},
    {"question": "Question 3: What is Arachibutyrophobia a fear of?", "options": ["Peanut butter sticking on the roof of the mouth", "Spiders", "Apples", "Keys"], "correct_option": 'Peanut butter sticking on the roof of the mouth'},
    {"question": "Question 4: Which exercise puts most mechanical leverage on the lumbar part of the lats?", "options": ["Mag grip pulldown", "Single arm neutral row", "Incline Barbell Row", "Walking"], "correct_option": 'Mag grip pulldown'},
    {"question": "Question 5: What dessert did Spongebob and Patrick get in the first movie?", "options": ["Ice cream", "Crabby Patty delight", "Goober berry", "Triple Gooberberry Sunrise"], "correct_option": 'Triple Gooberberry Sunrise'},
    {"question": "Question 6: Where did the crown go in the first Spongebob movie?", "options": ["Crusty Krab", "Shell City", "Chum Bucket", "Gary's shell"], "correct_option": 'Shell City'},
    {"question": "Question 7: Who was the boss at the Grotto?", "options": ["Midas", "Brutus", "Jules", "Deadpool"], "correct_option": 'Brutus'},
    {"question": "Question 8: Who are the time twins in Lego Ninjago?", "options": ["The Clock Bros", "Tick and Tock", "Krux and Acronix", "None of the above"], "correct_option": 'Krux and Acronix'},
    {"question": "Question 9: Who has the most European goals excluding friendlies?", "options": ["CR7", "Suarez", "Messi", "Harry Maguire"], "correct_option": 'Messi'},
    {"question": "Question 10: What is season 5 of Ninjago called?", "options": ["Uncharted", "Tournament of Elements", "Legacy of the Green Ninja", "Possession"], "correct_option": 'Possession'},

    # Add more questions and options here
]

# Create variables to store user's answers
user_answers = [StringVar() for _ in range(len(quiz_data))]

# Function to check answers
def check_answers():
    score = 0
    for i, question_data in enumerate(quiz_data):
        user_answer = user_answers[i].get()
        correct_option = question_data['correct_option']
        if user_answer == correct_option:
            score += 1

    messagebox.showinfo('Quiz Result', f'Your score: {score}/{len(quiz_data)}')

# Create labels and dropdown menus for each question
for i, question_data in enumerate(quiz_data):
    question_label = Label(Challenge2Frame, text=question_data['question'], fg='#e9cdb3', bg='#070945', font='Verdana 18 bold')
    question_label.grid(row=i+2, column=0, sticky='W', pady=10)
   
    options = question_data['options']
    user_answer = user_answers[i]

    # Create a dropdown menu with options
    dropdown = ttk.Combobox(Challenge2Frame, values=options, textvariable=user_answer)
    dropdown.grid(row=i+2, column=1, pady=10)

import threading

# Create a StringVar to store the remaining time
remaining_time = StringVar()
remaining_time.set("Time: 60")



# Function to update the timer label
def update_timer():
    time_left = 60
    while time_left > 0:
        remaining_time.set(f"Time: {time_left}")
        time_left -= 1
        time.sleep(1)
    messagebox.showinfo('Time Up', 'Time is up!')
    check_answers()  # Automatically check answers when time is up

# Create a label for the timer
timer_label = Label(Challenge2Frame, textvariable=remaining_time, fg='#070945', bg='#e9cdb3', font='Verdana 18 bold')
timer_label.grid(row= 1, column= 1, columnspan=2, pady=10)

# Function to start the timer thread
def start_timer():
    timer_thread = threading.Thread(target=update_timer)
    timer_thread.start()

# Create a submit button to check answers
submit_button = Button(Challenge2Frame, text='Submit', fg='#070945', bg='#e9cdb3', width=15, font='Verdana 18 bold', command=check_answers)
submit_button.grid(row=len(quiz_data) + 2, column=0, columnspan=2, pady=10)

# Create a start timer button to start the timer and check answers
start_button = Button(Challenge2Frame, text='Start Timer', fg='#070945', bg='#e9cdb3', width=30, font='Verdana 18 bold', command=start_timer)
start_button.grid(row = 1, column = 0, columnspan=2, pady=10)

#Create a proceed button to Challenge2Frame
proceed_button = Button(Challenge2Frame, text = 'Proceed', fg = '#070945', bg = '#e9cdb3', width = 30, font = 'Verdana 18 bold', command= lambda: raise_frame(Challenge3Frame))
proceed_button.grid(row = 13, column = 0, columnspan = 2, pady = 10)


############################################################################################################################################################################################
#Create the title for Challenge1Frame
challenge1title_label = Label(Challenge1Frame, text = 'Decrypt Escape Rooms - Reaction Test', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 36 bold')
challenge1title_label.grid(row = 0, column = 0, columnspan = 2)

start_time = 0

test_started = False

def start_reaction_test():
    global start_time, test_started
    if not test_started:
        test_started = True
        start_button.config(state='disabled')
        proceed_button.config(state='disabled')
        delay = random.uniform(1, 5)
        root.after(int(delay * 1000), change_box_colour)

def change_box_colour():
    global start_time
    reaction_time_label.config(text="Reaction Time: ")
    green_box.config(bg="green")
    start_time = time.time()
 

def check_reaction_time(event):
    global start_time
    reaction_time = time.time() - start_time
    if green_box.cget('bg') == 'green' and reaction_time <= 0.45:
        reaction_time_label.config(text=f'Reaction Time: {reaction_time:.2f} seconds')
        proceed_button.config(state="normal")
    else:
        reaction_time_label.config(text=f'Reaction Time: {reaction_time:.2f} seconds')
        proceed_button.config(state="disabled")
  



# Create a label that represents the box
green_box = tk.Label(Challenge1Frame, text="Click when it turns green", width=30, height=10, bg="red")
green_box.bind("<Button-1>", check_reaction_time)
green_box.grid(row=3, column=0, pady=10)

# Create a button to start the reaction test
start_button = tk.Button(Challenge1Frame, text="Start Reaction Test", fg='#070945', bg='#e9cdb3', width=30, font='Verdana 18 bold', command=start_reaction_test)
start_button.grid(row=4, column=0, pady=10)

# Create a label to display reaction time
reaction_time_label = tk.Label(Challenge1Frame, text="Reaction Time: ", fg='#e9cdb3', bg='#070945', font='Verdana 18 bold')
reaction_time_label.grid(row=2, column=0, pady=10)

# Create a button to proceed to the next challenge (initially disabled)
proceed_button = tk.Button(Challenge1Frame, text="Proceed", fg='#070945', bg='#e9cdb3', width=30, font='Verdana 18 bold', state="disabled", command= lambda: raise_frame(Challenge2Frame))
proceed_button.grid(row=5, column=0, pady=10)

###################################################################################################################################################################################################
#Create title for Challenge3Frame
challenge3title_label = Label(Challenge3Frame, text = 'Decrypt Escape Rooms - Whack a Mole', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 36 bold')
challenge3title_label.grid(row = 0, column = 0, columnspan = 2)

from tkinter import Canvas, IntVar

# Create a Canvas for the Whack-a-Mole game
whack_a_mole_canvas = Canvas(Challenge3Frame, width=400, height=400, bg='#070945')
whack_a_mole_canvas.grid(row=1, column=0, columnspan=2)

# List to keep track of mole objects
mole_objects = []

# Variable to keep track of the score
score = IntVar()
score.set(0)

# Function to create a new mole
def create_mole():
    x = random.randint(50, 350)
    y = random.randint(50, 350)
    mole = whack_a_mole_canvas.create_oval(x, y, x + 50, y + 50, fill='#e9cdb3')
    mole_objects.append(mole)
    # After a delay, remove the mole
    Challenge3Frame.after(2000, lambda mole=mole: whack_a_mole_canvas.delete(mole))

# Function to start the game and gradually create moles
def start_whack_a_mole_game():
    number_of_moles = 0
    duration = 25  # Set the game duration in seconds
    update_score()

    def create_moles():
        nonlocal number_of_moles
        if number_of_moles < duration:
            create_mole()
            number_of_moles += 2  # Adjust the rate of mole appearance
            Challenge3Frame.after(2000, create_moles)

    create_moles()

# Function to update the score label
def update_score():
    score_label.config(text=f'Score: {score.get()}')

# Function to handle mole click event
def mole_click(event):
    for mole in mole_objects:
        if whack_a_mole_canvas.coords(mole)[0] < event.x < whack_a_mole_canvas.coords(mole)[2] and \
           whack_a_mole_canvas.coords(mole)[1] < event.y < whack_a_mole_canvas.coords(mole)[3]:
            whack_a_mole_canvas.delete(mole)
            mole_objects.remove(mole)
            score.set(score.get() + 1)
            update_score()

# Create a Start button to begin the game
start_whack_a_mole_button = Button(Challenge3Frame, text='Start Whack-a-Mole', fg='#070945', bg='#e9cdb3', width=30, font='Verdana 18 bold', command=start_whack_a_mole_game)
start_whack_a_mole_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a label to display the score
score_label = Label(Challenge3Frame, text=f'Score: {score.get()}', fg='#e9cdb3', bg='#070945', font='Verdana 18 bold')
score_label.grid(row=3, column=0, columnspan=2, pady=10)

# Bind the mole_click function to canvas click event
whack_a_mole_canvas.bind("<Button-1>", mole_click)

raise_frame(LoginFrame)
root.mainloop()
