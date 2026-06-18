tasks=[]
while True:
    print("1.Add Task")
    print("2.View Task")
    print("3.Delete Task")
    print("4.Exit")

    choice=input("Enter the Choice:")
    if choice=="1":
        task=input("Enter the Task:")
        tasks.append(task)
        print("Task added Successfully")

    elif choice=="2":

        if len(tasks)==0:
            print("No Tasks Available")
        else:
            print("Tasks:")
            for index,task in enumerate(tasks):
                print(f"{index+1}. {task}")
    elif choice=="3":
        if len(tasks)==0:
            print("No Tasks Available")
        else:
            print("Tasks:")
            for index,task in enumerate(tasks):
                print(f"{index+1}. {task}")
            task_index=int(input("Enter the Task Number to Delete:"))
            if 1<=task_index<=len(tasks):
                deleted_task=tasks.pop(task_index-1)
                print(f"Task '{deleted_task}' Deleted Successfully")
            else:
                print("Invalid Task Number")
    elif choice=="4":
        print("Exiting the To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid Choice. Please Try Again.")
