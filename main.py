import datetime





class Task:
    
    number_of_task = 0
    
    def __init__(self,description,status): #initializing
        Task.number_of_task += 1
        self.description = description
        self.id = Task.number_of_task
        self.status = status
        self.created_at = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M %Y"))
        self.modified_at = self.created_at


def new_task(): #function to make new task 
    d = input("Describe your task: ")
    s = input("Set Status (1 = ongoing ; 2 = Done): ")
    if s=="1" or s=="2":
        task = Task(description = d,status=s)
    else:
        print("Enter a valid status choice")
        new_task()
    return task
    
def view_task(task):
    print("\n")
    print(f"Description: {task.description}\nid: {task.id}\ncreated: {task.created_at}\nmodified: {task.modified_at}")
    print("\n")
    if task.status == "1":
        print("ongoing")
    else:
        print("done")
    print("\n")


def main():
    print("***********************")
    print("* Welcome To Task-Cli *")
    print("***********************")

    print("Press (1) to add a task\nPress (2) to edit it\nPress (3) to delete it")
    choice = input("(1/2/3): ")
    if choice == "1":
        add_newtask()
    elif choice == "2":
        pass
    elif choice=="3":
        pass
    else:
        print("Please enter a vaild choice")
        main()



def add_newtask():
    tasks = []
    tasks.append(new_task())
    for i in range(len(tasks)):
        view_task(tasks[i])
    
    
    





if __name__ == "__main__":
    main()