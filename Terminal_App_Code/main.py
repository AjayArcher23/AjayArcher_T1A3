import random 

lvlrowcol = 10

# Wordsearch Levels/Words
levels = [
    ["DOG", "TIGER", "LIZARD", "PENGUIN", "ELEPHANT"],
    ["BASKETBALL", "FOOTBALL", "TENNIS", "BASEBALL", "HOCKEY", "GOLF", "BOXING"],
    ["LONDON", "PARIS", "TOKYO", "WASHINGTON", "AMSTERDAM", "CANBERRA", "ROME"],
    ["ROCK", "RAP", "JAZZ", "POP", "CLASSICAL", "COUNTRY", "REGGAE"],
    ["LOOP", "CONDITIONAL", "FUNCTION", "CLASS", "OBJECT", "INPUT"]
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
def search_word(word):
    # Check horizontal lines
    for row in puzzle:
        if all([l in row for l in word]):
            return True
    # Check vertical lines
    for i in range(lvlrowcol):
        if all([l in [row[i] for row in puzzle] for l in word]):
            return True 
    # Check diagonal lines
    for i in range(lvlrowcol - len(word) + 1):
        for j in range(lvlrowcol - len(word) + 1):
            if all([l == puzzle[i+k][j+k] for k, l in enumerate(word)]):
                return True
            elif all([l == puzzle[i+k][j+len(word)-1-k] for k, l in enumerate(reversed(word))]):
                return True

    return False

# Prompts the user for a word
def get_user_input():
    return input("Enter a word to search for (or type 'QUIT' to exit): ").upper()

# Main Game Loop
def play_game():
    global puzzle
    print("Welcome to the word search game!")
    quit_game = False
    for level in range(1, 6):
        print(f"Level {level}")
        puzzle = [['' for _ in range(lvlrowcol)] for _ in range(lvlrowcol)]
        words = levels[level - 1]
        place_words(words)
        fill_puzzle()
        display_puzzle()
        found_words = []
        while len(found_words) < len(words):
            user_input = get_user_input() 
            if user_input.startswith("LEVEL ") and user_input[6:] == str(level + 1):
                break
            elif user_input == "QUIT":
                quit_game = True
                break
            elif search_word(user_input) and user_input not in found_words:
                print("Congratulations! You found a word!")
                found_words.append(user_input)
            else:
                print("Sorry, that's not a valid word in the puzzle.")
        if quit_game:
            break
    if quit_game:
        print("You have quit the game.")
    else:
        print("Congratulations, you have completed all levels!") 
    
play_game()