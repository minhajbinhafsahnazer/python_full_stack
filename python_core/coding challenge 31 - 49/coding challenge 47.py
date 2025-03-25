#Write a function in Python to count words in a text file those are ending with alphabet "e".

def count_words_ending_with_e():
    no_of_words = 0  

    with open("story.txt", "r") as file:
        data = file.read()
        words = data.split()  # Splitting into words
        
        for word in words:
            if word.endswith('e'):  # Check if the word ends with 'e'
                no_of_words += 1

    print("Number of words ending with 'e':", no_of_words)

count_words_ending_with_e() 