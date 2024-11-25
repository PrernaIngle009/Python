import pyfiglet
def task():
    tasks=[]
    ascii_art = pyfiglet.figlet_format("TO-DO LIST",width=200)
    print(ascii_art)
    total_task=int(input("Enter how many tasks you want to add = "))
    for i in range(1,total_task+1):
        values=input(f"Enter task {i} = ")
        tasks.append(values)
    print(f"Today's tasks are {tasks}")
     
    while True:
        operation=int(input("Enter 1-Add\n 2-Update\n 3-Delete\n 4-View \n 5-Exit/Stop"))
        if operation==1:
            add=input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been added successfully...")
        elif operation==2:
            update=input("Enter task you want to update = ")
            if update in tasks:
                up=input("Enter new task = ")
                ind=tasks.index(update)
                tasks[ind]=up
                print(f"Task {up} Updated...")
        elif operation==3:
            dele=input("Which task you want to delete = ")
            if dele in tasks:
                ind=tasks.index(dele)
                del tasks[ind]
                print(f"{dele} has been deleted successfully....")
        elif operation==4:
            print(f"Total tasks are = {tasks}")
        elif operation==5:
            print("Closing The Program......")
            break
                
                
        
task()