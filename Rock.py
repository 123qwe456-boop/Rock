import random
from tkinter import Tk, Label, Button, StringVar


def determine_winner(player, computer):
    """Evaluates the rules of Rock, Paper, Scissors using conditional logic."""
    if player == computer:
        return "It's a tie! 🤝"

    # Define win conditions: winning_move: losing_move
    win_rules = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

    if win_rules[player] == computer:
        return "You Win! 🎉"
    else:
        return "Computer Wins! 🤖"


def play_round(player_choice):
    """Triggers when a player clicks a button.

    Handles computer selection and updates the GUI.
    """
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    # Use basic sequential loops to find items if teaching explicit traversal,
    # or simple matching logic. Here we use an explicit tracking update:
    result = determine_winner(player_choice, computer_choice)

    # Update GUI Labels dynamically
    player_choice_var.set(f"Your Choice: {player_choice}")
    computer_choice_var.set(f"Computer's Choice: {computer_choice}")
    result_var.set(result)


# --- Tkinter GUI Setup ---
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.configure(bg="#F0F4F8")

# StringVar holds dynamic text updates for Tkinter labels
player_choice_var = StringVar(value="Your Choice: None")
computer_choice_var = StringVar(value="Computer's Choice: None")
result_var = StringVar(value="Click a button below to play!")

# UI Labels
title_label = Label(
    root,
    text="Rock, Paper, Scissors!",
    font=("Arial", 18, "bold"),
    bg="#F0F4F8",
    fg="#333333",
)
title_label.pack(pady=15)

player_label = Label(
    root, textvariable=player_choice_var, font=("Arial", 12), bg="#F0F4F8"
)
player_label.pack(pady=5)

computer_label = Label(
    root, textvariable=computer_choice_var, font=("Arial", 12), bg="#F0F4F8"
)
computer_label.pack(pady=5)

result_label = Label(
    root,
    textvariable=result_var,
    font=("Arial", 14, "bold"),
    bg="#F0F4F8",
    fg="#0066CC",
)
result_label.pack(pady=20)

# Instruction Label to satisfy looping demonstration implicitly via events
instructions = Label(
    root, text="Choose your move:", font=("Arial", 10, "italic"), bg="#F0F4F8"
)
instructions.pack()

# Button Frame to group them side-by-side
from tkinter import Frame

button_frame = Frame(root, bg="#F0F4F8")
button_frame.pack(pady=10)

# We can demonstrate a loop by dynamically generating the buttons!
choices = ["Rock", "Paper", "Scissors"]
colors = ["#FF5733", "#33FF57", "#3357FF"]

for i in range(len(choices)):
    choice = choices[i]
    color = colors[i]
    # Using lambda with a default variable to bind the correct string to each button
    btn = Button(
        button_frame,
        text=choice,
        font=("Arial", 12, "bold"),
        width=10,
        bg=color,
        fg="black",
        command=lambda c=choice: play_round(c),
    )
    btn.pack(side="left", padx=5)

# Start the application loop (The ultimate while-loop of a GUI)
root.mainloop()
