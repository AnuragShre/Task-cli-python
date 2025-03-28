import datetime
import os.path
import json


class Task:

    number_of_task = 0
    
    def __init__(self,description,status,id,created_at,modified_at): #initializing
        Task.number_of_task += 1
        self.description = description
        self.id = str(Task.number_of_task)
        self.status = status
        if os.path.exists("data.json"):
            self.created_at= created_at
            self.modified_at= modified_at
            
def new_task(): #function to make new task 
    d = input("Describe your task: ")
    s = input("Set Status (1 = ongoing ; 2 = Done): ")
    ct = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M %Y"))
    mt = ct
    if s=="1" or s=="2":
        tasks = Task(description = d,status=s,id= Task.number_of_task,created_at=ct,modified_at=mt)
    else:
        print("Enter a valid status choice")
        new_task()
    return tasks
    
def view_task(task):
    print("=============================")
    print(f"Description: {task.description}\nid: {task.id}\ncreated: {task.created_at}\nmodified: {task.modified_at}")
    
    if task.status == "1":
        task.status ="Ongoing..."
        print("Ongoing...")
    else:
        print("Done")
        task.status = "Done."
    print("=============================")

def welcome():
    print("========================")
    print("| Welcome To Task-Cli  |")
    print("========================")

def main():
    

    print("\nPress (1) to add a task\nPress (2) to edit it\nPress (3) to delete it\nPress (4) to list all tasks\nPress (5) to filter search")
    choice = input("(1/2/3/4/5): ")
    if choice == "1":
        add_newtask()
        
    elif choice == "2":
        edit_task()
        
    elif choice=="3":
        delete()
        
    elif choice=="4":
        list_tasks()
        
    elif choice == "5":
        fil()
        
    else:
        print("Please enter a vaild choice")
    save_system()
    
    main()
    
   
   
def save_system():
    data = []
    with open("data.json", "w") as file:
        for i in range(len(tasks)):
            data2 = { 
                "des": tasks[i].description,
                "status": tasks[i].status,
                "id":tasks[i].id,
                "cd":tasks[i].created_at,
                "md":tasks[i].modified_at
                }
            data.append(data2)
        json.dump(data,file)

    
        
    
    
def load_system():
    with open('data.json', 'r') as file:
        dic = json.load(file)
        for i in range(len(dic)):
            task = Task(description=dic[i]["des"],status=dic[i]["status"],id=dic[i]["id"],created_at=dic[i]["cd"],modified_at=dic[i]["md"])
            tasks.append(task)




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
        print("==============")
        print(f"| Task ID: {tasks[i].id} |")
        view_task(tasks[i])
    if len(tasks)==0:
        load_system()


def fil():#filter
    a = input("1 = List of Ongoing tasks\n2 = List of Completed tasks\n")
    print("================")
    for i in range(len(tasks)):
        if a == "1" and tasks[i].status=="Ongoing...":
            print(f"Status:({tasks[i].status}) {tasks[i].description}")  
        elif a == "2" and tasks[i].status=="Done." :
            print(f"Status:({tasks[i].status}) {tasks[i].description}")  
    print("================")    

    if len(tasks)==0:
        print("Empty")
    





if __name__ == "__main__":
    tasks = []







    welcome()
    if not os.path.exists("data.json"):
        save_system()
    else:
        load_system()
   
    main()