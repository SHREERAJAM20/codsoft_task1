def display_menu():
    print("\nTo-Do list Menu")
    print("1.Add tasks")
    print("2.View tasks")
    print("3.Remove tasks")
    print("4.Exit")

def add_task(tasks): 
       task=input("Enter the task: ")
       tasks.append(task)
       print(f"Task '{task}' added")

def view_task(tasks):
      if tasks:
            print("\nYour To-Do List")
            for index,task in enumerate(tasks,start=1):
                print(f"{index}. {task}")
      else:
            print("There is no tasks added")      

def remove_task(tasks):
      view_task(tasks)
      if tasks:
            try:
                task_number=int(input("Enter the task number: "))
                if 1<= task_number <= len(tasks):
                     remove_task=tasks.pop(task_number-1)
                     print(f"Task {remove_task} removed from list")
                else:
                      print("Invalid task number")
            except ValueError:
                  print("Provide valid task number")

def main():
      tasks=[]
      while True:
            display_menu()
            choice=input("Enter the option: ")
            if choice=='1':
                  add_task(tasks)
            elif choice=='2':
                  view_task(tasks)      
            elif choice=='3':
                  remove_task(tasks)
            elif choice=='4':
                  print("Good Bye!!")
                  break    
            else:
                  print("Choose valid option")

if __name__=="__main__":
      main()
