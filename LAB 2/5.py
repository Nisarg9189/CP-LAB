age = int(input("Enter your age"))

def vote(age):
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")

vote(age)