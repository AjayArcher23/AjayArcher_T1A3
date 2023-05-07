import random 


lvlrowcol = 10

# Wordsearch Levels/Words
levels = [
    ["DOG", "TIGER", "LIZARD", "PENGUIN", "ELEPHANT"],
    ["BASKETBALL", "FOOTBALL", "TENNIS", "BASEBALL", "HOCKEY", "GOLF", "BOXING"],
    ["LONDON", "PARIS", "TOKYO", "WASHINGTON", "AMSTERDAM", "CANBERRA", "ROME"],
    ["ROCK", "RAP", "JAZZ", "POP", "CLASSICAL", "COUNTRY", "REGGAE"],
    ["SPOON", "KNIFE", "FORK", "CUP", "PLATE", "BOWL"]
]

# 2D list for letters
puzzle = [['' for _ in range(lvlrowcol)] for _ in range(lvlrowcol)]

# Places words in the puzzle
def place_words(words): 
    for word in words:
        while True:
            x, y = random.randint(0, lvlrowcol - 1), random.randint(0, lvlrowcol - 1)
            direction = random.choice(['horizontal', 'vertical', 'diagonal_down', 'diagonal_up'])
            if direction == 'horizontal':
                if y + len(word) > lvlrowcol:
                    continue
                overlap = False
                for i in range(len(word)):
                    if puzzle[x][y + i] != '':
                        overlap = True
                        break
                if overlap:
                    continue
                for i in range(len(word)):
                    puzzle[x][y + i] = word[i]
                break
            elif direction == 'vertical':
                if x + len(word) > lvlrowcol:
                    continue
                overlap = False
                for i in range(len(word)):
                    if puzzle[x + i][y] != '':
                        overlap = True
                        break
                if overlap:
                    continue
                for i in range(len(word)):
                    puzzle[x + i][y] = word[i]
                break
            elif direction == 'diagonal_down':
                if x + len(word) > lvlrowcol or y + len(word) > lvlrowcol:
                    continue
                overlap = False
                for i in range(len(word)):
                    if puzzle[x + i][y + i] != '':
                        overlap = True
                        break
                if overlap:
                    continue
                for i in range(len(word)):
                    puzzle[x + i][y + i] = word[i]
                break
            elif direction == 'diagonal_up':
                if x - len(word) < 0 or y + len(word) > lvlrowcol:
                    continue
                overlap = False
                for i in range(len(word)):
                    if puzzle[x - i][y + i] != '':
                        overlap = True
                        break
                if overlap:
                    continue
                for i in range(len(word)):
                    puzzle[x - i][y + i] = word[i]
                break

# Fills empty spaces with random letters
def fill_puzzle():
    for i in range(lvlrowcol):
        for j in range(lvlrowcol):
            if puzzle[i][j] == '':
                puzzle[i][j] = chr(random.randint(65, 90))


# Displays the puzzle
def display_puzzle():
    for row in puzzle:
        print(' '.join(row))

# Searches puzzle for the word
def search_word(word, words):
    if word in words:
        # Check horizontal lines
        for row in puzzle:
            if word in ''.join(row):
                return True
        # Check vertical lines
        for i in range(lvlrowcol):
            if word in ''.join([row[i] for row in puzzle]):
                return True 
        # Check diagonal lines
        for i in range(lvlrowcol - len(word) + 1):
            for j in range(lvlrowcol - len(word) + 1):
                if word == ''.join([puzzle[i+k][j+k] for k in range(len(word))] ):
                    return True
                elif word == ''.join([puzzle[i+k][j+len(word)-1-k] for k in range(len(word)-1, -1, -1)]):
                    return True
    return False

# Prompts the user for a word
def get_user_input():
    return input("Enter a word to search for (or type 'QUIT' to exit): ").upper()

# Clears the terminal of text
def clear_output():
        print('\033[2J\033[1;1H', end='')

# Main Game Loop
def play_game():
    global puzzle
    print("Welcome to the word search game!")
    quit_game = False
    level = 1
    while not quit_game and level <= 5:
        print(f"Level {level}")
        puzzle = [['' for _ in range(lvlrowcol)] for _ in range(lvlrowcol)]
        words = levels[level - 1]
        place_words(words)
        fill_puzzle()
        found_words = []
        while len(found_words) < len(levels[level-1]):
            display_puzzle()
            word = get_user_input()
            if word == 'QUIT':
                quit_game = True
                break
            elif word in found_words:
                print("You already found that word!")
            elif search_word(word, words):
                found_words.append(word)
                print(f"Great job! You've found {len(found_words)} out of {len(words)} words.")
            else:
                print("Sorry, that word is not in the puzzle.")
        if not quit_game:
            print(f"Congratulations, you completed level {level}!")
            level += 1 
            clear_output()
    if level > 5:
        print("Congratulations, you have completed all levels!") 
        quit_game = True
play_game()