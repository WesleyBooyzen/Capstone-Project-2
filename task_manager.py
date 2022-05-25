from fileinput import close
from linecache import getline

# create a list with all tasks and users
total_users = []
total_tasks = []
details = False

# open both user and task files
with open("user.txt", 'r+') as f:
    for line in f:
        total_users.append(line.split())

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for i in range(len(total_users)):
            if username and password in total_users[i]:
                details = True

        if details == True:
            break
        else:
            print("Enter a valid username/ password.")

# if the inputs are valid, the program continues
while True:
    # print out the input the user must make in order to go forth the program
    menu_options = input('''Please select one of the following options:

r - Register a user
a - Adding a task
va - View all tasks
vm - View my tasks
s - View statistics
e - Exit
:''').lower()

# close the file
    f = open('user.txt', 'a+')

# display menu inputs if user inputs the key "r"
    if menu_options == 'r':
        if username != "admin":
            print("Only admin can add new users.")
        elif username == 'admin':
            new_user = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            new_password_confirm = input("Please confrim new password: ")
            f.write(f'\n{new_user}, {new_password}')
            print("User registerd successfully.")
        elif new_password != new_password_confirm:
            print("Passwords do not macth.")

    f.close()

# open the tasks file to add tasks when user inputs 'a'
    g = open("tasks.txt", 'a+')

# display the input options the user must undergo if user chooses "a"
    if menu_options == "a":
        task_username = input("Enter username to which the task will be assigned: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        due_date = input("Enter the due date for the assigned task: ")
        assign_date = input("Enter the date the task was assigned: ")
        complete = input("Is the task completed: ")
        g.write(f'\n{task_title},{task_username},{assign_date},{due_date},{complete},{task_description}\n')

        g.close()

# display the input options the user must undergo if user chooses "va"
    elif menu_options == "va":
        with open("tasks.txt", 'r') as g:
            for viewing in g:
                view_names = viewing.strip()
                print(view_names)
        g.close()

# display the input options the user must undergp if the user chooses "vm"
    elif menu_options == "vm":
        with open("tasks.txt", 'r') as g:
            lines = g.readlines()

        user_tasks = []
        for line in lines:
            try:
                line = line.split(',')
                if line[1] == username.strip():
                    user_tasks.append(line)
            except IndexError:
                continue

        for line in user_tasks:
            username = line[1]
            task = line[0]
            task_description = line[5]
            task_assigned = line[2]
            due_date = line[3]
            task_completion = line[4]
            print("Task username: ", username, 
                    '\nTask: ', task, 
                    '\nTask Description: ', task_description, 
                    '\nDate Assigned: ', task_assigned, 
                    '\nTask Due Date: ', due_date, 
                    '\nTask Compeleted: ', task_completion)
            break

# if username == admin, the admin will get access to a different menue
# where admin can see the statistics of how many tasks and users are
# registered
    elif menu_options == "s":
        if username != "admin":
            print("Only admins can access statistics.")
        elif username == "admin":
            user_count = "user.txt"
            counting = 0
            with open('user.txt', 'r') as f:
                for line in f:
                    counting += 1
            print("Total users are: ", counting)

# create function to count the number of tasks in the file
            task_count = "tasks.txt"
            task_counting = 0
            with open('tasks.txt', 'r') as g:
                for line in g:
                    task_counting += 1
            print("Total tasks are: ", task_counting)


# exit the whole program if the user enters the key "e"
    elif menu_options == "e":
        print('Goodbye!!!')
        break

# if user does not input one of following in menu, print out a message
    else:
        print("You have made a wrong choice, Please Try again")
