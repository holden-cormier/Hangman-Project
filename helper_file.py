#HOLDEN CORMIER
#EVIL HANGMAN PROJECT
#
#09/23/2021

class Hangman:
    def __init__(self):
        #CREATES A HANGMAN OBJECT
        self.word_list = [] #CONVERTS THE DICTIONARY FILE INTO A LIST OF WORDS
        with open('dictionary.txt', 'r') as file:
            for line in file:
                self.word_list.append(line.rstrip('\n'))
        self.letter_count = '' #HOW MANY LETTERS THE USER WANTS THE WORD TO BE
        self.num_guesses = '' #HOW MANY GUESSES THE USER WANTS AND THE REMAINING GUESSES
        self.debug_help = False #IF THE USER WANTS TO SEE REMAINING WORDS
        self.word_start = [] #WORDS WITH CORRECT LENGTH
        self.win_or_lose = False
        self.current_guess = ''
        self.word_family = {}
        self.guess_list = ''
        self.final_word = ''
    def __str__(self):
        #RETURNS THE VARIABLES WITHIN THE HANGMANG OBJECT
        pass

    def play(self):
        #PLAYS A GAME OF HANGMAN WHERE THE COMPUTER ADJUSTS TO HOW THE PLAYER PLAYS
        #GAME SETUP
        self.get_letter_count()
        self.get_num_guesses()
        self.remaining_words_prompt()
        #GAME LOOP
        while self.num_guesses > 0 or self.win_or_lose is False:
            print('You have ', self.num_guesses, ' guesses left.')
            self.remaining_words_test()
            self.letter_guess()
            self.family_creation()
            print()

    def get_letter_count(self):
        #GETS THE LETTER COUNT FROM THE USER
        while not isinstance(self.letter_count, int):
            try:
                self.letter_count = int(input("Enter the length of your word: "))
            except ValueError:
                print('Word length entered is not valid')

    def get_num_guesses(self):
        #GETS THE NUMBER OF GUESSES FROM THE USER
        while not isinstance(self.num_guesses, int):
            try:
                self.num_guesses = int(input("Enter how many guesses you would like: "))
            except ValueError:
                print('Enter a number')

    def remaining_words_prompt(self):
        # CHANGES DEBUG_HELP IF THE USER WOULD LIKE TO SEE THE REMAINING WORDS WHEN THEY PLAY
        test = False
        value = 'n'
        while test == False:
            try:
                value = str(input('Would you like to see the remaining words left- y/n: '))
                if value == 'y':
                    self.debug_help = True
                    test = True
                    for k in range(
                            len(self.word_list)):  # REMOVES WORDS FROM WORD_LIST THAT ARE NOT THE CORRECT AMOUNT OF LETTERS
                        if self.letter_count == len(self.word_list[k]):
                            self.word_start.append(self.word_list[k])
                elif value == 'n':
                    test = True
                else:
                    print('Enter y or n: ')
            except ValueError:
                break

    def remaining_words_test(self):
        # PRINTS THE REMAINING WORDS IF USER SELECTS Y
        if self.debug_help == True:
            print(self.word_start)

    def letter_guess(self):
        while True:
            self.current_guess = input('Guess a letter: ')
            if self.current_guess.isalpha():
                if len(self.current_guess) == 1:
                    break
                else:
                    print('Enter just one letter')
            else:
                print('Enter a letter')

    def family_creation(self):
        family_length = self.letter_count+1
        for k in range(family_length):
            self.word_family[k] = []
        for value in self.word_start:
            if value.count(self.current_guess) == 1:
                self.word_family[value.find(self.current_guess)].append(value)
            elif value.count(self.current_guess) == 0:
                self.word_family[family_length-1].append(value)
        max = len(self.word_family[0])
        max_location = 0
        for x in range(family_length):
            if max < len(self.word_family[x]):
                max = len(self.word_family[x])
                max_location = x
        if len(self.word_family[max_location]) == 1:
            final_word = self.word_family[max_location]
        else:
            self.word_start = self.word_family[max_location]

    def guess_correct(self):
        pass

