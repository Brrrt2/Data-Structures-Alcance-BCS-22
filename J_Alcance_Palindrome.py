class Node:

    # Initialize a node with the given data.
    def __init__(self, data):
        self.data = data
        self.next = None

class PalindromeChecker:

    # Initialize the PalindromeChecker class with an empty stack and an empty input sentence.
    def __init__(self):
        
        self.top = None
        self.sentence = ""


    # Take user input for a sentence, push each character onto the stack, and display the palindrome result.
    def input(self):
        
        self.sentence = input("Enter a sentence you want to check: ")
        for char in self.sentence:
            self.push(char)
        self.display()

    # Push a new node with the given data onto the stack.
    def push(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    # Create a cleaned version of the input sentence by removing non-alphabetic characters and converting to lowercase.
    def clean_sentence(self, data):
        cleaned = ""
        for char in data:
            if char.isalpha():
                cleaned += char.lower()
        return cleaned

    # Check if the cleaned sentence is a palindrome.
    def palindrome(self, data):
        # Check if the cleaned sentence is a palindrome by comparing it to its reverse.
        cleaned = self.clean_sentence(data)
        return cleaned == cleaned[::-1]

    # Display the original sentence, cleaned sentence for comparison, and the result of the palindrome check.
    def display(self):
        cleaned = self.clean_sentence(self.sentence)
        print(f"Original Sentence: {self.sentence}")
        print(f"Cleaned Sentence (for comparison): {cleaned}")

        if self.palindrome(self.sentence):
            print(f"The sentence '{self.sentence}' is a Palindrome!\n")
        else:
            print(f"Sorry, the sentence '{self.sentence}' is not a Palindrome!\n")

# Create an instance of the PalindromeChecker class and initiate the palindrome checking loop.
if __name__ == "__main__":
    
    checker = PalindromeChecker()
    print("====================== Welcome to Palindrome Checker! ======================")

    while True:
        
        checker.input()
        # Take input, check for palindrome, and display the result.
        
        new_sentence = input("Do you want to check another sentence? Yes | No:\n ").lower()
        print("")
        if new_sentence != "yes":
            print("Closing...")
            break
        # Ask if the user wants to check another sentence.


