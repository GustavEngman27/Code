from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

def content_show(bag):
    number = 0
    for item in bag:
        number += 1
        print(f'{number}. {item}')

def content_save(bag):
    if len(bag) < 10:
        choice = input('Type a word to save:\n')
        bag.append(choice.lower())
        print(f'Word "{choice}" was saved!')
        return bag
    else:
        print('Bag capacity exceeded, please remove an item first')

def content_search(bag):
    choice = input('Type a word to search for:\n')
    if choice in bag:
        print(f'The item "{choice}" was found!')

def content_remove(bag):
    print('Select the index of the word to remove: (Normal person index, not programing index)\n')
    number = 0
    for item in bag:
        number += 1
        print(f'{number}. {item}')
    choice = input()
    number = 0
    for item in bag:
        if number == int(choice) - 1:
            bag.remove(item)
            print(f'The object "{item}" was removed...')
        number += 1
    return bag
        
def menu():
    lines = "-" * 20
    run = True
    bag = []
    while run == True:
        choice = input(f'{lines}\n1. {Fore.YELLOW}Show bag content{Style.RESET_ALL}\n2. {Fore.GREEN}Save new bag content{Style.RESET_ALL}\n3. {Fore.BLUE}Search bag content{Style.RESET_ALL}\n4. {Fore.RED}Remove content{Style.RESET_ALL}\n5. {Fore.BLACK}Exit{Style.RESET_ALL}\n{lines}\n')
        match choice.lower():
            case '1':
                content_show(bag)
            case '2':
                bag = content_save(bag)
            case '3':
                content_search(bag)
            case '4':
                bag = content_remove(bag)
            case '5':
                run == False
                break
menu()