#Where all of the libraries needed to create the controlled assessment
from tkinter import *
from tkinter import ttk
import csv
import random
import datetime
import time
from tkinter import messagebox
from datetime import date
import tkinter as tk
from tkinter.simpledialog import askstring
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
import pandas as pd

#changes the users view
def raise_frame(frame):
    frame.tkraise()

def raise_game_frame(frame):
    selected_player = StringVar()
    player_label = Label(frame, text = 'Select Player: ', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 24 bold')
    player_label.grid(row = 0, column = 4, padx=110)
    dropdown = ttk.Combobox(frame, values=thePlayers, textvariable=selected_player)
    dropdown.grid(row=0, column=10, pady=10)

    def on_player_selected(event):
        global selected
        selected = selected_player.get()
        if selected in thePlayers:
            thePlayers.remove(selected)
            dropdown['values'] = thePlayers

    dropdown.bind("<<ComboboxSelected>>", on_player_selected)

    frame.tkraise()

# raise leaderboard frame (needs own function as must call populate before)
def raise_leadeboard_frame():
    LeaderboardFrame.tkraise()
    record_score(theTeamName, scores)
    populate_treeview(tree)
    populate_treeview2(tree2)
    calc_average_score()

# record score
def record_score(name, scores):
    total = scores[0][1] + scores[1][1] + scores [2][1]
    with open("scores.csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([name, total, scores[0][0], scores[0][1], scores[1][0], scores[1][1], scores[2][0], scores[2][1]])

def calc_average_score():
    df = pd.read_csv('scores.csv')
    average1 = df.iloc[:, 3].mean()
    average2 = df.iloc[:, 5].mean()
    average3 = df.iloc[:, 7].mean()

    game1ave.set(int(average1))
    game2ave.set(int(average2))
    game3ave.set(int(average3))

def next_team():
    
    scores.clear()

    # reset c1
    global start1_time, test1_started
    test1_started = False
    start1_time = 0
    reaction_time_label.config(text="Reaction Time: ")
    green_box.config(bg="red")
    start_button.config(state="normal")
    proceed_button.config(state="disabled")

    # reset c2
    for dropdown in dropdowns:
        dropdown.set('')

    # reset c3
    score_label["text"] = f"Score: {0}"

    clearregistration()
    raise_frame(RegistrationFrame)

def clear_data():
    # Read the header from the CSV file
    with open('scores.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header

    # Truncate the CSV file while preserving the header
    with open('scores.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header back to the file

    populate_treeview(tree)
    populate_treeview2(tree2)
    
    game1ave.set('')
    game2ave.set('')
    game3ave.set('')

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
    global theTeamName
    global thePlayers
    #get all of the data for the team and the members

    #presence
    if teamname.get()== '':
        messagebox.showinfo('Registration','Please enter team name')
    elif teammember1.get()== '':
        messagebox.showinfo('Registration','Please enter team member 1')
    elif teammember2.get()== '':
        messagebox.showinfo('Registration','Please enter team member 2')
    elif teammember3.get()== '':
        messagebox.showinfo('Registration','Please enter team member 3')

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

            # set global variables

            theTeamName = teamname.get()
            thePlayers = [teammember1.get(), teammember2.get(), teammember3.get()]

            messagebox.showinfo('Registration',teamname.get() + ' has been registered')
            messagebox.showinfo('Registration', 'Begin Challenge 1')

            #change the view for the user to challenge 1
            raise_game_frame(Challenge1Frame)
        else:
            teamname.set('')
            teammember1.set('')
            teammember2.set('')
            teammember3.set('')

#this clears the registration frame
def clearregistration():
    teamname.set('')
    teammember1.set('')
    teammember2.set('')
    teammember3.set('')

# intialize variables
global scores
scores = []
theTeamName = ""
                        
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
passwordentry = Entry(LoginFrame, textvariable = password, font = 'Verdana 22', show='*', width = 20)
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
    {"question": "Q 1: Who won the 1938 Football World Cup?", "options": ["West Germany", "Italy", "France", "Brazil"], 'correct_option': 'Italy'},
    {"question": "Q 2: Which M&M colour is the rarest?", "options": ["Colourless", "Brown", "Blue", "Orange"], "correct_option": 'Brown'},
    {"question": "Q 3: What is Arachibutyrophobia a fear of?", "options": ["Peanut butter sticking on the roof of the mouth", "Spiders", "Apples", "Keys"], "correct_option": 'Peanut butter sticking on the roof of the mouth'},
    {"question": "Q 4: Which exercise puts most mechanical leverage on the lumbar part of the lats?", "options": ["Mag grip pulldown", "Single arm neutral row", "Incline Barbell Row", "Walking"], "correct_option": 'Mag grip pulldown'},
    {"question": "Q 5: What dessert did Spongebob and Patrick get in the first movie?", "options": ["Ice cream", "Crabby Patty delight", "Goober berry", "Triple Gooberberry Sunrise"], "correct_option": 'Triple Gooberberry Sunrise'},
    {"question": "Q 6: Where did the crown go in the first Spongebob movie?", "options": ["Crusty Krab", "Shell City", "Chum Bucket", "Gary's shell"], "correct_option": 'Shell City'},
    {"question": "Q 7: Who was the boss at the Grotto?", "options": ["Midas", "Brutus", "Jules", "Deadpool"], "correct_option": 'Brutus'},
    {"question": "Q 8: Who are the time twins in Lego Ninjago?", "options": ["The Clock Bros", "Tick and Tock", "Krux and Acronix", "None of the above"], "correct_option": 'Krux and Acronix'},
    {"question": "Q 9: Who has the most European goals excluding friendlies?", "options": ["CR7", "Suarez", "Messi", "Harry Maguire"], "correct_option": 'Messi'},
    {"question": "Q 10: What is season 5 of Ninjago called?", "options": ["Uncharted", "Tournament of Elements", "Legacy of the Green Ninja", "Possession"], "correct_option": 'Possession'},

    # Add more questions and options here
]

# Create variables to store user's answers
user_answers = [StringVar() for _ in range(len(quiz_data))]

# Function to check answers
def check_answers():
    current_time2 = datetime.datetime.now()
    # Calculate the difference
    time_difference = current_time2 - current_time1

    # Get the difference in seconds
    difference_in_seconds = time_difference.total_seconds()
    if (difference_in_seconds >= 60):
            messagebox.showinfo('Over 60 seconds', f'Fail!\nScore: 0')
            challenge1score = 0
    else:
        challenge1score = 0
        for i, question_data in enumerate(quiz_data):
            user_answer = user_answers[i].get()
            correct_option = question_data['correct_option']
            if user_answer == correct_option:
                challenge1score += 1

        messagebox.showinfo('Quiz Result', f'Your score: {challenge1score}/{len(quiz_data)}')

    score = (challenge1score/len(quiz_data)) * 100
    scores.append((selected, int(score)))


# Create labels and dropdown menus for each question
dropdowns = []

for i, question_data in enumerate(quiz_data):
    question_label = tk.Label(Challenge2Frame, text=question_data['question'], fg='#e9cdb3', bg='#070945', font='Verdana 12 bold')
    question_label.grid(row=i+2, column=0, sticky='W', pady=5)
   
    options = question_data['options']
    user_answer = user_answers[i]

    # Create a dropdown menu with options
    dropdown = ttk.Combobox(Challenge2Frame, values=options, textvariable=user_answer)
    dropdown.grid(row=i+2, column=1, pady=10)
    
    # Append the dropdown widget to the list
    dropdowns.append(dropdown)

# Create a label for the timer
timer_label = Label(Challenge2Frame, text="You have 60 seconds!", fg='#070945', bg='#e9cdb3', font='Verdana 18 bold')
timer_label.grid(row= 1, column= 2, pady=10, padx=15)

# Function to start the timer
def start_timer():
    global current_time1
    current_time1 = datetime.datetime.now()
    
# Create a submit button to check answers
submit_button = Button(Challenge2Frame, text='Submit', fg='#070945', bg='#e9cdb3', width=15, font='Verdana 18 bold', command=check_answers)
submit_button.grid(row=len(quiz_data) + 2, column=0, columnspan=2, pady=10)

# Create a start timer button to start the timer and check answers
start_button = Button(Challenge2Frame, text='Start Timer', fg='#070945', bg='#e9cdb3', width=30, font='Verdana 18 bold', command=start_timer)
start_button.grid(row = 1, column = 0, columnspan=2, pady=10)

#Create a proceed button to Challenge2Frame
proceed_button = Button(Challenge2Frame, text = 'Proceed', fg = '#070945', bg = '#e9cdb3', width = 30, font = 'Verdana 18 bold', command= lambda: raise_game_frame(Challenge3Frame))
proceed_button.grid(row = 13, column = 0, columnspan = 2, pady = 10)


############################################################################################################################################################################################

#Create the title for Challenge1Frame
challenge1title_label = Label(Challenge1Frame, text = 'Decrypt Escape Rooms - Reaction Test', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 36 bold')
challenge1title_label.grid(row = 0, column = 0, columnspan = 2)

start1_time = 0

test1_started = False

def start_reaction_test():
    global start1_time, test1_started
    if not test1_started:
        test1_started = True
        start_button.config(state='disabled')
        proceed_button.config(state='disabled')
        delay = random.uniform(1, 5)
        root.after(int(delay * 1000), change_box_colour)

def change_box_colour():
    global start1_time
    reaction_time_label.config(text="Reaction Time: ")
    green_box.config(bg="green")
    start1_time = time.time()
 

def check_reaction_time(event):
    global start1_time
    reaction_time = time.time() - start1_time
    if green_box.cget('bg') == 'green' and reaction_time <= 0.5:
        reaction_time_label.config(text=f'Reaction Time: {reaction_time:.2f} seconds')
        proceed_button.config(state="normal")
        # record score 
        score = (1 - reaction_time) * 100
        scores.append((selected, int(score)))

    else:
        reaction_time_label.config(text=f'Reaction Time: {reaction_time:.2f} seconds')
        proceed_button.config(state="disabled")

# selected_player = StringVar()
# dropdown = ttk.Combobox(Challenge1Frame, values=players, textvariable=selected_player)
# dropdown.grid(row=2, column=1, pady=10)


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
proceed_button = tk.Button(Challenge1Frame, text="Proceed", fg='#070945', bg='#e9cdb3', width=30, font='Verdana 18 bold', state="disabled", command= lambda: raise_game_frame(Challenge2Frame))
proceed_button.grid(row=5, column=0, pady=10)

###################################################################################################################################################################################################
#variables for challange 3
score = 0
game_running = False
game_duration = 60  # in seconds
mole_buttons = []

# fucntions for challange 3
def start_game():
    global moleScore, game_running
    moleScore = 0
    game_running = True
    update_score_label()
    Challenge3Frame.after(game_duration * 1000, end_game)
    randomly_populate_moles()

def end_game():
    global game_running
    game_running = False
    score = (moleScore/100) * 100
    messagebox.showinfo("Game Over", f"Game Over! You hit {moleScore} moles. \n Your final score is {int(score)}!")
    scores.append((selected, int(score)))
    proceed_to_leaderboard_button.config(state="normal")
    reset_moles()

def randomly_populate_moles():
    if game_running:
        for mole_button in mole_buttons:
            mole_button["state"] = tk.NORMAL
            mole_button["text"] = ""
            mole_frame.after(random.randint(1000, 3000), lambda button=mole_button: show_mole(button))

def show_mole(button):
    time = 1000 # adjust for how long moles stay on screen (ms)
    if game_running:
        button["text"] = "Mole"
        button["state"] = tk.NORMAL
        mole_frame.after(time, lambda b=button: hide_mole(b))

def hide_mole(button):
    if game_running:
        button["text"] = ""
        button["state"] = tk.DISABLED
        mole_frame.after(random.randint(1000, 3000), lambda b=button: show_mole(b))

def whack_mole(row, col):
    if game_running:
        button = mole_buttons[row * 3 + col]
        if button["text"] == "Mole":
            global moleScore
            moleScore += 1
            update_score_label()
            hide_mole(button)

def update_score_label():
    score_label["text"] = f"Score: {moleScore}"

def reset_moles():
    for mole_button in mole_buttons:
        mole_button["text"] = ""
        mole_button["state"] = tk.DISABLED

# frame componetes for Challenge3Frame
#Create title for Challenge3Frame
challenge3title_label = Label(Challenge3Frame, text = 'Decrypt Escape Rooms - Whack a Mole', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 36 bold')
challenge3title_label.grid(row = 0, column = 0, columnspan = 2)

# mole_frame
mole_frame = Frame(Challenge3Frame, width=400, height=400, bg='#070945')
mole_frame.grid(row=1, column=0, columnspan=2)

# set up grid for game
for row in range(3):
    for col in range(3):
        button = tk.Button(mole_frame, text="Mole", width=10, height=3, command=lambda r=row, c=col: whack_mole(r, c))
        button.grid(row=row, column=col)
        mole_buttons.append(button)

    score_label = tk.Label(mole_frame, text="Score: 0", fg='#e9cdb3', bg='#070945', font='Verdana 18 bold')
    score_label.grid(row=3, column=0, columnspan=2, pady=10)

# Create a Start button to begin the game
start_whack_a_mole_button = Button(Challenge3Frame, text='Start Whack-a-Mole', fg='#070945', bg='#e9cdb3', width=30, font='Verdana 18 bold', command=start_game)
start_whack_a_mole_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a Proceed to Leaderboard button (initially disabled)
proceed_to_leaderboard_button = Button(Challenge3Frame, text='Proceed to Leaderboard', fg='#070945', bg='#e9cdb3', width=30, font='Verdana 18 bold', state='disabled', command=lambda: raise_leadeboard_frame())
proceed_to_leaderboard_button.grid(row=4, column=0, columnspan=2, pady=10)

######################################################################################################################################################################################################################################
# LeaderboardFrame
# variables for leadboard frame

# fucntions for leaderbaord frame

def populate_treeview(tree):
    # Clear existing rows in the treeview
    for row in tree.get_children():
        tree.delete(row)

    # Read data from the CSV file and populate the TreeView
    with open("scores.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Skip header
        next(csv_reader)

        # Read data into a list of tuples
        data = [row for row in csv_reader]

        # Sort data based on the first column (assuming it contains numerical values)
        sorted_data = sorted(data, key=lambda x: int(x[1]), reverse=True) 

        # Populate the TreeView with sorted data
        for row in sorted_data:
            # Insert only the first two columns into the TreeView
            tree.insert("", "end", values=(row[0], row[1]))


def populate_treeview2(tree2):
    # Clear existing rows in the treeview
    for row in tree2.get_children():
        tree2.delete(row)

    # Read data from the CSV file and populate the TreeView
    with open("scores.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Skip header
        next(csv_reader)

        # Populate the TreeView with data from the first two columns
        for row in csv_reader:
            # Insert only the first two columns into the TreeView
            tree2.insert("", "end", values=(row[2], row[3], row[4], row[5], row[6], row[7]))



# gui
#Create title for LeaderboardFrame
LeaderboardFrame_label = Label(LeaderboardFrame, text = 'Decrypt Escape Rooms - Leaderboard', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 36 bold')
LeaderboardFrame_label.grid(row = 0, column = 0, columnspan = 2)

# team tree
tree = ttk.Treeview(LeaderboardFrame)

# Define columns
tree["columns"] = ("Team Name", "Total Score")

# Column configurations
tree.column("#0", width=0, stretch=tk.NO)  # hidden column
tree.column("Team Name", anchor=tk.W, width=150)
tree.column("Total Score", anchor=tk.CENTER, width=100)

# Column headings
tree.heading("#0", text="", anchor=tk.W)
tree.heading("Team Name", text="Team Name", anchor=tk.W)
tree.heading("Total Score", text="Total Score", anchor=tk.CENTER)

# grid treeview
tree.grid(row=1, column=0, sticky='w', padx=40, pady=10, rowspan=3)

# player tree
# team tree
tree2 = ttk.Treeview(LeaderboardFrame)

# Define columns
tree2["columns"] = ("Player 1", "Game 1", "Player 2",  "Game 2", "Player 3", "Game 3")

# Column configurations
tree2.column("#0", width=0, stretch=tk.NO)  # hidden column
tree2.column("Player 1", anchor=tk.CENTER, width=75)
tree2.column("Game 1", anchor=tk.CENTER, width=50)
tree2.column("Player 2", anchor=tk.CENTER, width=75)
tree2.column("Game 2", anchor=tk.CENTER, width=50)
tree2.column("Player 3", anchor=tk.CENTER, width=75)
tree2.column("Game 3", anchor=tk.CENTER, width=50)

# Column headings
tree2.heading("#0", text="", anchor=tk.W)
tree2.heading("Player 1", text="Team Member", anchor=tk.CENTER)
tree2.heading("Game 1", text="Game 1", anchor=tk.CENTER)
tree2.heading("Player 2", text="Team Member", anchor=tk.CENTER)
tree2.heading("Game 2", text="Game 2", anchor=tk.CENTER)
tree2.heading("Player 3", text="Team Member", anchor=tk.CENTER)
tree2.heading("Game 3", text="Game 3", anchor=tk.CENTER)

tree2.grid(row=4, column=0, sticky="nsew", pady= 10, columnspan=5)
# average times leaderBoardFrame
# average time variables
game1ave = StringVar()
game2ave = StringVar()
game3ave = StringVar()

game1_average_label = Label(LeaderboardFrame, text = 'Game 1 Average:', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 16 bold')
game1_average_label.grid(row = 1, column = 1, sticky= 'w')

game1_averageData_label = Label(LeaderboardFrame, textvariable=game1ave, fg = '#e9cdb3', bg = '#070945', font = 'Verdana 16 bold')
game1_averageData_label.grid(row = 1, column = 2, sticky= 'w')

game2_average_label = Label(LeaderboardFrame, text = 'Game 2 Average:', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 16 bold')
game2_average_label.grid(row = 2, column = 1, sticky= 'w')

game2_averageData_label = Label(LeaderboardFrame, textvariable=game2ave, fg = '#e9cdb3', bg = '#070945', font = 'Verdana 16 bold')
game2_averageData_label.grid(row = 2, column = 2, sticky= 'w')

game3_average_label = Label(LeaderboardFrame, text = 'Game 3 Average:', fg = '#e9cdb3', bg = '#070945', font = 'Verdana 16 bold')
game3_average_label.grid(row = 3, column = 1, sticky= 'w')

game3_averageData_label = Label(LeaderboardFrame, textvariable=game3ave, fg = '#e9cdb3', bg = '#070945', font = 'Verdana 16 bold')
game3_averageData_label.grid(row = 3, column = 2, sticky= 'w')

next_team_button = Button(LeaderboardFrame, text='Next Team', fg='#070945', bg='#e9cdb3', width=30, font='Verdana 18 bold', command=next_team)
next_team_button.grid(row=5, column=2, sticky= 'w',ipadx=10, ipady=10, padx=10, pady=10)

clear_data_button = Button(LeaderboardFrame, text='Clear Data', fg='#070945', bg='#e9cdb3', width=30, font='Verdana 18 bold', command=clear_data)
clear_data_button.grid(row=6, column=2, sticky= 'w',ipadx=10, ipady=10, padx=10, pady=10)

raise_frame(LoginFrame)
root.mainloop()
