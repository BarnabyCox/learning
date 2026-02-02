from random import randint

def main() -> None:
    target = randint(0, 100)
    buffer = input("Guess:") or "-1"
    guess = int(buffer)

    while guess != target:
        if guess > target:
            print("Too high...")
        else:
            print("Too low...")

        buffer = input("Guess again:") or -1
        guess = int(buffer)

    print("Correct!")

if __name__ == "__main__":
    main()