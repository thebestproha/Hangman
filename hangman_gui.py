import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self):
        self.words = ['PYTHON', 'HANGMAN', 'COMPUTER', 'PROGRAMMING', 'CHALLENGE', 'DEVELOPER']
        self.word = random.choice(self.words)
        self.guessed = set()
        self.wrong = 0
        self.max_wrong = 6
        
        self.root = tk.Tk()
        self.root.title("Hangman Game")
        self.root.geometry("450x540")
        self.root.configure(bg='#2c3e50')
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        # Title
        tk.Label(self.root, text="🎯 HANGMAN", font=('Arial', 20, 'bold'), 
                bg='#2c3e50', fg='#ecf0f1').pack(pady=10)
        
        # Hangman drawing
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg='#34495e', highlightthickness=0)
        self.canvas.pack(pady=10)
        
        # Word display
        self.word_label = tk.Label(self.root, font=('Courier', 24, 'bold'), 
                                  bg='#2c3e50', fg='#3498db')
        self.word_label.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#2c3e50')
        input_frame.pack(pady=10)
        
        self.entry = tk.Entry(input_frame, font=('Arial', 14), width=5, justify='center')
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind('<Return>', lambda e: self.guess())
        
        tk.Button(input_frame, text="Guess", command=self.guess, 
                 bg='#27ae60', fg='white', font=('Arial', 12, 'bold')).pack(side=tk.LEFT, padx=5)
        
        # Wrong guesses
        self.wrong_label = tk.Label(self.root, font=('Arial', 12), 
                                   bg='#2c3e50', fg='#e74c3c')
        self.wrong_label.pack(pady=5)
        
        # New game button
        tk.Button(self.root, text="New Game", command=self.new_game,
                 bg='#8e44ad', fg='white', font=('Arial', 12, 'bold')).pack(pady=10)
    
    def draw_hangman(self):
        self.canvas.delete("all")
        # Gallows
        self.canvas.create_line(50, 180, 150, 180, width=3, fill='#95a5a6')  # base
        self.canvas.create_line(80, 180, 80, 20, width=3, fill='#95a5a6')   # pole
        self.canvas.create_line(80, 20, 130, 20, width=3, fill='#95a5a6')   # top
        self.canvas.create_line(130, 20, 130, 40, width=3, fill='#95a5a6')  # noose
        
        if self.wrong >= 1:  # head
            self.canvas.create_oval(120, 40, 140, 60, outline='#e74c3c', width=2)
        if self.wrong >= 2:  # body
            self.canvas.create_line(130, 60, 130, 120, width=3, fill='#e74c3c')
        if self.wrong >= 3:  # left arm
            self.canvas.create_line(130, 80, 110, 100, width=2, fill='#e74c3c')
        if self.wrong >= 4:  # right arm
            self.canvas.create_line(130, 80, 150, 100, width=2, fill='#e74c3c')
        if self.wrong >= 5:  # left leg
            self.canvas.create_line(130, 120, 110, 150, width=3, fill='#e74c3c')
        if self.wrong >= 6:  # right leg
            self.canvas.create_line(130, 120, 150, 150, width=3, fill='#e74c3c')
    
    def get_display_word(self):
        return ' '.join([letter if letter in self.guessed else '_' for letter in self.word])
    
    def update_display(self):
        self.word_label.config(text=self.get_display_word())
        wrong_letters = [g for g in self.guessed if g not in self.word]
        self.wrong_label.config(text=f"Wrong: {', '.join(wrong_letters)} ({self.wrong}/{self.max_wrong})")
        self.draw_hangman()
    
    def guess(self):
        letter = self.entry.get().upper().strip()
        self.entry.delete(0, tk.END)
        
        if not letter or len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Invalid", "Please enter a single letter!")
            return
        
        if letter in self.guessed:
            messagebox.showinfo("Already Guessed", f"You already guessed '{letter}'!")
            return
        
        self.guessed.add(letter)
        
        if letter not in self.word:
            self.wrong += 1
        
        self.update_display()
        
        # Check win/lose
        if set(self.word) <= self.guessed:
            messagebox.showinfo("You Won! 🎉", f"Congratulations! The word was '{self.word}'")
        elif self.wrong >= self.max_wrong:
            messagebox.showinfo("Game Over 💀", f"You lost! The word was '{self.word}'")
    
    def new_game(self):
        self.word = random.choice(self.words)
        self.guessed = set()
        self.wrong = 0
        self.update_display()
        self.entry.focus()
    
    def run(self):
        self.entry.focus()
        self.root.mainloop()

if __name__ == "__main__":
    game = HangmanGame()
    game.run()
