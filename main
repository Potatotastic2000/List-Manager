UserLists = [["red","blue","yellow"]]
ListNames = ["colors", "shapes"]



# MENUS


def editmenu():
    print("Here are your current lists: ")
    print(ListNames)
    print("")
    ListSelection = input("Which list would you like to edit? ")
    SelectedList = (UserLists[ListNames.index(ListSelection)])
    print(str(ListSelection) + ":", SelectedList)
    print("")

    def printlist():
        for x in SelectedList:
                print(str(SelectedList.index(x) + 1) + ".", x)


    useroption = ""
    while useroption != "done":
        print("Type 'add' or 'delete'. Type 'done' when you are finished editing")
        useroption = input("> ")
        if useroption == "add":
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
        if useroption == "delete":
            print("")
            printlist()
            print("Type the number of the item you would like to delete. Type '!exit' when you are finished deleting items")
            deleting = True
            while deleting:
                itemselection = (input("> "))               
                try: 
                    if len(SelectedList) == 1:
                        print("")
                        print("You are attempting to delete the last item in this list, doing so will delete the list entirely. Are you sure you wish to continue?")
                        print("Type 'yes' or 'no'")
                        confirming = True
                        while confirming:
                            userconfirm = input("> ")
                            if userconfirm == "yes" or "Yes":
                                UserLists.pop(ListNames.index(ListSelection))
                                ListNames.pop(ListNames.index(ListSelection))
                                optionsmenu()
                                confirming = False
                            elif userconfirm == "no" or "No":
                                confirming = False
                            else: 
                                print("(", userconfirm, ")", "is not a valid input")
                                print("")
                                print("Type 'yes' or 'no'")
                    if (int(itemselection) > 0) and (int(itemselection) <= len(SelectedList)) and (len(SelectedList) > 1):
                        SelectedList.pop(int(itemselection)-1)
                        print("")
                        printlist()   
                    else:
                        print("(", itemselection, ")", "is not a valid input")
                except ValueError:
                    if itemselection == "!exit":
                         deleting = False
                    else:
                        print("(", itemselection, ")", "is not a valid input")

                
                
            

            print("Here is the new list: ", SelectedList)
                
    optionsmenu()

    print("Type a new item and press 'enter'")
    print("Type '!done' when you are finished")
    while newitem != "!done":
        newitem = input("What would you like to add? ")

        
def optionsmenu():
    print("Here are a list of commands you can use:")
    print("")
    print("View: view a list")
    print("Create: create a new list")
    print("Edit: edit a list's contents")
    print("Delete: delete an existing list")
    print("Exit: exit the program")
    print("")
    print("")
    selectedoption = input("> ")
    if selectedoption == "Exit" or "exit":
        quit()




#PROGRAM SCRIPT

print("")
print("Welcome to List Maker!:")
print("Start by creating a list:")
print("")
editmenu()





