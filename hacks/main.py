import time
# from ship import ship
# from candle import candle
# from keypad import matrix
# from swap import swapnumbers
# from tree import create_tree, grow_tree
# from lists import lists_tester
# from fibonacci import tester
from week2 import factorial, mathfactors
from week1 import lists, fibonacci
from week0 import keypad, swap, tree, candle, ship, frog
main_menu = [
  
]
sub_menu = [
    ["Swap", swap.swapnumbers],
    ["Matrix", keypad.matrix],
    ["Ship", ship.ship],
    ["Candle", candle.candle],
    ["Christmas Tree", tree.grow_tree],
    ["Froggy", frog.frog],
]

animations_sub_menu = [
    ["Lists", lists.lists_tester] ,
    ["Fibonacci", fibonacci.tester],
]
listandloops_sub_menu = [
    ["Factorial", factorial.tester],
    ["Math Funtion", mathfactors.testinput]
]
# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0", submenu])
    menu_list.append(["Week 1", animations_submenu])
    menu_list.append(["Week 2", listandloops_submenu])

    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def animations_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, animations_sub_menu)

def listandloops_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, listandloops_sub_menu)
  
def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()