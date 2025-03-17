import datetime


class Task:
    
    number_of_task = 0
    
    def __init__(self,description,*args,**kwargs): #initializing
        Task.number_of_task += 1
        self.description = description
        self.id = Task.number_of_task
        self.status = status
        self.createdAt = str(datetime.now(timezone.utc))
        self.modifiedAt = self.createdAt

        for key, val in kwargs.items():
            if key == "description":
                self.description = val
            if key == "status":
                self.status = val
            if key == "createdAt" and val is not None:
                self.created_at = val
            if key == "modifiedAt" and val is not None:
                self.updated_at = val



def main():
    task = Task(description = "hello",status="on")
    print(task)





if __name__ == "__main__":
    main()