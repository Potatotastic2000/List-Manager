UserLists = [["red", "blue", "yellow"], ['square', 'tringle', 'circle']]
ListNames = ["colors", "shapes"]

#repeat: "yes" or "no"
#options: create a list of options or type "StringInput" or "IntegerInput" and have just one action
#actions: create a list of functions with a corresponding index to the options list
#exitcode (optional): create a string that will be used to stop the loop
def edit_list(repeat, options, actions, SelectedList, ListSelection, exitcode="*********************"):
    new_list = []
    choosing = True
    while choosing:
        userchoice = input("> ")
        if userchoice == exitcode:
            choosing = False
        else:
            if options.__contains__(userchoice.lower):
                new_list = actions[options.index(userchoice.lower)]((SelectedList, ListSelection))

                #if repeat is set to no, the user is done choosing once they have selected an option
                if repeat == "no":
                    choosing = False
            else:
                print("")
                print("(", userchoice, ")", "is not a valid option")
                print("please type one of these options: ", options, "or type", exitcode)
    return new_list

def user_choice(repeat, options, actions="", exitcode="*********************"):
    choosing = True
    while choosing:
        userchoice = input("> ")
        if userchoice == exitcode:
            choosing = False
        else:
            if options.__contains__(userchoice):
                actions[options.index(userchoice)]()
                #if repeat is set to no, the user is done choosing once they have selected an option
                if repeat == "no":
                      choosing = False
            elif options == "NewList":
                ListNames.append(userchoice)
                UserLists.append([])
                SelectedList = (UserLists[ListNames.index(userchoice)])
                addItem((SelectedList))
            else:
                print("")
                print("(", userchoice, ")", "is not a valid option")
                print("please type one of these options: ", options, "or type", exitcode)


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
    print("Here is the new list: ", SelectedList)
    print("")
    print("Type 'add' or 'delete'. Type 'done' when you are finished editing")
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
                if len(SelectedList) == 1:
                    print("")
                    print(
                        "You are attempting to delete the last item in this list, doing so will delete the list entirely. Are you sure you wish to continue?")
                    print("Type 'yes' or 'no'")
                    confirming = True
                    while confirming:
                        userconfirm = input("> ")
                        if userconfirm == userconfirm.lower() == "yes":
                            UserLists.pop(ListNames.index(ListSelection))
                            ListNames.pop(ListNames.index(ListSelection))
                            edit_menu()
                            confirming = False
                        elif userconfirm == "no" or "No":
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
    print("Type 'add' or 'delete'. Type 'done' when you are finished editing")
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





'''
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

██████╗░███████╗██╗░░░░░███████╗████████╗███████╗       ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
██╔══██╗██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔════╝       ████╗░████║██╔════╝████╗░██║██║░░░██║
██║░░██║█████╗░░██║░░░░░█████╗░░░░░██║░░░█████╗░░       ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║░░██║██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░       ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██████╔╝███████╗███████╗███████╗░░░██║░░░███████╗       ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚══════╝       ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
'''





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

    print("Type 'add' or 'delete'. Type 'done' when you are finished editing")
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
    user_choice("no", "NewList")
    print("Add some items to your List: ")

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
    print("Here are a list of commands you can use:")
    print("")
    print("View: view a list")
    print("Create: create a new list")
    print("Edit: edit a list's contents")
    print("Delete: delete an existing list")
    print("Exit: exit the program")
    print("")
    print("")
 #   user_choice("yes", ["View", "Create", "Edit", "Delete", "Exit"], [view_menu])

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