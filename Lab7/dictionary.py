'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 11/02/22
Lab: lab07
Last modified: 11/03/22
Purpose: Processes on a file that contains the entire US Constitution
'''


def clean_word(word):
    punctuation = ['!', '?', ':', ';', ',', '|', '.', '[', ']','(',')','--']
    word = word.lower()
    for value in punctuation:
        word = word.replace(value, '')
    words = word.split()
    return words

def build_counts(text):
    constitution = {}
    words = clean_word(text)
    for word in words:
        if word in constitution:
            constitution[word] = constitution[word] + 1
        else:
            constitution[word] = 1
    return constitution
    

def unique_words(word_counts):
    list = []
    my_dictionary = build_counts(word_counts)
    for x in my_dictionary.items():
        if x[1] == 1:
            list.append(x[0])
    return list

def main():
    print("Welcome to the word counter!")
    user_input = input("Enter a file name: ")
    with open(user_input, "r") as f:
        word_counts = f.read()
    
        with open("word_data.txt", "w") as f:
            for word in build_counts(word_counts).items():
                f.write(f"{word[0]} : {word[1]}\n")

        with open("unique_words.txt", "w") as f:
            f.write("Here is a list of words that appear exactly one time in the Constitution:\n")
            for x in unique_words(word_counts):
                f.write(x+"\n")
    
    print(f"The file {user_input} has been processed.")
    print("Output stored in word_data.txt and unique_words.txt")
    print("Exiting...")
main()

