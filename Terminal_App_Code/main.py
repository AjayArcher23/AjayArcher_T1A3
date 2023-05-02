import random 
rowl = 10 
coll = 10


game_finished = False 
level1_finished = False 
level2_finished = False 
level3_finished = False 
level4_finished = False 
level5_finished = False 

# Step 1: Themes and words

class Wordsearch: 
    def __init__(self, theme, words): 
        self.theme = theme
        self.words = words 
    def theme_word_display(self): 
        return f"""{self.theme} 
{self.words}"""

# Level 1
wordsearch_easiest = Wordsearch( "Animals: ", ["CAT", "FROG", "TIGER", "LIZARD", "PENGUIN", "ELEPHANT"])  
print (wordsearch_easiest) 
# Level 2
wordsearch_easy = Wordsearch( "Sports: ", ["BASKETBALL", "FOOTBALL", "TENNIS", "BASEBALL", "HOCKEY", "GOLF", "BOXING"])  
print (wordsearch_easy) 
# Level 3
wordsearch_medium = Wordsearch( "Capital Cities: ", ["LONDON", "PARIS", "TOKYO", "WASHINGTON", "AMSTERDAM", "CANBERRA", "ROME"])  
print (wordsearch_medium) 
# Level 4
wordsearch_hard = Wordsearch( "Music Genres: ", ["ROCK", "RAP", "JAZZ", "POP", "CLASSICAL", "COUNTRY", "REGGAE"])  
print (wordsearch_hard) 
# Level 5
wordsearch_hardest = Wordsearch( "Python: ", ["LOOP", "CONDITIONAL", "FUNCTION", "CLASS", "OBJECT", "INPUT"])  
print (wordsearch_hardest)
        
# 2D List of letters  
puzzle = [["" for _ in range(10)] for _ in range(10)]   

# Place chosen words in puzzle   
def word_placer(words):
    for word in words: 
        # Selects random position in 2d list
        row, col = random.randint(0, 9), random.randint(0, 9)  
        # Selects the direction the word will go in
        direction = random.choice("hor", "ver") 
        if direction == "hor":  
            # Checks word will fit 
            if col + len(word) > 10: 
                col = 10 - len(word)  
                # Places word in random position (going horizontal)
                for i in range(len(word)):
                    puzzle[row][col+i] = word[i]  
        else: 
            if row + len(word) > 10: 
                row = 10 - len(word) 
                # Places word in random position (going vertical)
                for i in range(len(word)): 
                    puzzle[row+i][col] = word[i]


# Fill empty spaces with random letters 
# def fill_grid(puzzle):  


# Display the puzzle 

# Prompt user for word 

# Search puzzle for the word 

# Display result of search