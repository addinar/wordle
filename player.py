import tkinter.messagebox as messagebox
from game import Game
from word import Word
import format as f

class Player:
    def __init__(self, game: Game, word: Word):
        self.game = game
        self.word = word
        self.current_row = 0
        self.current_column = 0
        self.row_texts = []
        self.word_found = False
        self.words_entered = 0

    def begin_game(self):
        self.current_word = self.word.new_word()
        self.game.root.bind('<Key>', self.update_label)
        self.game.root.bind('<Return>', self.check_word)
        self.game.root.bind('<BackSpace>', self.delete_char)
        self.game.create_board()
        self.game.root.mainloop()

    def update_label(self, event):
        key_value = event.char.upper()
        if self.current_row < self.game.height and self.current_column < self.game.width and key_value.isalpha():
            label = self.game.cell_labels[self.current_row][self.current_column]
            self.row_texts.append(str(key_value))
            label.config(text=key_value)
            self.current_column += 1

    def check_word(self, event):
        if self.current_column == self.game.width and self.word_exists():
            green_letters = 0
            self.words_entered += 1
            for i in range(self.game.width):
                label = self.game.cell_labels[self.current_row][i]
                if self.row_texts[i] == self.current_word[i]:
                    label.config(bg=f.GREEN, fg="white")
                    green_letters += 1
                elif self.row_texts[i] in self.current_word:
                    label.config(bg=f.YELLOW, fg="white")
                else:
                    label.config(bg=f.GREY, fg="white")

            self.current_column = 0
            self.current_row += 1
            self.row_texts = []

            if green_letters == self.game.width and self.current_row <= self.game.height and self.current_column <= self.game.width:
                self.word_found = True

        elif not self.word_exists():
            messagebox.showinfo('Word does not exist', 'Word does not exist; please input another word')
            for i in range(self.game.width):
                label = self.game.cell_labels[self.current_row][i]
                label.config(text=" ")
            self.row_texts = []
            self.current_column = 0

        if self.word_found:
            self.game.root.after(100, self.game_won_message)
        elif self.words_entered >= 6:
            self.game.root.after(100, self.game_lost_message)

    def delete_char(self, event):
        if self.current_column > 0:
            self.current_column -= 1
            label = self.game.cell_labels[self.current_row][self.current_column]
            label.config(text='')
            if self.row_texts:
                self.row_texts.pop()

    def word_exists(self):
        word = ""
        word += "".join(self.row_texts).lower()
        if word in self.word.lines:
            return True
        else:
            return False

    def game_won_message(self):
        messagebox.showinfo('Wordle', 'Congratulations! You guessed the right word!')

    def game_lost_message(self):
        formatted_message = "You lose! The word is: {}".format(self.current_word)
        messagebox.showinfo('Wordle', formatted_message)






