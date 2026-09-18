import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

balance = 1000
stake = 0
continue_question = True
valid_stake_input = False
total = 0

def roll_dice(total):
    total += random.randint(1, 6)
    return total
    

def run_attempt(balance, stake, total):
    has_stopped = False
    total = 0
    total = roll_dice(total)
    while has_stopped == False:
        print(f'Your current dice total is {total}\nDo you stop?\n')
        choice = input(str())
        if choice == 'yes'.lower() or input == 'y'.lower():
            has_stopped = True
            if total == 21:
                print('You got 21!')
                balance += stake
            elif total > 21:
                print("You did't reach 21...")
                balance =- stake
            elif total == 20 or total == 19:
                print(f'You reached {total}')
                balance += stake / 2
            else:
                print('Coward')
                balance -= stake / 2
        else:
            total = roll_dice(total)
            if total >= 21:
                has_stopped = True
                if total == 21:
                    print('You got 21!')
                    balance += stake
                else:
                    print('You when above 21...') 
                    balance -= stake

            else:
                pass

    return balance


while continue_question == True:
    print(f'Your balance is {int(balance)}')
    valid_stake_input = False
    if input('Continue?') == 'yes'.lower():
        while valid_stake_input == False:
            stake = int(input(f'Select amount at stake:\n'))
            if stake > 0 and stake <= balance:
                valid_stake_input = True
                balance = run_attempt(balance, stake, total)
                if balance == 0:
                    print('You went broke...')
                    continue_question = False
                    break
                else:
                    pass
            else:
                print('Invalid input, try again')
    else:
        break

