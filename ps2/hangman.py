# Problem Set 2, hangman.py
# Name: ahmed Baruwa
# Collaborators:
# Time spent:8hrs

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if len(secret_word) != len(letters_guessed):
        return False
    for i in range(len(secret_word)):
        if (secret_word[i] != letters_guessed[i]):
            return False
    return True       
            

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    lbuffer = list(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:            
            #print("letter =",letters_guessed[i], pos )
            lbuffer[i] = secret_word[i]
            #print(lbuffer)
        else:
            #pos = secret_word.find(letters_guessed[i])
            lbuffer[i] = "_ "
            #print(lbuffer)
            
    sbuffer = ''.join(lbuffer)
    return sbuffer


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    listOfAlpha = list(string.ascii_lowercase)
    stringOfAlpha = string.ascii_lowercase
    #print("Buffer holds :", buffer_of_alpha)
    #buffer_of_alpha = list(buffer_of_alpha)
    letters_guessed = list(letters_guessed)
    for i in range(len(letters_guessed)):
        if letters_guessed[i] in listOfAlpha:
            pos = stringOfAlpha.find(letters_guessed[i])
            #print(pos)           
            #print(buffer_of_alpha)
            listOfAlpha[pos] = ''
    stringOfAlpha = ''.join(listOfAlpha)
    return stringOfAlpha
         
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    guesses = 6
    warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    buffer = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    print("You have 3 warnings left.")

    letters_guessed = ""
    
    """while True:
        if get_available_letters(letters_guessed) == "":
            print("The end")
            break"""
    while guesses > 0 and warnings > 0 :
        print("------------")
        if secret_word == get_guessed_word(secret_word,buffer):
            print ("Congratulations, you won!")
            print ("Your total score for this game is:", guesses * len(set(secret_word)))
            break
        
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(buffer))
        
        
        
        letters_guessed = input("Please guess a letter: ") 
        
        
        if warnings == 0 and letters_guessed in buffer:
            guesses -= 1
            print ("Oops! You've already guessed that letter. You have no warnings left")
            print("so you lose one guess:", get_guessed_word(secret_word,buffer))
            
            
        
        elif letters_guessed in buffer:
            warnings -= 1
            print ("Oops! You've already guessed that letter. You now have",warnings,"warnings left:")
            print (get_guessed_word(secret_word,buffer))
            #break
            
        elif not letters_guessed.isalpha() and warnings > 0:
            buffer.append(letters_guessed)
            warnings -= 1         
                
            print("Oops! That is not a valid letter. You have",warnings,"warnings left:",get_guessed_word(secret_word,buffer))
            #break                          
           

            
        elif letters_guessed not in secret_word:
#            #print("Faullty", get_available_letters(letters_guessed))
#            print(buffer)
#            print(secret_word)
            if letters_guessed in consonants:                
                guesses -= 1
            elif letters_guessed in vowels: 
                guesses -= 2
            buffer.append(letters_guessed)
            print("Oops! That letter is not in my word:",get_guessed_word(secret_word,buffer))
            #break"""

        elif letters_guessed in secret_word:            
            buffer.append(letters_guessed)
#            print(secret_word)
#            print(buffer)
#            
            print("Good guess:", get_guessed_word(secret_word,buffer))
            

            #break
       
        
    #pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''    
    tired = list(my_word)
    other_word = list(other_word)
    for mutant in my_word:       
        if not mutant.isalpha() and not mutant == '_':
            pos = tired.index(mutant)
            del(tired[pos])

    nmutated = list(my_word)

    if not len(tired) == len(other_word):
        #print("len of my-word =", len(striped))
        return False

    mutated = nmutated
    for mutant in my_word:       
        if not mutant.isalpha():
            pos = nmutated.index(mutant)
            del(mutated[pos])

    striped = ''.join(nmutated)

    for strip in striped:

        if strip not in other_word:
            return False
    for i in range(len(tired)):
        if tired[i].isalpha():

            if strip.isalpha() and not tired[i] == other_word[i]:
                return False
    else:
        return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #word_lis = (load_words())
    buffer = []

    for word in wordlist:
        
        if match_with_gaps(my_word, word):
            buffer.append(word )
    if buffer == []:
        print ("No matches found")
    else:
        buffer = ' '.join(buffer)
        print (buffer)
    
    
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    buffer = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long.")
    print("You have 3 warnings left.")

    letters_guessed = ""
    
    """while True:
        if get_available_letters(letters_guessed) == "":
            print("The end")
            break"""
    while True :
        print("------------")
        if guesses == 0:
            print("Sorry, you ran out of guesses. The word was", secret_word + '.')
            break
            
        if secret_word == get_guessed_word(secret_word,buffer):
            print ("Congratulations, you won!")
            print ("Your total score for this game is:", guesses * len(set(secret_word)))
            break
        
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(buffer))
        
        
        
        letters_guessed = input("Please guess a letter: ") 
        
        if warnings == 0 and letters_guessed in buffer:
            guesses -= 1
            print ("Oops! You've already guessed that letter. You have no warnings left")
            print("so you lose one guess:", get_guessed_word(secret_word,buffer))
            #break
        
        elif letters_guessed in buffer:
            warnings -= 1
            print ("Oops! You've already guessed that letter. You now have",warnings,"warnings:")
            print (get_guessed_word(secret_word,buffer))
            #break
        elif letters_guessed == '*':
            show_possible_matches(get_guessed_word(secret_word,buffer))
            
        elif not letters_guessed.isalpha()  and not letters_guessed == '*' and warnings > 0:
            buffer.append(letters_guessed)
            warnings -= 1         
                
            print("Oops! That is not a valid letter. You have",warnings,"warnings left:",get_guessed_word(secret_word,buffer))
            #break                   
        elif letters_guessed not in secret_word and not letters_guessed == '*':
#            #print("Faullty", get_available_letters(letters_guessed))
#            print(buffer)
#            print(secret_word)
            if letters_guessed in consonants:                
                guesses -= 1
            elif letters_guessed in vowels: 
                guesses -= 2
            buffer.append(letters_guessed)
            print("Oops! That letter is not in my word:",get_guessed_word(secret_word,buffer))
            #break"""

        elif letters_guessed in secret_word:            
            buffer.append(letters_guessed)
#            print(secret_word)
#            print(buffer)
            
            print("Good guess:", get_guessed_word(secret_word,buffer))

    
    
    
    
#    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)
    #show_possible_matches("a_ _ l_")

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
