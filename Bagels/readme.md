# Bagels - Detective Logic Game 🎯

A Python implementation of the classic **Bagels** number-guessing game. The computer generates a random 3-digit secret number with unique digits, and the player must use logical clues to guess it within a limited number of attempts.

---

## Features

* 🎲 Randomly generates a unique 3-digit secret number
* ✅ Validates user input
* 🔍 Provides intelligent clues:

  * **Fermi** – Correct digit in the correct position
  * **Pico** – Correct digit in the wrong position
  * **Bagels** – No correct digits
* 🔢 Limited number of attempts
* 🧩 Modular code using functions
* 📖 Well-documented with Python docstrings

---

## Technologies Used

* Python 3
* `random` module

---

## Concepts Practiced

* Functions
* Loops (`while`, `for`)
* Conditional statements
* String manipulation
* Lists and Sets
* Input validation
* Random number generation
* Modular programming
* Problem solving and algorithmic thinking

---

## Project Structure

```text
Bagels/
├── bagels.py
└── README.md
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/aaryanshlok0/python-mini-projects.git
```

2. Navigate to the project folder:

```bash
cd python-mini-projects/Bagels
```

3. Run the program:

```bash
python bagels.py
```

---

## Example Gameplay

```text
Welcome to Bagels! A detective logic game

Enter your guess: 123
Pico

Enter your guess: 531
Fermi Pico

Enter your guess: 581
Congratulations!
```

---

## Validation Rules

A valid guess must:

* Contain exactly **3 digits**
* Contain **only numeric characters**
* Have **no repeated digits**

Invalid guesses are rejected and do not count as an attempt.

---

## Future Improvements

* Difficulty levels (3, 4, or 5 digits)
* Play Again option
* High score tracking
* Better user interface
* Difficulty selection
* Unit tests

---

## Learning Outcome

This project helped reinforce core Python programming concepts, including modular design, input validation, loops, conditional logic, string operations, and problem-solving through a complete console-based game.

---

## Author

**Aaryan Shlok**

GitHub: https://github.com/aaryanshlok0
  