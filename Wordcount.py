def computeGIndex(word, sentences, syllables):
   return 0.39 * (word/sentences) + 11.8 * (syllables/word) - 15.59

def computeFIndex(word, sentences, syllables):
   return 206.835 - 1.015 * (word/sentences) - 84.6 * (syllables/word)

def wordCount(textFile):
   file = openFile(textFile)

   words = file.split()
   count = 0

   for word in words:
      count += 1
   return count


def userInput():
   print("Enter file name: ")
   return input()

def openFile(fileName):
   file =  open(filename, "r")
   text = file.read()
   file.close()
   return text

def countSentence(textFile):
  count = 0
  sentenceMarks = ".", ";", ":", "?", "!"

  for char in textFile:
     if char in sentenceMarks:
        count = count + 1
  return count


def countSyllables(textFile):
   file = openFile(textFile)

   count = 0
   vowel = ['a', 'e', 'i', 'o', 'u']
   previousChar = ""
   words = file.split()

   for word in words:
      if len(word) <= 3:
         count = count + 1
      else:
         for letter in words:
            if letter in vowel and previousChar not in vowel:
               count = count + 1
            previousChar = letter
      if word.endswith('ed' or 'es' or 'e'):
         count = count + 1
      if word.endswith('le'):
         count = count - 1
   
   return count

def outputFile(file, f, g):
   file = open('textFile.txt', 'a')
   file.write("This is the G index " + (str)(g))
   file.write(" this is the F index " + (str)(f))
   file.close()


filename = userInput

file = openFile(filename)

print(countSentence(file))

print(wordCount(file))

print(countSyllables(file))

f = computeFIndex(wordCount(file), countSentence(file), countSyllables(file))
g = computeGIndex(wordCount(file), countSentence(file), countSyllables(file))

outputFile(file, f, g)