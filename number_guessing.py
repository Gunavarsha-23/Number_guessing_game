import random
print("welcome to number guessing game!")
print("I have selected a number between 1 and 100, can you guess it?")
level=input("choose a difficulty level: type 'easy' or 'hard': ")
c_choice=random.randint(1,100)

if level=='easy':
    attempts=10 
        
elif level=='hard': 
    attempts=5
else:
    print("Invalid input, please choose 'easy' or 'hard'.")
    exit()

print(f"You have {attempts} attempts to guess the number.")

while attempts>0:
    ans=int(input("make a guess: "))
        
    if ans==c_choice:
        print(f"Got it! the answer was {c_choice}")
        print(f"you guessed it in {attempts} attempts")
        break

    elif ans>c_choice:
        print("Too high")

    elif ans<c_choice:
        print("Too low")

    attempts-=1
    if attempts>0:
        print(f"You have {attempts} attempts remaining to guess the number.")

    else:
        print("You have run out of attempts, you lose.")
        print(f"The correct answer was {c_choice}")
    