# Birthday Paradox 🎂

A Python simulation of the famous **Birthday Paradox**, demonstrating the surprising probability that two or more people in a group share the same birthday.

The program generates random birthdays, checks for duplicate birthdays, and estimates the probability of a shared birthday using Monte Carlo simulation.

---

## 📌 About the Birthday Paradox

The Birthday Paradox states that in a group of **23 people**, there is approximately a **50.7% chance** that at least two people share the same birthday.

Although this seems counterintuitive, repeated simulations reveal that it is indeed true.

---

## ✨ Features

- 🎲 Randomly generates birthdays
- 📅 Uses Python's `datetime` module for accurate date generation
- 🔍 Detects duplicate birthdays using Python sets
- 📊 Estimates probability using Monte Carlo simulation
- 🧩 Modular code with reusable functions
- 📖 Displays birthdays in a human-readable format

---

## 🛠️ Technologies Used

- Python 3
- `random`
- `datetime`

---

## 📚 Concepts Practiced

- Functions
- Lists
- Sets
- Loops
- Random number generation
- Date and time manipulation
- Monte Carlo Simulation
- Probability
- String formatting (`strftime`)
- Modular programming

---

## 📂 Project Structure

```text
Birthday-Paradox/
├── birthday_paradox.py
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/aaryanshlok0/python-mini-projects.git
```

2. Navigate to the project

```bash
cd python-mini-projects/Birthday-Paradox
```

3. Run the program

```bash
python birthday_paradox.py
```

---

## 💻 Sample Output

```text
Enter no of birthdays to be generated: 23

05 January
18 March
12 July
05 January
...

A duplicate birthday was found.

Enter no of simulations to run: 100000

Estimated probability: 50.73%
```

---

## 🧠 How It Works

1. Generates a random birthday for each person.
2. Stores all birthdays in a list.
3. Uses a Python `set` to detect duplicate birthdays.
4. Repeats the experiment multiple times.
5. Calculates the probability of finding at least one matching birthday.

---

## 📈 Example Result

For **23 people**, the simulation should produce a probability close to:

```text
50.7%
```

As the number of simulations increases, the estimated probability becomes more accurate.

---

## 🔮 Future Improvements

- Input validation
- Display matching birthdays
- Visualize probability using graphs
- Allow custom year ranges
- Interactive menu system
- Unit tests

---

## 👨‍💻 Learning Outcomes

This project helped reinforce:

- Working with Python modules
- Date manipulation using `datetime`
- Detecting duplicates using sets
- Building reusable functions
- Running large-scale simulations
- Understanding probability through programming

---

## 👤 Author

**Aaryan Shlok**

GitHub: https://github.com/aaryanshlok0

---
⭐ This project is part of my **Python Mini Projects** series, where I build small projects to strengthen my Python fundamentals and problem-solving skills.