import random

player_points = 0
computer_points = 0

for i in range(5):
    my_ans = input("Choose: Rock, Paper, or Scissors (or 'quit' to exit): ")
    my_ans = my_ans.lower()

    if my_ans == "quit":
        print("Final Scores:")
        print(f"You: {player_points} points")
        print(f"Computer: {computer_points} points")
        break

    if my_ans not in ["rock", "paper", "scissors"]:
        print("Please choose a correct answer")
        continue

    comp_ans = random.choice(["rock", "paper", "scissors"])

    print(f"Computer chose: {comp_ans}")

    if my_ans == comp_ans:
        print("You tied")

    elif (my_ans == "paper" and comp_ans == "rock") or \
         (my_ans == "rock" and comp_ans == "scissors") or \
         (my_ans == "scissors" and comp_ans == "paper"):
        print("You Won!")
        player_points += 1

    else:
        print("You lose!")
        computer_points += 1

    print(f"Your points: {player_points}")
    print(f"Computer's points: {computer_points}")
