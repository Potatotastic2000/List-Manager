
UserLists = []
ListNames = []


def edit_list(repeat, options, actions, SelectedList, ListSelection, exitcode="Exit"):
    new_list = SelectedList
    choosing = True
    while choosing:
        print("Type 'add' or 'delete'. Type 'done' when you are finished editing")
        userchoice = input("> ")
        if userchoice == exitcode and repeat == "yes":
            choosing = False
        else:
            if options.__contains__(userchoice.lower()):
                new_list = actions[options.index(userchoice.lower())]((SelectedList, ListSelection))
            else:
                print("")
                print("(!)  (", userchoice, ")", "is not a valid option")
                if repeat.lower() == "yes":
                    print("please type one of these options: ", options, "or type", exitcode)
                if repeat.lower() == "no":
                    print("please type one of these options: ", options)
    return new_list

'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

██╗░░░██╗░██████╗███████╗██████╗░       ░█████╗░██╗░░██╗░█████╗░██╗░█████╗░███████╗░░██╗██╗░░
██║░░░██║██╔════╝██╔════╝██╔══██╗       ██╔══██╗██║░░██║██╔══██╗██║██╔══██╗██╔════╝░██╔╝╚██╗░
██║░░░██║╚█████╗░█████╗░░██████╔╝       ██║░░╚═╝███████║██║░░██║██║██║░░╚═╝█████╗░░██╔╝░░╚██╗
██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗       ██║░░██╗██╔══██║██║░░██║██║██║░░██╗██╔══╝░░╚██╗░░██╔╝
╚██████╔╝██████╔╝███████╗██║░░██║       ╚█████╔╝██║░░██║╚█████╔╝██║╚█████╔╝███████╗░╚██╗██╔╝░
░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝       ░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░╚════╝░╚══════╝░░╚═╝╚═╝░░
'''



#        -----------PARAMETERS-------------

#repeat: "yes" or "no"
#options: create a list of options with a corresponding 'actions' index to run a function when they choose an option or type "StringInput" to return the users input
#actions: create a list of functions with a corresponding index to the options list
#exitcode (optional): create a string that will be used to stop the loop

def user_choice(repeat, options, actions=[], exitcode="Exit"):
    choosing = True
    while choosing:
        userchoice = input("> ")

        #check to see if the user has entered the exit code and stop wants to stop choosing
        if userchoice == exitcode and repeat == "yes":
            choosing = False

#           ----------RUN SPECIFIED ACTION------------

        else:
            if options != "StringInput" and options != "IntegerInput":
                #try to run the specified action corresponding to the options provided
                if options.__contains__(userchoice.lower()):
                    actions[options.index(userchoice)]()

                    #if the action runs and repeat is set to no, the user is done choosing an option once they have selected one
                    if repeat == "no":
                          choosing = False

#              ---------INVALID INPUT-----------

                else:
                    print("")
                    # inform the user that they have entered something wrong and remind them of the options and exit code
                    print("(!)  (", userchoice, ")", "is not a valid option")
                    if repeat.lower() == "yes":
                        print("please type one of these options: ", options, "or type", exitcode)
                    if repeat.lower() == "no":
                        print("please type one of these options: ", options)

#            ---------STRING INPUT-------------
            else:
                if options == "StringInput":
                    #make sure the user didn't put blank space
                    if userchoice.isspace() == False and userchoice != "":
                        return userchoice
                    else:
                        print("(!) You must provide text here ")
                        create_menu()

'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
'''


def printlist(SelectedList):
    for x in enumerate(SelectedList):
        print(str(x[0] + 1) + ".", x[1])

def say(text):
    print(str(text))


def addItem(parametertuple):
    SelectedList = parametertuple[0]
    print("")
    print("Type a new item and press 'enter'")
    print("Type '!exit' when you are finished adding items")
    newitem = ""
    while newitem != "!exit":
        newitem = input("> ")
        if newitem != "!exit":
            print("added!")
            SelectedList.append(newitem)
    if SelectedList[0] == "placeholder":
        SelectedList.pop(0)
    print("\nHere is the new list: ", SelectedList)
    print("")
    return SelectedList


