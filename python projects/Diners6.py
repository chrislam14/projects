# Christopher Lam 29545944 and Gurkirat Kamboj 80519093 ICS 31 Lab sec. 1 Lab Assignment 6

## Developing the diners31 program 

"""
One way to organize:  The object-oriented way:
    We have Diners, we have a collection of Diners
    Diners can be created with user input, and printed, ...
    collections can be created, printed, searched, added to, ...
That refers primarily to how things are treated inside the program.
    We can call that the MODEL.
The user interface is the other part, called the VIEW.
We could start with either; the view lets us see stuff working
    from the beginning, so we'll start there.
"""
from collections import namedtuple  # It's customary to do this at top

## VIEW (USER INTERFACE) PORTION OF DINERS PROGRAM

def diners31() -> None:
    ''' Main program; starts up and finishes up. '''
    print("Welcome to the Diners Program")
    print()

    our_diners = []  # This is our collection of Diners
    our_diners = handle_commands(our_diners)  # Do everything
    print()
    print("Thank you.  Good-bye.")
    return

MENU = """
Diner collection Program --- Choose one
 n:  Add a new diner to the collection
 r:  Remove a diner from the collection
 s:  Search the collection for selected diners
 sc: Search for diners with a specific cuisine
 sp: Search for diners with a specific dish
 c: Change prices for the dishes served
 e: Remove (erase) all the diners from the collection
 p:  Print all the diners
 q:  Quit
"""

def handle_commands(diners: 'list of Diner') -> 'list of Diner':
    ''' Print menu, accept and execute commands to maintain list
    '''
    # This is a still more realistic program stub
    keep_going = True
    while keep_going:
        command = input(MENU)
        if command == 'q':
            keep_going = False       #  we're done
        elif command == 'n':
            r = diner_get_info()
            diners = collection_add(diners, r)
        elif command == 'r':
            n = input("Please enter the name of the diner" +
                      " to remove:  ")
            diners = collection_remove_by_name(diners, n)
        elif command == 's':
            n = input("Please enter the name of the diner" +
                      " to search for:  ")
            print(collection_to_str(collection_search_by_name(diners, n)))
        elif command == 'p':
            collection_print_format(diners)
        elif command == 'e':
            diners = []
            print("All diners have been erased")
        elif command == 'c':
            percentage = input("By what percentage would you like to change the price? ")
            collection_change_prices( diners, int(percentage))
            print ("The prices have been changed")
        elif command == 'sc':
            cuisine_search = input( "What kind of cuisine would you like to search for: ")
            collection_search_cuisine (diners, cuisine_search)
        elif command == 'sd':
            dish_search = input( "What dish would you like to search for: ")
            collection_search_dish (diners, dish_search)
        else:
            print("The command you typed, '", command, "', ",
                "isn't a valid command.  Please try again.", sep="")
    return diners

## MODEL PORTION OF DINERS PROGRAM

#DISH

Dish = namedtuple( "Dish", "name price calories")

dish1 = Dish( "Pizza", 2.85, 285)
dish2 = Dish("Burger", 3.25, 354)
dish3 = Dish("Spaghetti", 8.13, 221)

def dish_str (dish: Dish) -> str:
    '''takes a dish namedtuple and returns a string of that dish's info'''
    return dish.name + " ($"+str(dish.price) + "): " + str(dish.calories) + " cal\n"

def dish_get_info() -> Dish:
    ''' Prompt user for fields of a dish,
        then create a Dish object and return it.
    '''
    n = input("Please enter the dish's name: ")
    p = input("Please enter the price: ")
    c = input("Please enter the amount of calories of the dish: ")
    return Dish(n, float(p), int(c))

def dish_change_price ( dish: Dish, change: int) -> Dish:
    '''takes a dish and returns a dish with the price change percentage according to input'''
    new_dish = Dish( dish.name, dish.price + dish.price * change/100, dish.calories)
    dish = new_dish
    return dish

assert dish_change_price (dish1, 100) == Dish( "Pizza", 5.70, 285)

#MENU

menu1 = [dish1,dish2]

