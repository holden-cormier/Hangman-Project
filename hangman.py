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

    def __str__(self):
        #RETURNS THE VARIABLES WITHIN THE HANGMANG OBJECT
        pass

    def play(self):
        #COLLECT GAME INFO
        #LETTER COUNT
        print('Welcome to Evil Hangman!')
        final_word = []
        win_or_lose = False
        letter_count = 0
        guess_list = ''
        _print = ''
        words_left = []
        word_family = {}
        _print = ''
        while True:
            letter_count = input('Enter letter count: ')
            if letter_count.isnumeric() and int(letter_count) < 29:
                break
            else:
                print('Enter a valid letter count.')
        #CREATES STARTING WORDLIST
        for word in self.word_list:
            if len(word) == int(letter_count):
                words_left.append(word)
        #NUMBER OF GUESSES
        num_guesses = 0
        while True:
            num_guesses = input('Enter a guess total: ')
            if num_guesses.isnumeric():
                break
            else:
                print('Enter a valid guess number')
        #RETURN WORDS PROMPT
        remaining_words_test = False
        while True:
            y_or_n = input('Would you like to see your remaining words(y or n): ')
            if y_or_n.isalpha() and y_or_n == 'y':
                remaining_words_test = True
                break
            elif y_or_n.isalpha() and y_or_n == 'n':
                break
            else:
                print('Enter y or n')
        #SETS UP FINAL WORD
        print('You have ', num_guesses, ' guesses remaining.')
        for k in range(int(letter_count)):
            final_word.append('_')
            print('_',end='')
        print()
        #GAME LOOP
        while True:
            #GET THE USERS CURRENT GUESS
            current_guess = ''
            while True:
                current_guess = input('Guess a letter: ').lower()
                if current_guess.isalpha() and len(current_guess) == 1:
                    if guess_list.count(current_guess) != 0:
                        print('Enter a new letter')
                    else:
                        guess_list = guess_list + current_guess
                        break
                else:
                    print('Guess a valid letter')
            #CREATE THE WORD FAMILIES
            max = ''
            for word in words_left:
                current_key = ''
                for letter in range(len(word)):
                    if word[letter] == current_guess:
                        current_key += current_guess
                    else:
                        current_key += '_'
                word_family[current_key] = []
            for word in words_left:
                current_key = ''
                for letter in range(len(word)):
                    if word[letter] == current_guess:
                        current_key += current_guess
                    else:
                        current_key += '_'
                word_family[current_key].append(word)
            #ADJUST CURRENT WORD COUNT
            max = current_key
            for k in word_family.keys():
                if len(word_family[max]) < len(word_family[k]):
                    max = k
            words_left = word_family[max]
            word_family = {}
            if current_guess in words_left[0]:
                #MODIFIES FINAL WORD
                for count in range(int(letter_count)):
                    if words_left[0][count] == current_guess:
                        final_word[count] = current_guess
            else:
               num_guesses = int(num_guesses) - 1
               # PRINT UNDERSCORE
            _print = ''
            for k in range(int(letter_count)):
                _print += final_word[k]
            if num_guesses == 0:
                break
            if final_word.__contains__('_') == False and len(words_left) == 1:
                win_or_lose = True
                break
            if remaining_words_test == True:
                print(words_left)
            print('You have ',num_guesses, ' guesses remaining')
            print('you have guessed:', guess_list)
            print(_print)

        #PRINT IF THE PLAYER WINS OR LOSES
        if win_or_lose == False:
            print()
            print('You lose.')
            print('The word was', words_left[0])
        if win_or_lose == True:
            print()
            print('You win!')
            print('The word was ', _print)
            print('You had ', num_guesses, ' guesses remaining!')
















