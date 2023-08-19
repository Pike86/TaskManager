from Modules import ScreenClearModule

#Stock text for change directory
#cd C:\Users\apike\OneDrive\Desktop\Coding\Python Course\TaskManager

#==============
#==============
#ADMINISTRATION
#==============
#==============

#----------
#----------
#Task Lists
#----------
#----------
tasks = [
    #--------------------------
    #List to Store Active Tasks
    #--------------------------
    [

    ],

    #-----------------------------
    #List to Store Completed Tasks
    #-----------------------------
    [

    ],

    #-----------------------------
    #List to Store Cancelled Tasks
    #-----------------------------
    [

    ]
]


isRepeated = 0

menus = [
    "Active",
    "Completed",
    "Cancelled",
    "New Task"
]

taskStatuses = [
    "Active",
    "Completed",
    "Cancelled"
]

#-------------------------------------------
#Function to Clear Screen and Display Header
#-------------------------------------------
def clearAndDisplayHeader():
    ScreenClearModule.clear()
    print("========================")
    print("Task Manager Application")
    print("========================")
    print("")

#----------------------------
#Function to Check for 'Quit'
#----------------------------
quitCounter = 0
def checkForQuit():
    clearAndDisplayHeader()
    print("----")
    print("Quit")
    print("----")
    print("")
    #First Display a Message.
    #If the user entered an invalid response in the previous quit attempt, the program will prompt them to provide a better response, and will provide more specific instructions."
    global quitCounter

    if(quitCounter==0):
        quitResponse = input("Are you sure you want to quit? 'Y' or 'N'?")

    elif(quitCounter>0):
        quitResponse = input("Sorry I don't understand your response.\nAre you sure you want to quit? Enter 'Y' or 'N', without quotes.")
        quitCounter = 0

    quitResponseUpper = quitResponse.upper()
    #Having presented the prompt, take the user's response.
    #If the user fails to enter 'y' or 'n', reset the function. See the above comment.
    if(quitResponseUpper=="Y"):
        ScreenClearModule.clear()
        print("Thanks for using the Waterframe Games Task Management App!")
        exit()

    elif(quitResponseUpper=="N"):
        displayMenu("Main")

    else:
        quitCounter = 1
        checkForQuit()

#=================
#=================
#MAKING SELECTIONS
#=================
#=================

#-----------------------------------
#Function to Process Menu Selections
#-----------------------------------
def makeSelection(menuID):
    global isRepeated
    if(isRepeated==0):
        selection = input("Please make your selection. (Ex. '1', '2', etc.)\nType 'M' to return to the main menu.\nType 'Q' to quit.")
    elif(isRepeated==1):
        selection = input("Sorry, I don't understand your response. Please select one of the above options(Ex. '1', '2', etc.)\nType 'M' to return to the main menu.\nType 'Q' to quit.")
        isRepeated=0
    if selection.isdigit():
        number = int(selection)
        displayMenu(menus[number-1])
    else:
        selectionUpper = selection.upper()
        if(selectionUpper=="M"):
            displayMenu("Main")
        elif(selectionUpper=="Q"):
            checkForQuit()
        else:
            clearAndDisplayHeader()
            isRepeated=1
            makeSelection(menuID)

#-------------------------------------------------------------
#Function to Calculate Characters for Tasks and Display Dashes
#-------------------------------------------------------------
def calculateDashes(dictionary, key, keyID):
    value = dictionary[key]
    IDvalue = dictionary[keyID]
    length = len(value)+8+len(str(IDvalue))
    dashes = "-" * length
    return dashes


#-------------------------
#Function to Display Menus
#-------------------------
taskCounter = 1
def taskPrintout(ID):
    print(calculateDashes(ID,"Title","ID"))
    print("Task " + str(ID["ID"]) + " - " + ID["Title"])
    print(calculateDashes(ID,"Title","ID"))
    print(ID["Description"]+"\n")

tempTaskID = 0
def taskSelection(ID):
    global isRepeated
    print("-----------")
    print("REVIEW/EDIT")
    print("-----------")
    print(" ")
    if(isRepeated==0):
        selectedTask = input("With which task would you like to interact? (Ex. '1', '2', etc.)\nType 'M' to return to the main menu.\nType 'Q' to quit.")
    else:
        isRepeated=0
        selectedTask = input("Sorry. I don't understand your response. With which task would you like to interact? (Ex. '1', '2', etc.)\nType 'M' to return to the main menu.\nType 'Q' to quit.")
    if selectedTask.isdigit():
        number = int(selectedTask)
        taskReviewPrompt(ID, number-1)
    else:
        selectionUpper =  selectedTask.upper()
        if(selectionUpper=="M"):
            displayMenu("Main")
        elif(selectionUpper=="Q"):
            checkForQuit()
        else:
            clearAndDisplayHeader()
            isRepeated=1
            taskSelection(ID)