def menu_change_price ( dish_list: "List of Dish", percentage: int) -> "List of Dish":
    '''takes a list of dishes and changes the price of all dishes according to inputed percentage'''
    for dish in range(len(dish_list)):
        dish_list[dish] = dish_change_price(dish_list[dish], percentage)
    return dish_list

assert menu_change_price(menu1, 200) == [Dish(name='Pizza', price=8.55, calories=285),
                                          Dish(name='Burger', price=9.75, calories=354)]

def menu_remove_by_name(dishes: 'list of Dish', to_remove: str) -> 'list of Dish':
    ''' Return the menu with all names matching to_remove removed.
    '''
    result = []
    for d in dishes:
        if d.name != to_remove:
            result.append(d)
    return result
assert menu_remove_by_name (menu1, "Pizza") == [Dish(name='Burger', price=9.75, calories=354)]

def menu_to_str(dishes: 'list of Dish') -> str:
    ''' Return a string representing the whole menu of dishes'''
    result = ""
    for d in dishes:
        result = result + dish_str(d)
    return result

def menu_add(dishes: 'list of Dishes', dish: Dish) -> 'list of Dish':
    ''' Return the menu with the diner added to it
    '''
    dishes.append(dish)
    return dishes

assert menu_add(menu1, dish3) == [Dish(name='Pizza', price=8.55, calories=285),
                                   Dish(name='Burger', price=9.75, calories=354),
                                   Dish(name='Spaghetti', price=8.13, calories=221)]

def menu_format_print (dishes: "list of Dishes") -> None:
    for d in dishes:
        print ( f' Name: {d.name:10s}')
        print ( f' Price: {d.price:2.2f}')
        print ( f' Calories: {d.calories:4f}')

MENU2 = '''
Menu creation program for a diner
 n:  Add a new dish to the menu
 r:  Remove a dish from the menu
 c: Change prices for the dishes served
 e: Remove (erase) all the dishes from the collection
 p:  Print all the dishes
 q:  Quit
'''

def menu_enter(dishes: "List of Dish") -> "List of Dish":
    ''' repeatedly asks user if they want to add a dish'''
    keep_going = True
    keep_going_input = input ("Would you like to create a menu for this diner? \n put y for yes or n for no ")
    if keep_going_input == 'y':
        keep_going = True
    elif keep_going_input == 'n':
        keep_going = False
        
    while keep_going:
        command = input(MENU2)
        if command == 'q':
            keep_going = False       #  we're done
        elif command == 'n':
            r = dish_get_info()
            dishes = menu_add(dishes, r)
        elif command == 'r':
            n = input("Please enter the name of the dish" +
                      " to remove:  ")
            dishes = menu_remove_by_name(dishes, n)
        elif command == 'p':
            print(menu_to_str(dishes))
        elif command == 'e':
            dishes = []
            print("All dishes have been erased")
        elif command == 'c':
            percentage = input("By what percentage would you like to change the prices? ")
            menu_change_price( dishes, int(percentage))
            print ("The prices have been changed")
        else:
            print("The command you typed, '", command, "', ",
                "isn't a valid command.  Please try again.", sep="")
    return dishes         

def menu_avg_price (menu:"List of Dish") -> int:
    price = 0
    for d in menu:
        price += d.price
    return price/len(menu)

## DINER
Diner = namedtuple('Diner', 'name cuisine phone menu')

