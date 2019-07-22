import random as rm
num=rm.randint(1,6)
count=1
while count<=3:
    usernum=int(input(" Guess the number: "))
    if num==usernum:
        print(f"You guessed right in the {count} attempt.")
        break
    elif usernum<num:
        print("Guessed number is less than actual number")
        count+=1
    else:
        print("Guessed number is more than actual number")
        count+=1
print(f"The number is {num}")
print("THANK YOU.")

