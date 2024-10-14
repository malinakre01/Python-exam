# Question 5:
    
def read_integers():
    integers = []
    while True:
        # The strip() method removes spaces at the beginning and at the end of the string:
        userInput = input("Enter an integer: ").strip()
        if userInput == "":
            break
        integers.append(int(userInput))
    return integers

def display_numbers(integers):
    positive_numbers = [num for num in integers if num > 0]
    zeros = [num for num in integers if num == 0]
    negative_numbers = [num for num in integers if num < 0]
    
    all_num = positive_numbers + zeros + negative_numbers
    print("The numbers were:")
    print(" ".join(str(num) for num in all_num))
    
integers = read_integers()
display_numbers(integers)