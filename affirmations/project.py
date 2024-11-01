#!/usr/bin/env python3

import sys
import cowsay
import random


def main():
    amount = 120

    affirmations = [
        "I learn a little bit every day.",
        "I am doing my best.",
        "I know more today than I knew yesterday.",
        "I am ready to learn something new today.",
        "I can ask for help.",
        "I can help others who need me.",
        "I can achieve my goals.",
        "I can do difficult things.",
        "I can learn from my mistakes.",
        "I can use more than one language to communicate.",
        "I play an important role in my community.",
        "I accept all of my emotions.",
        "I am ready for a new challenge.",
        "I am different and unique.",
        "I treat others with kindness and respect.",
        "I am grateful for my friends and family.",
        "I am thankful for my teacher.",
        "I take care of my body and mind.",
        "I focus on things that matter to me.",
        "I feel wonderful.",
    ]

    automatasciiart = " _________________________________________\n|_________________________________________|\n|                                         |\n|          POSITIVE AFFIRMATIONS          |\n|                                         |\n|       .-----------. .-----------.   123 |\n|      |   No. 01   | |   No. 02   |  456 |\n|      |            | |            |  789 |\n|      |  [ 1,2O ]  | |  [ 1,2O ]  |  ### |\n|       '-----------' '-----------'       |\n|                                     ||  |\n|       .-----------. .-----------.       |\n|      |   No. 03   | |   No. 04   |      |\n|      |            | |            |      |\n|      |  [ 1,2O ]  | |  [ 1,2O ]  |      |\n|       '-----------' '-----------'       |\n|                                         |\n|   TAKE FROM HERE!                       |\n|     ___________                         |\n|    |           |                        |\n|____|___________|________________________|\n|_________________________________________|\n"
    print(automatasciiart)

    while True:
        try:
            choice = int(input("Choose an item between 1 and 20 you want to buy: "))

            if choice > 20 or choice < 1:
                raise ValueError

        except ValueError:
            choice = random.randint(1, 20)

        except EOFError:
            print("\n", end="")
            cowsay.cow("You did exit this program on purpose! See you!")
            sys.exit(1)

        choicecalc = choice - 1

        while amount > 0:
            try:
                print(f"Amount due to buy affirmation: {amount} Cents")
                coin = int(input("Please insert one virtual coin: "))

                if coin == 1:
                    amount -= 1

                elif coin == 2:
                    amount -= 2

                elif coin == 5:
                    amount -= 5

                elif coin == 10:
                    amount -= 10

                elif coin == 20:
                    amount -= 20

                elif coin == 50:
                    amount -= 50

                elif coin == 100:
                    amount -= 100

                elif coin == 200:
                    amount -= 200

            except ValueError:
                continue

            except EOFError:
                print("\n", end="")
                cowsay.cow("I'm sorry to hear, that you ran out of money!")
                sys.exit(1)

        if amount == 0:
            print("Thank you very much for your purchase!!!")
            cowsay.cow(f"{affirmations[choicecalc]}")
            sys.exit(1)

        elif amount < 0:
            print(f"We owe you some change for your purchase: {amount} Cents")
            cowsay.cow(f"{affirmations[choicecalc]}")
            sys.exit(1)


if __name__ == "__main__":
    main()
