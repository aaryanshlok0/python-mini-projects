# Cho-Han Dice Game

A simple command-line Python game based on the traditional Japanese dice game **Cho-Han**.
The player bets money and guesses whether the total of two dice will be even or odd.

## About the Game

Cho-Han is a dice game where two dice are rolled inside a cup.
Players guess whether the sum of the dice will be:

* **Cho** — Even number
* **Han** — Odd number

If the player guesses correctly, they win the bet. If not, they lose the bet.

## Features

* Starts with a fixed player balance
* Allows the player to place bets
* Validates bet amount
* Rolls two random dice
* Checks whether the result is Cho or Han
* Updates the balance after each round
* Game continues until the player runs out of money

## Tech Used

* Python
* `random` module

## How to Run

1. Make sure Python is installed on your system.

2. Clone this repository:

```bash
git clone https://github.com/your-username/cho-han-dice-game.git
```

3. Go to the project folder:

```bash
cd cho-han-dice-game
```

4. Run the game:

```bash
python main.py
```

## Game Rules

1. The player starts with a balance of 3000.
2. The player enters the amount they want to bet.
3. The player guesses:

   * `C` for Cho
   * `H` for Han
4. Two dice are rolled.
5. If the total is even, the result is Cho.
6. If the total is odd, the result is Han.
7. If the guess is correct, the player wins the bet amount.
8. If the guess is wrong, the player loses the bet amount.
9. The game ends when the balance becomes 0.

## Example Output

```text
Welcome to Cho-Han!
Your current balance is 3000
Enter the amount you want to bet: 500
(C)ho or (H)an to make a guess! C

Rolling dices!!
Value on first dice is 4
Value on second dice is 2
Total value on dice is 6
Result: Cho

You won!
Your current balance is 3500
```

## Project Structure

```text
cho-han-dice-game/
│
├── main.py
└── README.md
```

## What I Learned

Through this project, I practiced:

* Using functions in Python
* Working with loops
* Taking user input
* Validating input
* Using conditional statements
* Using the `random` module
* Creating a basic command-line game

## Future Improvements

Some possible improvements for this project:

* Add replay option after game over
* Add better error handling for non-numeric inputs
* Add a casino-style introduction
* Add betting history
* Add player name input
* Add multiple difficulty levels

## Author

Made by **Aaryan Shlok**
