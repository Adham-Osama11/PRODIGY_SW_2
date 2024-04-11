import random
rand_num = random.randint(0,10);

guessed_num = int(input("Please Enter number from 0 to 10: "))
count=1
while guessed_num != rand_num:
    if guessed_num != rand_num:
        if guessed_num-rand_num < 0:
            print("Guessed number is less than random number")
        else:
            print("Guessed number is greater than random number")

    guessed_num = int(input("Please Enter number from 0 to 10: "))
    count+=count
else:
    print("The number is correct, number of guesses:",count)
