import random 
lvlrowcol = 10 

# Creates 2D list
puzzle = [['' for _ in range(lvlrowcol)] for _ in range(lvlrowcol)]

game_finished = False 

# Themes and words

class Levels: 
    def __init__(self, theme, words): 
        self.theme = theme 
        self. words = words 

    def run(self, words): 
        print(f"The theme {self.theme} contains the words {self.words}") 
        # Places words in the puzzle
        for word in words:
            while True:
                x, y = random.randint(0, lvlrowcol), random.randint(0, lvlrowcol)
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

       
            


# Level 1
wordsearch_easiest = Levels("Animals",["CAT","FROG","TIGER","LIZARD","PENGUIN","ELEPHANT"])   
# Level 2
wordsearch_easy = Levels("Sports", ["BASKETBALL","FOOTBALL","TENNIS","BASEBALL","HOCKEY","GOLF","BOXING"])  
# Level 3
wordsearch_medium = Levels("Capital", ["LONDON","PARIS","TOKYO","WASHINGTON","AMSTERDAM","CANBERRA","ROME"])   
# Level 4
wordsearch_hard = Levels("Music Genres", ["ROCK","RAP","JAZZ","POP","CLASSICAL","COUNTRY","REGGAE"])   
# Level 5
wordsearch_hardest = Levels("Python", ["LOOP","CONDITIONAL","FUNCTION","CLASS","OBJECT","INPUT"])  

wordsearch_easiest.run()
current_lvl = wordsearch_easiest 