d1 = Diner('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
d2 = Diner('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])				

d3 = Diner( "Pascal", "French", "940-752-0107", [Dish("escargots", 12.95, 250),
                                                                        Dish("poached salmon", 18.50, 550),
                                                                        Dish("rack of lamb", 24.00, 850),
                                                                        Dish("marjolaine cake", 8.50, 950)])

# It would be more flexible if we just returned a string
# and let the calling program (the model part, here) decide
# what to do with it

def print_format_diner (eatery: Diner) -> None:
    avg_calories = 0
    avg_price = 0
    print( f' Diner: {eatery.name:10s}')
    print (f' Cuisine: {eatery.cuisine:10s}')
    print (f' Phone: {eatery.phone:10s}')
    print (f' Menu: ')
    menu_format_print(eatery.menu)
    menu_len = len(eatery.menu)
    for d in eatery.menu:
        avg_calories += d.calories
        avg_price += d.price
    print (f' \n Average calories: {avg_calories/menu_len:4.1f} \t Average price: ${avg_price/menu_len:2.2f}\n')
           
def diner_get_info() -> Diner:
    ''' Prompt user for fields of a diner,
        then create a Diner object and return it.
    '''
    new_menu = [] 
    n = input("Please enter the diner's name: ")
    c = input("Please enter the kind of food served: ")
    ph = input("Please enter the phone number: ")
    p = menu_enter(new_menu)
    return Diner(n, c, ph, p)

def diner_change_price (diner: Diner, percentage: int) -> Diner:
    '''changes the price of the dishes in a diner'''
    new_diner = Diner ( diner.name, diner.cuisine, diner.phone, menu_change_price (diner.menu, percentage))
    diner = new_diner
    return diner

assert diner_change_price ( d1, 100) == Diner('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 25.00, 500),
                                                    Dish('Larb Gai', 22.00, 450)])

## COLLECTION
# A collection of Diners is a list of Diner objects
# But some day we might choose a different form, a different way
# to represent collections (e.g., a dictionary).  If we give the
# rest of our development team our API (Aplication Programming
# Interface), the names of functions, the types of their arguments,
# and what the function DOES), that should be enough for them.
# They shouldn't have to know the internals of our code.

diners_list = [d1, d2]
def collection_add(diners: 'list of Diner', eatery: Diner) -> \
    'list of Diner':
    ''' Return the collection with the diner added to it
    '''
    diners.append(eatery)
    return diners
assert collection_add(diners_list, d3) == [d1, d2, d3]
            
def collection_search_by_name(diners: 'list of Diner',
                              looking_for: str) -> 'list of Diner':
    ''' Return a collection containing those diners in diner
        that match the parameter looking_for '''
    result = [ ]
    for d in diners:
        if d.name == looking_for:
            result.append(d)
    return result

assert collection_search_by_name (diners_list, "Wendys") == []

def collection_remove_by_name(diners: 'list of Diner', to_remove: str) \
    -> 'list of Diner':
    ''' Return the collection with all names matching to_remove removed.
    '''
    result = []
    for d in diners:
        if d.name != to_remove:
            result.append(d)
    return result

assert collection_remove_by_name(diners_list, "Taillevent") == \
       [Diner(name='Thai Dishes', cuisine='Thai', phone='334-4433',
              menu=[Dish(name='Mee Krob', price=25.0, calories=500),
                    Dish(name='Larb Gai', price=22.0, calories=450)]),
        Diner(name='Pascal', cuisine='French', phone='940-752-0107',
              menu=[Dish(name='escargots', price=12.95, calories=250),
                    Dish(name='poached salmon', price=18.5, calories=550),
                    Dish(name='rack of lamb', price=24.0, calories=850),
                    Dish(name='marjolaine cake', price=8.5, calories=950)])]

def collection_change_prices (diner_list: "List of Diner", percentage: float) -> "List of Diner":
    '''takes a list of diners and changes the price according to the percentage'''
    for d in range(len(diner_list)):
        diner_list[d] = diner_change_price (diner_list[d], percentage)
    return diner_list

def collection_print_format (diners: "list of diner")-> None:
    ''' takes a collection and prints it in format'''
    for d in diners:
        print_format_diner(d)

def collection_search_cuisine (diners: "list of Diners", cuisine: "str") -> None:
    ''' prints a list of diners with the given cuisine'''
    new_list = []
    avg_price = 0
    for d in diners:
        if d.cuisine == cuisine:
            new_list.append(d)
            avg_price += menu_avg_price (d.menu)
    if new_list == []:
        print( "There are no diners that serve", cuisine, "cuisine")
    else:
        collection_print_format(new_list)
        print ( f' average price of all menus: {avg_price/len(new_list):2.2f}')

def collection_search_dish (diners: "list of Diners", dish: "str") -> None:
    '''prints all diners with given searched dish'''
    new_list = []
    for d1 in diners:
        for d2 in d1.menu:
            if dish in d2.name:
                new_list.append(d1)
    if new_list == []:
        print( "There are no diners that have,", dish)
    else:
        collection_print_format(new_list)

## START EVERYTHING UP
diners31()