def deleteItem(parametertuple):
    SelectedList = parametertuple[0]
    ListSelection = parametertuple[1]
    print("")
    printlist(SelectedList)
    print(
        "Type the number of the item you would like to delete. Type '!exit' when you are finished deleting items")
    deleting = True
    while deleting:
        itemselection = (input("> "))
        try:
            if (int(itemselection) > 0) and (int(itemselection) <= len(SelectedList)) and (
                    len(SelectedList) >= 1):

                #delete the list if the last item is deleted
                if len(SelectedList) == 1:
                    print("")
                    #warn the user of their actions
                    print(
                        "You are attempting to delete the last item in this list, doing so will delete the list entirely. Are you sure you wish to continue?")
                    print("Type 'yes' or 'no'")
                    confirming = True
                    while confirming:
                        userconfirm = input("> ")
                        if userconfirm.lower() == "yes":
                            UserLists.pop(ListNames.index(ListSelection))
                            ListNames.pop(ListNames.index(ListSelection))
                            edit_menu()
                            confirming = False
                        elif userconfirm.lower() == "no":
                            confirming = False
                            edit_menu()
                        else:
                            print("(", userconfirm, ")", "is not a valid input")
                            print("")
                            print("Type 'yes' or 'no'")
                else:
                    SelectedList.pop(int(itemselection) - 1)
                    print("")
                    printlist(SelectedList)
            else:
                print("(", itemselection, ")", "is not a valid input")
        except ValueError:
            if itemselection == "!exit":
                deleting = False
            else:
                print("(", itemselection, ")", "is not a valid input")
    return SelectedList






'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

███████╗██╗░░██╗██╗████████╗        ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
██╔════╝╚██╗██╔╝██║╚══██╔══╝        ████╗░████║██╔════╝████╗░██║██║░░░██║
█████╗░░░╚███╔╝░██║░░░██║░░░        ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██╔══╝░░░██╔██╗░██║░░░██║░░░        ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
███████╗██╔╝╚██╗██║░░░██║░░░        ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░        ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
'''



def exit_menu():
    print("\nThank you for using List Maker!")
    exit(0)

'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

██████╗░███████╗██╗░░░░░███████╗████████╗███████╗       ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
██╔══██╗██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔════╝       ████╗░████║██╔════╝████╗░██║██║░░░██║
██║░░██║█████╗░░██║░░░░░█████╗░░░░░██║░░░█████╗░░       ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║░░██║██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░       ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██████╔╝███████╗███████╗███████╗░░░██║░░░███████╗       ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚══════╝       ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
'''



def delete_menu():
    print("Here are your current lists: ")
    print(ListNames)
    print("")

    # user selects the list they want to delete
    print("Which list would you like to delete? ")
    print("Type the name of the list or type '!exit' to go back ")
    ListSelection = input("> ")
    if ListSelection == "!exit":
        print("")
        options_menu()
    try:
        SelectedList = (UserLists[ListNames.index(ListSelection)])
    except:
        print("\n\n\n(!) This list does not exist\n")
        delete_menu()
        return
    UserLists.pop(UserLists.index(SelectedList))
    ListNames.pop(ListNames.index(ListSelection))
    print("Deleted!")
    print("")
    options_menu()

'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
'''






'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

███████╗██████╗░██╗████████╗        ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
██╔════╝██╔══██╗██║╚══██╔══╝        ████╗░████║██╔════╝████╗░██║██║░░░██║
█████╗░░██║░░██║██║░░░██║░░░        ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██╔══╝░░██║░░██║██║░░░██║░░░        ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
███████╗██████╔╝██║░░░██║░░░        ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚══════╝╚═════╝░╚═╝░░░╚═╝░░░        ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
'''

#TODO: There is no way to edit the name of a list
#TODO: User is stuck in the menu if there is no list to select