newLocation = [5,5]
reviewSelections=[1]
isRepeated = 0
def taskReviewPrompt(ID, theSelectedTask):
    global newLocation
    global isRepeated
    clearAndDisplayHeader()
    print("-----------")
    print("REVIEW/EDIT")
    print("-----------")

    if(ID==0):
        print("1.) Mark Task as 'Complete'")
        print("2.) Mark Task as 'Cancelled'")
        newLocation = [1,2]
    elif(ID==1):
        print("1.) Restore Task to 'Active'")
        print("2.) Mark Task as 'Cancelled'")
        newLocation = [0,2]
    elif(ID==2):
        print("1.) Restore Task to 'Active'")
        print("2.) Mark Task as 'Complete'")
        newLocation = [0,1]

    if(isRepeated==0):
        choice = input("Please make your selection.(Ex. '1', '2', etc.)\nType 'M' to return to the main menu.\nType 'Q' to quit.")
    else:
        print("")
        choice = input("Sorry, I don't understand your selection. Please select from the above options (Ex. '1', '2', etc.)\nType 'M' to return to the main menu.\nType 'Q' to quit.")
        isRepeated=0
    if choice.isdigit():
        actionSelection = int(choice)-1
        print("Let's append tasks[" + str(ID) + "][" + str(theSelectedTask) + "] to tasks " + str(newLocation[actionSelection]) + " and remove it from " + str(ID))
        tasks[newLocation[actionSelection]].append(tasks[ID][theSelectedTask])
        tasks[ID].pop(theSelectedTask)
        input("Click to proceed")
        clearAndDisplayHeader()
    else:
        selectionUpper =  choice.upper()
        if(selectionUpper=="M"):
            displayMenu("Main")
        elif(selectionUpper=="Q"):
            checkForQuit()
        else:
            isRepeated=1
            taskReviewPrompt(ID,theSelectedTask)
            clearAndDisplayHeader()

def displayMenu(menuID):
    clearAndDisplayHeader()
    if(menuID=="Main"):
        print("---------")
        print("Main Menu")
        print("---------")
        print("")
        print("1.) View Active Tasks")
        print("2.) View Completed Tasks")
        print("3.) View Cancelled Tasks")
        print("4.) Create a New Task")

    elif(menuID=="Active"):
        print("------------")
        print("ACTIVE TASKS")
        print("------------")
        print("")
        for x in tasks[0]:
            taskPrintout(x)
        taskSelection(0)

    elif(menuID=="Completed"):
        print("---------------")
        print("COMPLETED TASKS")
        print("---------------")
        print("")
        for x in tasks[1]:
            taskPrintout(x)
        taskSelection(1)

    elif(menuID=="Cancelled"):
        print("---------------")
        print("CANCELLED TASKS")
        print("---------------")
        print("")
        for x in tasks[2]:
            taskPrintout(x)
        taskSelection(2)

    elif(menuID=="New Task"):
        print("-----------------")
        print("Create a New Task")
        print("-----------------")
        print("")
        global taskCounter
        newTaskID = taskCounter
        newTaskTitle = input("Task " + str(taskCounter) + " - Title: ")
        newTaskDescription = input("Task " + str(taskCounter) + " - Description: ")
        tasks[0].append({"ID": newTaskID, "Title": newTaskTitle, "Description": newTaskDescription, "Status":taskStatuses[0]},)
        taskCounter+=1

    print("")
    makeSelection(menuID)

#============
#============
#TITLE SCREEN
#============
#============

#----------------------------------------------
#Clear the Console and Display the Title Screen
#----------------------------------------------
clearAndDisplayHeader()
print("Waterframe Games - 2023")
print("")
input("Press Enter to Continue")
clearAndDisplayHeader()
displayMenu("Main")

#=================
#=================
#DISPLAY MAIN MENU
#=================
#=================
#displayMenu("Tasks")

#Trying Number Selections - Will Convert to Module
#def menuSelection(selection):
#    selection
