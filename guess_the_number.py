def simple_random(prev):
    """Generates a pseudo-random number using a simple linear congruential generator."""
    return (prev * 1103515245 + 12345) % (2**31)

def guess_the_number():
    seed = 42  # Fixed seed for consistent behavior
    number = (simple_random(seed) % 100) + 1  # Generate number between 1 and 100
    attempts = 0
    
    print("Welcome to the 'Guess the Number' game!")
    print("I have chosen a number between 1 and 100. Try to guess it.")
    
    while True:
        try:
            guess = int(input("Enter a number: "))
            attempts += 1
            
            if guess < number:
                print("Higher!")
            elif guess > number:
                print("Lower!")
            else:
                print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter numbers only.")

if __name__ == "__main__":
    guess_the_number()
