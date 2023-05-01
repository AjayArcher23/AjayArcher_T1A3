import random 

# Step 1: Themes and words

class Wordsearch: 
    def __init__(self, theme, words): 
        self.theme = theme
        self.words = words 
    def __str__(self): 
        return f"""{self.theme} 
{self.words}"""

# Level 1
wordsearch_easiest = Wordsearch( "Animals: ", ["cat", "dog", "frog", "tiger", "lizard", "penguin", "elephant"])  
print (wordsearch_easiest) 
# Level 2
wordsearch_easy = Wordsearch( "Sports: ", ["basketball", "football", "tennis", "baseball", "hockey", "golf", "boxing"])  
print (wordsearch_easy) 
# Level 3
wordsearch_medium = Wordsearch( "Capital Cities: ", ["london", "paris", "tokyo", "washington", "Amsterdam", "canberra", "rome"])  
print (wordsearch_medium) 
# Level 4
wordsearch_hard = Wordsearch( "Music Genres: ", ["rock", "rap", "jazz", "pop", "classical", "country", "reggae"])  
print (wordsearch_hard) 
# Level 5
wordsearch_hardest = Wordsearch( "Python: ", ["loop", "conditional", "function", "class", "object", "input"])  
print (wordsearch_hardest)
        
# List for letters 

# Place chosen words in puzzle 

# Fill empty spaces with random letters 

# Display the puzzle 

# Prompt user for word 

# Search puzzle for the word 

# Display result of search