# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:48:38 2018

@author: BARUWA1
"""

import string
def is_word_guessed(secret_word, letters_guessed):
    if len(secret_word) != len(letters_guessed):
        return False
    for i in range(len(secret_word)):
        if (secret_word[i] != letters_guessed[i]):
            return False
    return True     

def get_guessed_word(secret_word,letters_guessed):
    lbuffer = list(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            #pos = secret_word.find(letters_guessed[i])
            #print("letter =",letters_guessed[i], pos )
            lbuffer[i] = secret_word[i]
            #print(lbuffer)
        else:
            #pos = secret_word.find(letters_guessed[i])
            lbuffer[i] = "_ "
            #print(lbuffer)
            
    sbuffer = ''.join(lbuffer)
    print(sbuffer)
    

def get_available_letters(letters_guessed):
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
    print("I am thinking of a word that is", len(choose_word(wordlist)),"letters long.")
    print("You have 3 warnings left.")

    letters_guessed = ""
    
    """while True:
        if get_available_letters(letters_guessed) == "":
            print("The end")
            break"""
    while guesses > 0:
        print("------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        
        
        letters_guessed = input("Please guess a letter: ") 
        
        if warnings == 0:
            guesses -= 1
        elif letters_guessed in buffer:
            warnings -= 1
            print ("Oops! You've already guessed that letter. You now have",warnings,":")
            print (get_available_letters(letters_guessed))
            #break
            
        elif not letters_guessed.isalpha() and warnings > 0:
            buffer.append(letters_guessed)
            warnings -= 1         
                
            print("Oops! That is not a valid letter. You have",warnings,"warnings left:",get_guessed_word(secret_word,buffer))
            #break                          
           
        elif letters_guessed in get_available_letters(letters_guessed):            
            buffer.append(letters_guessed)
            print("Good guess:", get_available_letters(letters_guessed))
            
        elif not letters_guessed in get_available_letters(letters_guessed):
            print("Faullty")
            if letters_guessed in consonants:                
                warnings -= 1
            elif letters_guessed in vowels: 
                warnings -= 2
            buffer.append(letters_guessed)
            print("Oops! That letter is not in my word:",get_guessed_word(secret_word,buffer))
        
def match_with_gaps(my_word, other_word):
    tired = list(my_word)
    other_word = list(other_word)
    for mutant in my_word:       
        if not mutant.isalpha() and not mutant == '_':
            pos = tired.index(mutant)
            del(tired[pos])

    nmutated = list(my_word)
    print("nmutated-",nmutated)
    print("tired=", tired)
    if not len(tired) == len(other_word):
        #print("len of my-word =", len(striped))
        return False
    print("nmutated-",nmutated)
    print(len(tired) ,len(other_word))
    mutated = nmutated
    for mutant in my_word:       
        if not mutant.isalpha():
            pos = nmutated.index(mutant)
            del(mutated[pos])

    striped = ''.join(nmutated)
    print("mutated=",mutated)
    print("nmutated=",nmutated)
    print("striped-", striped)

    print("equal")
    for strip in striped:
        print(strip)
        if strip not in other_word:
            return False
    for i in range(len(tired)):
        if tired[i].isalpha():

            if strip.isalpha() and not tired[i] == other_word[i]:
                return False
    else:
        return True
    
    
if __name__ == "__main__":
    #get_guessed_word("antelope", "davpsd")
    #print(is_word_guessed("antelope","davpsd"))
    #print(get_guessed_word("helicopter",[]))
    #print(get_available_letters('l'))
    print(match_with_gaps("t_ _ t", "tabs"))
    