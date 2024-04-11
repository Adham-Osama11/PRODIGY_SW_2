import random
rand_num = random.randint(0, 10)

def get_user_guess():
    while True:
        try:
            guessed_num = int(input("Please Enter a number from 0 to 10: "))
            if 0 <= guessed_num <= 10:
                return guessed_num
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

count = 1
guessed_num = get_user_guess()

while guessed_num != rand_num:
    if guessed_num < rand_num:
        print("Guessed number is less than the random number.")
    else:
        print("Guessed number is greater than the random number.")
    guessed_num = get_user_guess()
    count += 1

print(f"The number is correct! Number of guesses: {count}")
