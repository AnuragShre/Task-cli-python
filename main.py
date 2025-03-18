import datetime





class Task:
    
    number_of_task = 0
    
    def __init__(self,description,status): #initializing
        Task.number_of_task += 1
        self.description = description
        self.id = str(Task.number_of_task)
        self.status = status
        self.created_at = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M %Y"))
        self.modified_at = self.created_at


def new_task(): #function to make new task 
    d = input("Describe your task: ")
    s = input("Set Status (1 = ongoing ; 2 = Done): ")
    if s=="1" or s=="2":
        tasks = Task(description = d,status=s)
    else:
        print("Enter a valid status choice")
        new_task()
    return tasks
    
def view_task(task):
    print("****************************")
    print(f"Description: {task.description}\nid: {task.id}\ncreated: {task.created_at}\nmodified: {task.modified_at}")
    
    if task.status == "1":
        task.status ="Ongoing..."
        print("Ongoing...")
    else:
        print("Done")
        task.status = "Done."
    print("")
    print("****************************")

def welcome():
    print("***********************")
    print("* Welcome To Task-Cli *")
    print("***********************")

def main():


    print("\nPress (1) to add a task\nPress (2) to edit it\nPress (3) to delete it\nPress (4) to list all tasks")
    choice = input("(1/2/3/4): ")
    if choice == "1":
        add_newtask()
        main()
    elif choice == "2":
        edit_task()
        main()
    elif choice=="3":
        delete()
        main()
    elif choice=="4":
        list_tasks()
        main()
    else:
        print("Please enter a vaild choice")
        main()



def add_newtask():
    
    tasks.append(new_task())
    choice = input("Would you like to view all tasks(y/n) :")
    if choice == "y" or choice == "Y":
        list_tasks()
    else:
        main()
   
def edit_task():
    choice = input("what would you like to edit?\nDescription(d)\nstatus(s)\n: ").lower()    
    if choice == "d" or choice == "s":
        print("List of all available tasks: ")
        list_tasks()
        if choice == "d":
            task_id = input("Enter task ID: ")
            for i in range(len(tasks)):
        
                if tasks[i].id == task_id:
                    new_desc = input("Enter new description: ")
                    tasks[i].description = new_desc
                    tasks[i].modified_at =  str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M %Y"))
    
        elif choice == "s":
            task_id = input("Enter task ID: ")
            for i in range(len(tasks)):
    
                if tasks[i].id == task_id:
                    new_s = input("Set Status (1 = ongoing ; 2 = Done): ")
                    if new_s == "1":
                        tasks[i].status = "Ongoing..."
                    else:
                        tasks[i].status = "Done."
                    tasks[i].modified_at =  str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M %Y"))
    else:
        print("Please enter a valid choice")
        edit_task()                


def delete():
    list_tasks()
    task_id = input("Task ID of task you want to delete: ")
    for i in range(len(tasks)):
        if tasks[i].id == task_id:  
            tasks.pop(i)  
    if len(tasks)==0:
        print("Empty")


def list_tasks():
    for i in range(len(tasks)):
        print("**************")
        print(f"* Task ID: {tasks[i].id} *")
        view_task(tasks[i])
    if len(tasks)==0:
        print("Empty")





if __name__ == "__main__":
    tasks = []
    welcome()
    main()