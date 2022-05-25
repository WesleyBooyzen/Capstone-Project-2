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
        user = input("Enter your username: ")
        password = input("Enter your password: ")

        for i in range(len(total_users)):
            if user and password in total_users[i]:
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
        if user != "admin":
            print("Only admin can add new users.")
        elif user == 'admin':
            new_user = input("Enter a new username: ")
            new_pass = input("Enter a new password: ")
            new_pass_confirm = input("Please confrim new password: ")
            f.write(f'\n{new_user}, {new_pass}')
            print("User registerd successfully.")
        elif new_pass != new_pass_confirm:
            print("Passwords do not macth.")

    f.close()

# open the tasks file to add tasks when user inputs 'a'
    g = open("tasks.txt", 'a+')

# display the input options the user must undergo if user chooses "a"
    if menu_options == "a":
        user_task = input("Enter username to which the task will be assigned: ")
        task_title = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ")
        due_date = input("Enter the due date for the assigned task: ")
        assign_date = input("Enter the date the task was assigned: ")
        complete = input("Is the task completed: ")
        g.write(f'\n{user_task},{task_title},{description},{due_date},{assign_date},{complete}')

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
            for line in g:
                user_task, task_title, description, due_date, assign_date, complete = line.split(",")
                if user_task == user:
                    print(f''' 
Assigned to:                    {user_task}
Task:                           {task_title}
Task description:               {description}
Due date:                       {due_date}
Date assigned:                  {assign_date}
Task Complete?                  {complete}
''')

# if username == admin, the admin will get access to a different menue
# where admin can see the statistics of how many tasks and users are
# registered
    elif menu_options == "s":
        if user != "admin":
            print("Only admins can access statistics.")
        elif user == "admin":
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
