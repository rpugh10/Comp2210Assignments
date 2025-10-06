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

def word_frequency_file(filename):
    file = open(filename, "r")
    text = file.read()
    file.close()

    words = text.split()
    my_dict = {}

    for word in words:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict

def char_frequency_file(filename):
    file = open(filename, "r")
    text = file.read()
    file.close()

    words = text.split()
    my_dict = {}

    for word in words:
        word = word.lower().strip()
        for letters in word:
            if letters in my_dict:
                my_dict[letters] += 1
            else:
                my_dict[letters] = 1
    return my_dict

def wordIndex(filename):
    file = open(filename, "r")
    text = file.read()
    file.close()

    words = text.split()

    my_dic = {}

    for index, word in enumerate(words):
        if word not in my_dic:
            my_dic[word] = [index]
        else:
            my_dic[word].append(index)
    return my_dic

def double_numbers(input_file, output_file):
    infile = open(input_file, "r")
    outfile = open(output_file, 'w')

    for line in infile:
        line = line.strip()
        if line: #This will only skip lines that are truly empty and have no numbers on that line, if not it will evaluate the line
            num = int(line)
            doubled = num * 2
            outfile.write(str(doubled) + "\n")
    infile.close
    outfile.close

def append_even_numbers(filename):
    input_file = open(filename, "r")
    text = input_file.readlines()
    input_file.close()
    input_file = open(filename, "a")

    for line in text:
        line = line.strip()
        if line:
            number = int(line)
            if number % 2 == 1:
                input_file.write(str(number) + "\n")
    input_file.close()
append_even_numbers("numbers.txt")

def replace_and_write(input, output, old, new):
    input_file = open(input, "r")
    content = input_file.read()
    input_file.close()
    output_file = open(output, "w")

    if old in content:
        new_word = content.replace(old, new)
        output_file.write(new_word)
    output_file.close()
replace_and_write("sample_text.txt", "rewritten.txt", "a", "BIG poo")

            






    




   