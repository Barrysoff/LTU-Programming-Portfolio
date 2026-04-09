"""
Practice assignment 4C, Word Frequency Calculator
Author: Mattias Westermark
"""

# Write a program that analyzes how frequently words appear in a given text.


def count_word_frequency(text):
    # The program splits the text into words and counts how many times each word appears.

    word_dict = {}

    # Convert to lower case and remove punctuation.
    text = text.lower()
    new_text = ""

    for char in text:
        if char in ".,!?:;":
            new_text += " "
        else:
            new_text += char

    word_list = new_text.split()

    # Count how many times each word appear
    # The results are stored in a dictionary, where keys are words and values are frequencies.

    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return word_dict


def dict_to_list_of_dicts(word_dict):
    # Convert the dictionary into a list of dictionaries

    word_list_dict = []

    for word, count in word_dict.items():
        new_list = {"word": word, "count": count}
        word_list_dict.append(new_list)

    return word_list_dict


def bubble_sort(word_list_dict):
    # Sort the list based on the count

    result = word_list_dict[:]
    n = len(result)

    # Outer loop
    for i in range(0, n):
        # Inner loop
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if result[j]['count'] < result[j + 1]['count']:
                # Traditional swap
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp

    return result


def main():
    # The user enters a sentence or paragraph.
    text = input("Enter a sentence: ").strip()
    amount = input("How many top words would you like to see? ").strip()

    try:
        amount = int(amount)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    word_dict = count_word_frequency(text)

    word_list_dict = dict_to_list_of_dicts(word_dict)

    sorted_list = bubble_sort(word_list_dict)

    # The program prints the top N most common words, where N is chosen by the user.

    print("Most common words:")
    for i in range(amount):
        if i >= len(sorted_list):
            break

        print(f"{i + 1}. \"{sorted_list[i]['word']}\" - {sorted_list[i]['count']} times")


"""Guard function"""
if __name__ == "__main__":
    main()