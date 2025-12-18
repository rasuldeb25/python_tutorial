import  random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("----------------------------")
print("Python Number Guessing Game")
print("----------------------------")
print(f"Guess a number between {lowest_num} and {highest_num}")

while is_running:
    guess_str = input("Enter your guess: ")
    if guess_str.isdigit():
        guess = int(guess_str)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print(f"Invalid input. Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"It took you {guesses} guesses")
            is_running = False
    else:
        print(f"Invalid input. Select a number between {lowest_num} and {highest_num}")
