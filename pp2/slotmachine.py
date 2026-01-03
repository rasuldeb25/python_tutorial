#Python Slot machine
import  random
def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")
def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 6
        elif row[0] == '⭐':
            return bet * 10
    else:
        return 0

def main():
    balance = 100
    print("----------------------------")
    print("Welcome to the slot machine!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("----------------------------")
    while balance > 0:
        print(f"Current balance: ${balance:.2f}")
        while True:
            bet_str = input("Enter your bet: ")
            if bet_str.isdigit():
                bet = float(bet_str)
                break
            else:
                print("Please enter a digit: ")
        if bet > balance:
            print("You don't have enough money!: ")
            continue
        if bet <=0:
            print("Bet must be greater than 0: ")
            continue
        balance -= bet
        row = spin_row()
        print("Spinning ... \n")
        print_row(row)

        payout = get_payout(row,bet)
        if payout > 0:
            print(f"You won ${payout:.2f}!")
        else:
            print("You lost!")
        balance += payout
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again !='Y':
            break
    print("------------------------------")
    print(f"Final balance: ${balance:.2f}")
    print("------------------------------")

if __name__ == "__main__":
    main()