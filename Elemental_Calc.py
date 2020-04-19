def main_menu():
    print("1. List of Elements")
    print("2. Learn about Elements")
    print("3. Add Elements")
    print("4. Combine Elements")
    print("5. Exit Program")
    a = True
    while a:
        selection = int(input("Enter a # corresponding to what you would like to do:"))
        if selection == 1:
            list()
            a = False
        elif selection == 2:
            learn()
            a = False
        elif selection == 3:
            add()
            a = False
        elif selection == 4:
            combine()
            a = False
        elif selection == 5:
            a = False
        else:
            print("Option not yet available. Enter 1-4")
            main_menu()
    exit()


def list():
    print("Hydrogen, Helium, Boron, Carbon, Nitrogen, Oxygen")
    anykey = input("Enter anything to return to main menu")
    main_menu()


def learn():
    b = True
    while b:

        element_list = ["Hydrogen", "Helium", "Boron", "Carbon", "Nitrogen", "Oxygen"]
        print(element_list)
        element_select = int(input("Enter a number from 0-5 corresponding the element on the list:"))
        if element_select == 0:
            print("Hydrogen: Atomic number = 1 , Atomic mass = 1.0078 , Symbol = H")
            b = False
        elif element_select == 1:
            print("Helium: Atomic number = 2 , Atomic mass = 4.003 , Symbol = He")
            b = False
        elif element_select == 2:
            print("Boron: Atomic number = 5 , Atomic mass = 10.811 , Symbol = B")
            b = False
        elif element_select == 3:
            print("Carbon: Atomic number = 6 , Atomic mass = 12.0107 , Symbol = H")
            b = False
        elif element_select == 4:
            print("Nitrogen: Atomic number = 7 , Atomic mass = 14.0067 , Symbol = N")
            b = False
        elif element_select == 5:
            print("Oxygen: Atomic number = 8 , Atomic mass = 15.999 , Symbol = O")
            b = False
        else:
            print("Invalid choice. Enter 1-4:")
        anykey = input("Enter anything to return to main menu:")
        main_menu()
    exit()


def add():
    element_list = ["Hydrogen", "Helium", "Boron", "Carbon", "Nitrogen", "Oxygen"]
    element1 = int(input("Enter a number from 0-5 corresponding the element from the list:"))
    element2 = int(input("Enter another element:"))
    element_list[0] = 1.0078
    element_list[1] = 4.003
    element_list[2] = 10.811
    element_list[3] = 12.0107
    element_list[4] = 14.0067
    element_list[5] = 15.999
    print(element_list)
    print(format(element_list[element1] + element_list[element2], ".2f"))
    anykey = input("Enter anything to return to main menu:")
    main_menu()


def combine():
    element_list = ["Hydrogen", "Carbon", "Oxygen", "Copper", "Tin"]
    print(element_list)
    c = True
    while c:
        element1 = int(input("Enter a number from 0-4 corresponding to the element list:"))
        element2 = int(input("Enter another element number:"))
        if ((element1 == 0) and (element2 == 1)) or ((element1 == 1) and (element2 == 0)):
            print("Butane, Propane, and Methane all contain Hydrocarbon atoms!")
            c = False
        elif ((element1 == 0) and (element2 == 2)) or ((element1 == 2) and (element2 == 0)):
            print("Water, Carbon Monoxide, and Hydroxide are all composed of Hydrogen and Oxygen molecules!")
            c = False
        elif ((element1 == 1) and (element2 == 2)) or ((element1 == 2) and (element2 == 1)):
            print("Ozone, Perozide, and most common acids contain Carbon and Oxygen molecules.")
            c = False
        elif ((element1 == 0) and (element2 == 3)) or ((element1 == 3) and (element2 ==0)):
            print("Copper oxide, Chloride, and Sulfuric acid are all compounds that contain Hydrogen and Copper!")
            c = False
        elif ((element1 == 0) and (element2 == 4)) or ((element1 == 4) and (element2 == 0)):
            print("Hydrochloric acid and Sulfide are compounds that contain Hydrogen and Tin.")
            c = False
        elif ((element1 == 1) and (element2 == 3)) or ((element1 == 3) and (element2 == 1)):
            print("Cyanide and Copper salts are known as Organocopper compounds in organometallic chemistry!")
            c = False
        elif ((element1 == 1) and (element2 == 4)) or ((element1 == 4) and (element2 == 1)):
            print("Organotin compounds are highly toxic and have been used as biocides.")
            c = False
        elif ((element1 == 2) and (element2 == 3)) or ((element1 == 3) and (element2 == 2)):
            print("If Copper encounters itself with Oxygen then it begins to receive some physical reactions.")
            c = False
        elif ((element1 == 2) and (element2 == 4)) or ((element1 == 4) and (element2 == 2)):
            print("When tin reacts with oxygen it forms tin oxide which is white and insoluble in water.")
            c = False
        elif ((element1 == 3) and (element2 == 4)) or ((element1 == 4) and (element2 == 3)):
            print("When tin and copper are mixed together, they form a stronger metal called Bronze.")
            c = False
        else:
            print("Invalid Choice, choose from 0-4:")
        anykey = input("Enter anything to return to main menu:")
        main_menu()
    exit()


# main routine

main_menu()
