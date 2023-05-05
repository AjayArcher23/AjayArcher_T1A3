import random 
lvlrowcol = 10 
game_finished = False


# Level 1
wordsearch_easiest = ["CAT","TIGER","LIZARD","PENGUIN","ELEPHANT"]  
# Level 2
wordsearch_easy = ["BASKETBALL","FOOTBALL","TENNIS","BASEBALL","HOCKEY","GOLF","BOXING"]
# Level 3
wordsearch_medium = ["LONDON","PARIS","TOKYO","WASHINGTON","AMSTERDAM","CANBERRA","ROME"]  
# Level 4
wordsearch_hard = ["ROCK","RAP","JAZZ","POP","CLASSICAL","COUNTRY","REGGAE"]   
# Level 5
wordsearch_hardest = ["LOOP","CONDITIONAL","FUNCTION","CLASS","OBJECT","INPUT"]

words = wordsearch_easiest

# 2D list for letters
puzzle = [['' for _ in range(lvlrowcol)] for _ in range(lvlrowcol)]

 # Places words in the puzzle
def run():  
        for word in words:
            while True:
                x, y = random.randint(0, lvlrowcol-1), random.randint(0, lvlrowcol-1)
                direction = random.choice(['horizontal', 'vertical', 'diagonal_down', 'diagonal_up'])
                if direction == 'horizontal':
                    if y + len(word) > lvlrowcol:
                        continue
                    overlap = False
                    for i in range(len(word)):
                        if puzzle[x][y+i] != '':
                            overlap = True
                            break
                    if overlap:
                        continue
                    for i in range(len(word)):
                        puzzle[x][y+i] = word[i]
                    break
                elif direction == 'vertical':
                    if x + len(word) > lvlrowcol:
                        continue
                    overlap = False
                    for i in range(len(word)):
                        if puzzle[x+i][y] != '':
                            overlap = True
                            break
                    if overlap:
                        continue
                    for i in range(len(word)):
                        puzzle[x+i][y] = word[i]
                    break
                elif direction == 'diagonal_down':
                    if x + len(word) > lvlrowcol or y + len(word) > lvlrowcol:
                        continue
                    overlap = False
                    for i in range(len(word)):
                        if puzzle[x+i][y+i] != '':
                            overlap = True
                            break
                    if overlap:
                        continue
                    for i in range(len(word)):
                        puzzle[x+i][y+i] = word[i]
                    break
                elif direction == 'diagonal_up':
                    if x - len(word) < 0 or y + len(word) > lvlrowcol:
                        continue
                    overlap = False
                    for i in range(len(word)):
                        if puzzle[x-i][y+i] != '':
                            overlap = True
                            break
                    if overlap:
                        continue
                    for i in range(len(word)):
                        puzzle[x-i][y+i] = word[i]
                    break

        #Fills empty spaces with random letters
        for i in range(lvlrowcol):
            for j in range(lvlrowcol):
                if puzzle[i][j] == '':
                    puzzle[i][j] = chr(random.randint(65, 90))

        # Displays the puzzle
        def display_puzzle():
            for row in puzzle:
                print(' '.join(row))

        display_puzzle()

        # Prompts the user for a word
        def get_user_input():
            return input("Enter a word to search for: ").upper()

        # Searches puzzle for the word
        def search_word(word):
            found = False
            # Horizontal Search
            for i in range(lvlrowcol):
                row = ''.join(puzzle[i])
                if word in row:
                    found = True
                    break
            # Vertical Search
            if not found:
                for j in range(lvlrowcol):
                    col = ''.join([puzzle[i][j] for i in range(10)])
                    if word in col:
                        found = True
                        break
            # Diagonal search from top-left to bottom-right
            if not found:
                for i in range(lvlrowcol):
                    for j in range(lvlrowcol):
                        if puzzle[i][j] == word[0]:
                            for k in range(len(word)):
                                if i+k < lvlrowcol and j+k < lvlrowcol and puzzle[i+k][j+k] == word[k]:
                                    found = True
                                else:
                                    found = False
                                    break
                            if found:
                                break
                    if found:
                        break
            return found

        # Displays the result of search
        found_words = []
        while len(found_words) < len(words):
            word_to_find = get_user_input()
            if word_to_find.upper() in words and word_to_find.upper() not in found_words:
                if search_word(word_to_find.upper()):
                    print("Word found!")
                    found_words.append(word_to_find.upper())
            elif word_to_find.upper() in found_words:
                print("You've already found that word.") 
            else:
                print("Word not found, try again.")
                
            if len(found_words) == len(words):
                print("Congratulations! You found all the words.") 
run()


