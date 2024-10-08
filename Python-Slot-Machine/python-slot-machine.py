import random  # Import the random module for generating random choices

# Define constants to set up game rules
MAX_LINES = 3  # Maximum number of lines to bet on
MAX_BET = 100  # Maximum amount a player can bet per line
MIN_BET = 1  # Minimum amount a player can bet per line
ROWS = 3  # Number of rows in the slot machine (height)
COLS = 3  # Number of columns in the slot machine (width)

# Define the symbols and how many times they appear on the slot machine
symbol_count = {
    "Cherry": 2,  # 'Cherry' appears 2 times
    "Bell": 4,    # 'Bell' appears 4 times
    "Lemon": 6,   # 'Lemon' appears 6 times
    "Bar": 8      # 'Bar' appears 8 times
}

# Define the value of each symbol when it appears in a winning combination
symbol_value = {
    "Cherry": 5,  # 'Cherry' pays 5x the bet
    "Bell": 4,    # 'Bell' pays 4x the bet
    "Lemon": 3,   # 'Lemon' pays 3x the bet
    "Bar": 2      # 'Bar' pays 2x the bet
}

def check_winnings(columns, lines, bet, values):
    winnings = 0  # Track the player's winnings
    winning_lines = []  # Keep track of which lines won

    # Check each line that the player bet on
    for line in range(lines):
        symbol = columns[0][line]  # Take the symbol in the first column for this line
        # Check if all symbols in this line match the first symbol
        for column in columns:
            if column[line] != symbol:
                break  # Stop checking if a symbol doesn't match
        else:
            # All symbols in this line match, calculate the winnings
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Record the winning line

    return winnings, winning_lines

def spin_machine(rows, cols, symbols):
    """
    Generate a random slot machine spin by selecting symbols for each column.
    """
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def display_machine(columns):
    """
    Display the slot machine's columns row by row.
    """
    print("\n[🎰 Let's see your results! 🎰]")
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
    print("\nFingers crossed! 🍀")

def deposit_money():
    """
    Ask the user to deposit money for playing.
    """
    while True:
        amount = input("💸 How much would you like to deposit for a chance to win big? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"💰 You've deposited ${amount}. Let's start!")
                break
            else:
                print("⛔️ Amount must be greater than zero.")
        else:
            print("⛔️ Please enter a valid number.")

    return amount

def choose_lines():
    """
    Ask the user how many lines they want to bet on (up to MAX_LINES).
    """
    while True:
        lines = input(f"🎯 How many lines would you like to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                print(f"👍 Great choice! Betting on {lines} lines.")
                break
            else:
                print(f"⛔️ Choose a valid number of lines between 1 and {MAX_LINES}.")
        else:
            print("⛔️ Please enter a number.")

    return lines

def choose_bet():
    """
    Ask the user how much they want to bet on each line.
    """
    while True:
        amount = input(f"💵 How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                print(f"🤑 You're betting ${amount} per line. Let's roll!")
                break
            else:
                print(f"⛔️ Your bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("⛔️ Please enter a number.")

    return amount

def play_spin(balance):
    """
    Execute a slot machine spin and update the user's balance based on the result.
    """
    lines = choose_lines()
    while True:
        bet = choose_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"💸 You don't have enough money to bet that much! Your balance is ${balance}.")
        else:
            break

    print(f"🎲 You're betting ${bet} on {lines} lines. Total bet: ${total_bet}.")
    
    # Spin the slot machine
    slots = spin_machine(ROWS, COLS, symbol_count)
    display_machine(slots)
    
    # Calculate winnings
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    if winnings > 0:
        print(f"🎉 You've won ${winnings}! Winning lines: {', '.join(map(str, winning_lines))}.")
    else:
        print("😞 No wins this time, but better luck on your next spin!")

    return winnings - total_bet  # Return net result (winnings - total bet)

def main():
    """
    Main function to run the slot machine game.
    """
    balance = deposit_money()  # Get the initial deposit
    while balance > 0:
        print(f"\n💵 Your current balance: ${balance}")
        choice = input("Press [ENTER] to spin the slot machine or [q] to cash out: ")

        if choice == "q":
            print(f"💸 You're walking away with ${balance}. Thanks for playing!")
            break

        balance += play_spin(balance)

        if balance <= 0:
            print("😢 Oh no! You're out of money. Better luck next time!")
            break

    print(f"🎰 Final balance: ${balance}. See you next time!")

main()
