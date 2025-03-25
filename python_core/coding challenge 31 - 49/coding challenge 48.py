#Write a function in Python to count and display the total number of words in a text file.
def count_words_in_file(filename="story.txt"):
    try:
        with open(filename, "r") as file:
            text = file.read()
            
        # Split the text into words based on whitespace
        words = text.split()
        
        print(f"Total number of words: {len(words)}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Call the function
count_words_in_file()