def edit_menu():
    print("Here are your current lists: ")
    print(ListNames)
    print("")

    #user selects the list they want to edit
    ListSelection = input("Which list would you like to edit? ")
    try:
        SelectedList = (UserLists[ListNames.index(ListSelection)])
    except:
        print("\n\n\n(!) This list does not exist\n")
        edit_menu()
        return
    print(str(ListSelection) + ":", SelectedList)
    print("")


    SelectedList = edit_list("yes", ["add", "delete"], [addItem, deleteItem], SelectedList, ListSelection, "done")
    print("Here is the new list: ", SelectedList)

    options_menu()

'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
'''






'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

░█████╗░██████╗░███████╗░█████╗░████████╗███████╗       ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝       ████╗░████║██╔════╝████╗░██║██║░░░██║
██║░░╚═╝██████╔╝█████╗░░███████║░░░██║░░░█████╗░░       ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║░░██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░██╔══╝░░       ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░███████╗       ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝       ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
'''



def create_menu():
    print("\nName your new list: ")
    newlist = user_choice("no", "StringInput")
    for x in ListNames:
        if x == newlist:
            print("(!) You already have a list named", "(", newlist, ")")
            create_menu()
    ListNames.append(newlist)
    UserLists.append(["placeholder"])
    SelectedList = (UserLists[ListNames.index(newlist)])
    ListSelection = newlist
    print("\n\nAdd some items to this list:")
    addItem((SelectedList, ListSelection))
    options_menu()
'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
'''






'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

██╗░░░██╗██╗███████╗░██╗░░░░░░░██╗      ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
██║░░░██║██║██╔════╝░██║░░██╗░░██║      ████╗░████║██╔════╝████╗░██║██║░░░██║
╚██╗░██╔╝██║█████╗░░░╚██╗████╗██╔╝      ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
░╚████╔╝░██║██╔══╝░░░░████╔═████║░      ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
░░╚██╔╝░░██║███████╗░░╚██╔╝░╚██╔╝░      ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
░░░╚═╝░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░      ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
'''



def view_menu():
    print("Here are your current lists: ")
    print(ListNames)
    print("")

    # user selects the list they want to view
    ListSelection = input("Which list would you like to view? ")
    try:
        SelectedList = (UserLists[ListNames.index(ListSelection)])
    except:
        print("\n\n\n(!) This list does not exist\n")
        view_menu()
        return
    print("\n\n\n\n")
    print(str(ListSelection) + ":", SelectedList)
    print("")
    options_menu()

'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
'''






'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

░█████╗░██████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗       ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝       ████╗░████║██╔════╝████╗░██║██║░░░██║
██║░░██║██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░       ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║░░██║██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗       ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
╚█████╔╝██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝       ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░       ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
'''



def options_menu():
    print("Here is a list of commands you can use:")
    print("")
    print("View: view a list")
    print("Create: create a new list")
    print("Edit: edit a list's contents")
    print("Delete: delete an existing list")
    print("Exit: exit the program")
    print("")
    print("")
    user_choice("no", ["view", "create", "edit", "delete", "exit"], [view_menu, create_menu, edit_menu, delete_menu, exit_menu])

'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
'''






'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

██████╗░██████╗░░█████╗░░██████╗░██████╗░░█████╗░███╗░░░███╗        ░██████╗░█████╗░██████╗░██╗██████╗░████████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗████╗░████║        ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝
██████╔╝██████╔╝██║░░██║██║░░██╗░██████╔╝███████║██╔████╔██║        ╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║        ░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║        ██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝        ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░
'''



print("")
print("""
██╗░░░░░██╗░██████╗████████╗        ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░
██║░░░░░██║██╔════╝╚══██╔══╝        ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
██║░░░░░██║╚█████╗░░░░██║░░░        ██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
██║░░░░░██║░╚═══██╗░░░██║░░░        ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
███████╗██║██████╔╝░░░██║░░░        ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║
╚══════╝╚═╝╚═════╝░░░░╚═╝░░░        ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝
""")

print("Start by creating a list:")
print("")
create_menu()

'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
'''