import random
words = ["these", "are", "some", "random", "words", "to", "guess", "in", "this", "hangman", "game"]  #yes these are really random
word = random.choice(words)
display = '_' * len(word)
correct_guesses =0
count = 0

guess = input("It's a %d letter word, Enter you guess: %s \n"%(len(word),display)).strip()

while guess.isdigit()==True:
    guess= input("Please enter an alphabet: ").strip()

while len(guess)!=1:
    guess= input("Invalid Input! Please try again: ").strip()  
 
while correct_guesses!=len(word):  
    if guess in word:
        correct_guesses+=1
        display = display[:word.index(guess)] + guess + display[word.index(guess)+ 1:]  
        word = word[:word.index(guess)]+"_"+word[word.index(guess)+1:]
 
        if correct_guesses<len(word):
            guess= input("correct! guess another letter: %s\n"%display).strip()
        
    else:
        count+=1
        if count ==1:    
            guess= input("wrong guess! 4 attempts left: %s\n"%display).strip()  
        elif count ==2: 
            guess= input("wrong guess! 3 attempts left: %s\n"%display).strip()
        elif count ==3:
            guess= input("wrong guess! 2 attempts left: %s\n"%display).strip()
        elif count ==4:            
            guess= input("wrong guess! 1 attempts left: %s\n"%display).strip()
        elif count ==5:
            print("You're Hanged \n")
            exit()

if correct_guesses==len(word):
    print("Congrats! U Win")