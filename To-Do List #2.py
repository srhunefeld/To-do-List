#Sam Hunefeld

#Functions
newlist = []
def addTask():
    task = input("What task do you want to add to your list?(please keep it in lowercase letters)")
    newlist.extend(task) 
    print("You have added " + task + " to your list")
    ans = input("Would you like to add another task to your list? yes(y) or no(n)")
    if ans == "y":
        addTask()
    else:
        program()
def removeTask():
    task = input("What task do you want to remove from your list?(please keep it in lowercase)")
    x = newlist.index(task)
    newlist.pop(x)
    print("You have removed " + task + " from your list")
    ans = input("Would you like to remove another task to your list? yes(y) or no(n)")
    if ans == "y":
        removeTask()
    else:
        program()
def viewList():
    print(newlist)
    ans = input("Would you like to view your list again? yes(y) or no(n)")
    if ans == "y":
        viewList()
    else:
        program()
def markTask():
    task = input("What task do you want to mark as finished on your list?")
    x = newlist.index(task)
    newlist.pop(x)
    y = task + " [X]"
    newlist.append(y)
    print("You have marked " + task + " as finish on your list")
    ans = input("Would you like to mark another task as finished on your list? yes(y) or no(n)")
    if ans == "y":
        removeTask()
    else:
        program()
def removeTasks():
    newlist.clear()
    print("All tasks have been removed.")
    program()
def alphabetizeTasks():
    newlist.sort()
    print("Your tasks have been organized alphabetically.")
    program()
def numberOfTasks():
    c = len(newlist)
    print(c)
    program()

def program():
    option = input("What would like to do?\nAdd a task (add)\nremove a taks (remove)\nView your to-do list(view)\nMark item as finished(mark)\nExit the program(exit)\nRemove all taks(remove_tasks)\nAlphabetize all taks(alphabetize)\nList the number of tasks in your list(number)")
    if option == "add":
        addTask()
    if option == "remove":
        removeTask()
    if option == "view":
        viewList()
    if option == "mark":
        markTask()
    if option == "remove_tasks":
        removeTasks()
    if option == "alphabetize":
        alphabetizeTasks()
    if option == "number":
        numberOfTasks()
    if option == "exit":
        exit()
#Main
program()