word = str(input('Choose a word:\n'))
word_progress = list("_"*len(word))
word = list(word)
game_end = False
current_position = 0
any_success = False
guess = ''
false_guesses_left = int(8)
win = False

def check(current_position, false_guesses_left, word_progress, word, game_end, win):
    current_position = 0
    any_success = False
    for letter in word:
        if guess == word[current_position] and word_progress[current_position] != letter:
            word_progress[current_position] = letter
            any_success = True
        current_position += 1
    if any_success == False:
        print('Incorrect')
        false_guesses_left = false_guesses_left - 1
        if false_guesses_left <= 0:
            print('You lost')
            game_end = True
            return game_end
        print(f'You have {false_guesses_left} guesses left')
        return false_guesses_left
    else:
        print('Correct')
    current_position = 0
    word_progress = "".join(word_progress)
    word = "".join(word)
    print(word_progress)
    if word_progress == word:
        game_end = True
        win = True
        print('test')
    else:
        pass
    word_progress = word_progress.split(word_progress)
    word = word.split(word)
    return false_guesses_left, game_end, win

while game_end == False:
    guess = str(input(f'Guess a letter\n'))
    if guess == 'exit':
        break
    false_guesses_left, game_end, win = check(current_position, false_guesses_left, word_progress, word, game_end, win)

if win == True:
    print('You won')