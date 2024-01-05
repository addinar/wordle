import tkinter as tk
import format as f

class Game:
    def __init__(self, width, height):
        # Create a Tkinter window
        self.root = tk.Tk()
        self.root.title("Wordle")
        self.root.resizable(width=False, height=False)
        self.cell_labels = []
        self.keyboard_labels = []
        self.width = width
        self.height = height

    def create_board(self):
        for i in range(self.height):
            row_labels = []
            for j in range(self.width):
                label = tk.Label(self.root, text='', font=f.FONT, bg="white", fg="black", bd=2, relief="solid",justify=tk.CENTER,width=4, height=2)
                label.grid(row=i, column=j, padx=10, pady=10)
                row_labels.append(label)
            self.cell_labels.append(row_labels)












