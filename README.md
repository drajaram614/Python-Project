# Slot Machine Python Program

## Summary

This Python program simulates a slot machine game where players can deposit money, place bets on multiple lines, and spin the slot machine to win or lose money based on randomly generated outcomes. The game features a customizable number of lines, adjustable bets per line, and various symbols with different payout values. The slot machine results are displayed in a readable format, and winnings are calculated based on the player's bets and the slot machine's outcome.

## What I Learned

During the development of this slot machine game, I gained valuable experience in Python programming, particularly in the following areas:

- **Functions:** Understanding how to define and use functions to encapsulate functionality and make the code modular.
- **Python Syntax:** Using Python syntax effectively to handle user input, manage program flow, and generate random values.
- **Data Structures:** Utilizing dictionaries to manage symbol counts and values, as well as lists to handle columns and rows in the slot machine.
- **Control Flow:** Implementing loops and conditional statements to manage game logic and user interactions.

## Functions

### `check_winnings(columns, lines, bet, values)`

**Purpose:** To check the winnings based on the player's bets and the slot machine's outcome.

**Explanation:**
- Iterates through each line the player bet on.
- Checks if all symbols in a line match.
- Calculates the winnings and records the winning lines.

**Why:** To determine how much the player has won based on the symbols in the lines they bet on.

### `spin_machine(rows, cols, symbols)`

**Purpose:** To generate a random slot machine spin by selecting symbols for each column.

**Explanation:**
- Creates a list of all symbols based on their counts.
- Randomly selects symbols for each column.
- Ensures each column has the correct number of symbols.

**Why:** To simulate the slot machine's spinning action and produce a random result for each column.

### `display_machine(columns)`

**Purpose:** To display the slot machine's columns in a readable format.

**Explanation:**
- Prints the symbols row by row.
- Uses `|` to separate columns for better visual clarity.

**Why:** To provide a clear and engaging display of the slot machine's results to the user.

### `deposit_money()`

**Purpose:** To ask the user to deposit money for playing the game.

**Explanation:**
- Prompts the user for a deposit amount.
- Validates the input to ensure it's a positive integer.

**Why:** To initialize the player's balance before they start playing.

### `choose_lines()`

**Purpose:** To ask the user how many lines they want to bet on.

**Explanation:**
- Prompts the user to choose a number of lines.
- Validates the input to ensure it falls within the allowed range.

**Why:** To allow the player to select the number of lines they wish to bet on.

### `choose_bet()`

**Purpose:** To ask the user how much they want to bet on each line.

**Explanation:**
- Prompts the user to enter a bet amount.
- Validates the input to ensure it falls within the allowed range.

**Why:** To determine how much the player wants to bet per line.

### `play_spin(balance)`

**Purpose:** To execute a single spin of the slot machine and update the player's balance.

**Explanation:**
- Uses the other functions to manage a spin, display results, and calculate winnings.
- Updates the player's balance based on the results of the spin.

**Why:** To handle the core gameplay mechanics and manage the player's balance after each spin.

## Important Python Syntax

- **Functions:** Defined using `def` keyword. Example: `def function_name(parameters):`.
- **Loops:** `for` and `while` loops for iterating over sequences and repeating actions. Example: `for item in sequence:`.
- **Conditional Statements:** `if`, `elif`, and `else` for decision-making. Example: `if condition:`.
- **Dictionaries:** Used for storing symbol counts and values. Example: `symbol_count = {"Cherry": 2, "Bell": 4, ...}`.
- **Lists:** Used for storing columns and rows of symbols. Example: `columns = []`.

## Slot Machine Code Output

![Example Output 1](IMAGE_URL_1)

![Example Output 2](IMAGE_URL_2)
