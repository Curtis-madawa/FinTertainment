![0f03e5cf-498c-4e93-9caa-ec0243a0c539](https://github.com/Curtis-madawa/FinTertainment/assets/123270149/45af7bcd-0293-4b6e-88f1-389277f513df)
# FinTertainment - 


Description:FinTertainment is a technology company that aims to revolutionize the way people engage with their personal finances by providing a unique and entertaining platform. It offers a gamified financial management application that combines educational content, personalized financial advice, and interactive entertainment experiences.

import random

class FinTertainment:

    def __init__(self, balance=100):

        self.balance = balance

    def play_game(self, bet_amount):

        if bet_amount > self.balance:

            print("Insufficient balance.")

            return

        self.balance -= bet_amount

        # Simulating a game result

        win = random.choice([True, False])

        if win:

            self.balance += bet_amount * 2

            print("Congratulations! You won.")

        else:

            print("Oops! You lost.")

    def display_balance(self):

        print(f"Your current balance is ${self.balance}.")

# Usage example

app = FinTertainment()

while True:

    print("Welcome to FinTertainment!")

    print("1. Play Game")

    print("2. Display Balance")

    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':

        bet_amount = int(input("Enter the bet amount: "))

        app.play_game(bet_amount)

    elif choice == '2':

        app.display_balance()

    elif choice == '3':

        print("Thank you for playing. Goodbye!")

        break

    else:

        print("Invalid choice. Please try again.")
