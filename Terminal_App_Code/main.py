import random 
lvlrow = 10 
lvlcol = 10


game_finished = False 

# Themes and words

class Levels: 
    def __init__(self, theme, words): 
        self.theme = theme 
        self. words = words 

    def run(self): 
        print(f"The theme {self.theme} contains the words {self.words}")


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

