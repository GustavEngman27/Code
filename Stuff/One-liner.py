word = str(input('Choose a word:\n'));word_progress = list('_' * len(word));word = list(word); won = False;current_position = 0
def check(current_position):
    for letter in word:word_progress[current_position] = guess if guess == letter else print('Incorrect');print(word_progress);current_position += 1; return word_progress
while won == False: guess = str(input('Guess a letter:\n')); word_progress = check(current_position)