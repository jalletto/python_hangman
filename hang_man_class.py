import string 
import os

class Hangman:
    def __init__(self):
        self.word = self.get_word_to_guess()
        self.guess_state = list('*' * len(self.word))
        self.guesses_remaining = 10
        self.letters_not_guessed = list(string.ascii_lowercase)

    def get_word_to_guess(self):
        word = input("Enter a Word for your opponent to guess:\n").lower()
        os.system('clear')
        return word

    def get_guess_state(self):
        return " ".join(self.guess_state)

    def get_letters_not_guessed(self):
       return " ".join(self.letters_not_guessed)
    
    def letter_is_already_guessed(self, letter):
        return letter not in self.letters_not_guessed
        
    def check_guess(self,guess):
        for i,l in enumerate(self.word):
            if l == guess:
                self.guess_state[i] = guess
        self.mark_letter_as_guessed(guess)
        self.update_number_of_guesses(guess)
    
    def update_number_of_guesses(self, guess):
        if guess not in self.word or not self.letter_is_already_guessed(guess):
            self.guesses_remaining -= 1
        
    def mark_letter_as_guessed(self, letter):
        if letter in self.letters_not_guessed:
            index = self.letters_not_guessed.index(letter)
            self.letters_not_guessed[index] = "#"
        
    def player_wins(self):
        return self.word == "".join(self.guess_state)
    
    def player_out_of_guesses(self): 
        return self.guesses_remaining == 0
    
    def is_game_over(self):
        return self.player_wins() or self.player_out_of_guesses()
    
    def print_game_status(self):
        print('PYTHON HANGMAN')
        print('---------------')
        print("Your guess so far: " + self.get_guess_state().upper())
        print('Number of guesses remaining: ' + str(self.guesses_remaining))
        print("Letters you haven't guessed yet: " + self.get_letters_not_guessed().upper() + '\n')

    def let_user_guess(self):
        user_guess = input("Enter a letter to guess:\n" ).lower()
        if self.letter_is_already_guessed(user_guess):
            os.system('clear')
            print(f"You already guessed {user_guess} !!!\nPick a different letter.\n")
        else:
            self.check_guess(user_guess)
            os.system('clear')

    def display_game_result(self):
        if self.player_wins():
            print(f"You guessed {self.word.upper()} correctly!")
        else:
            print(f"You are out of guesses and have failed to guess the word {self.word.upper()}")
        
    def play(self):
        while self.is_game_over() == False:
            self.print_game_status()
            self.let_user_guess()
        
        self.display_game_result()
        
       
