import tkinter as tk  # Import the tkinter library for creating GUI
from tkinter import messagebox  # Import the messagebox module for displaying messages
import random  # Import the random module for generating random moves

class TicTacToe:
    def __init__(self, root):
        self.root = root  # Initialize the root window
        self.root.title("Tic Tac Toe")  # Set the title of the window
        self.player_turn = True  # True for X's turn, False for O's turn (handled by computer)
        self.board = [""] * 9  # Initialize the board with empty strings
        # Create buttons for the Tic Tac Toe grid using a list comprehension
        self.buttons = [tk.Button(self.root, text='', font=('normal', 40), height=1, width=2,
                                  command=lambda idx=i: self.on_button_click(idx)) for i in range(9)]
        self.setup_grid()  # Call the setup_grid method to place buttons on the grid

    def setup_grid(self):
        """Places buttons on the grid to represent the Tic Tac Toe board."""
        for i in range(9):  # Loop through each button index
            row, col = divmod(i, 3)  # Calculate the row and column for each button
            self.buttons[i].grid(row=row, column=col)  # Place the button on the grid

    def on_button_click(self, idx):
        """Handle button clicks for marking X and then let the computer mark O."""
        if self.buttons[idx]['text'] == '' and self.check_winner() is None:  # Check if the button is empty and there is no winner
            self.make_move(idx, 'X')  # Mark X on the button
            self.check_game_over()  # Check if the game is over
            # Computer makes its move if the game is not over and no winner yet
            if "" in self.board and self.check_winner() is None:
                self.root.after(100, self.computer_move)  # Let the computer make a move after a delay

    def make_move(self, idx, player):
        """Marks the board with the player's symbol."""
        self.buttons[idx]['text'] = player  # Set the text of the button to the player's symbol
        self.board[idx] = player  # Update the board with the player's symbol

    def computer_move(self):
        """Implements simple AI for the computer's move."""
        move_made = False  # Flag to track if a move has been made
        # Check for a winning move or block opponent's winning move
        for player in ['O', 'X']:  # Loop through players (O and X)
            for i in range(9):  # Loop through each position on the board
                if self.board[i] == "":  # Check if the position is empty
                    self.board[i] = player  # Try placing player's symbol on the position
                    if self.check_winner() == player:  # Check if the player wins
                        self.make_move(i, 'O')  # If winning move found, mark O on the button
                        move_made = True  # Set move_made flag to True
                        break  # Exit inner loop
                    self.board[i] = ""  # Reset the board position
            if move_made:  # Check if a move has been made
                break  # Exit outer loop

        if not move_made:  # If no immediate win or block
            # Choose a random empty spot
            available_moves = [i for i in range(9) if self.board[i] == ""]  # Get available moves
            if available_moves:  # If there are available moves
                self.make_move(random.choice(available_moves), 'O')  # Choose a random move for O

        self.check_game_over()  # Check if the game is over after the computer's move

    def check_winner(self):
        """Checks board for a winner and returns 'X' or 'O'."""
        wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]  # Define winning combinations
        for a, b, c in wins:  # Loop through each winning combination
            if self.board[a] == self.board[b] == self.board[c] != "":  # Check if any combination has the same symbol and is not empty
                return self.board[a]  # Return the winning symbol
        return None  # Return None if no winner is found

    def check_game_over(self):
        """Check if the game is over and display the result."""
        winner = self.check_winner()  # Check if there's a winner
        if winner:  # If there's a winner
            messagebox.showinfo("Game Over", f"{winner} wins!")  # Show winner message
            self.reset_game()  # Reset the game
        elif "" not in self.board:  # If the board is full
            messagebox.showinfo("Game Over", "It's a tie!")  # Show tie message
            self.reset_game()  # Reset the game

    def reset_game(self):
        """Resets the game by clearing the board and setting the initial player turn."""
        self.board = [""] * 9  # Reset the board
        for button in self.buttons:  # Loop through each button
            button.config(text='')  # Clear the text on the button

def main():
    root = tk.Tk()  # Create the main window
    game = TicTacToe(root)  # Initialize the game
    root.mainloop()  # Start the main event loop

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
