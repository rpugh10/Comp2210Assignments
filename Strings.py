def mask_emails(text):
    words = text.split()

    masked_words = []

    for word in words:
        if "@" in word and word.endswith(".com"):
            findIndex = word.find("@")
            moveIndex = word[findIndex:]
            masked_word = "***" + moveIndex
            masked_words.append(masked_word)
        else:
            masked_words.append(word)
        
    return ' '.join(masked_words)

def count_palindrome(text):
    words = text.lower().split()
    count = 0

    for word in words:
        if word == (word[::-1]):
            count = count + 1
    return count

def every_nth_character(text, n):
    new_string = []
    new_string.append(text[::n])
    return new_string

def word_frequency(text):
    words = text.split()
    my_dict = {}

    for word in words:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict

def char_frequency(text):
    words = text.split()
    my_dict = {}

    for word in words:
        for letters in word:
            my_dict[letters] = word.count(letters)
    return my_dict

def most_common_word(text):
    words = text.split()
    my_dict = {}

    for word in words:
        word = word.lower()

        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1

    most_common = max(my_dict, key=my_dict.get)

    return most_common, my_dict[most_common] #Separating the two values to be returned with a common will make them a tuple

def index_words(text):
    words = text.split()
    my_dict = {}
    word_checker = 0 

    for index, word in enumerate(words):   
        if word not in my_dict:
            my_dict[word] = [index] #If we have not seen the word before it adds a new entry at index 0
        else:
            my_dict[word].append(index) #If the word in in the dictionary we append the new index(add the new index)

    return my_dict


    




   