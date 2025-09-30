def computeGIndex(word, sentences, syllables):
   return 0.39(word/sentences) + 11.8(syllables/word) - 15.59

def computeFIndex(word, sentences, syllables):
   return 206.835 - 1.015 * (word/sentences) - 84.6 * (syllables/word)

def wordCount(textFile):
   file = openFile(textFile)
   text = file.read()
   file.close()

   words = text.split()
   count = 0

   for word in words:
      count += 1
   return count


def userInput():
   print("Enter file name: ")
   return input()

def openFile(fileName):
   file =  open(filename, "r")
   return file

def countSentence(textFile):
  file = openFile(textFile) #Opening the file
  text = file.read() # Have to read the file so you know what's in it
  file.close()
  count = 0
  sentenceMarks = ".", ";", ":", "?", "!"

  for char in text:
     if char in sentenceMarks:
        count = count + 1
  return count


def countSyllables():
   return 

def outputFile():
   return 

filename = userInput()

file = openFile(filename)

print(countSentence(file))

print(wordCount(file))