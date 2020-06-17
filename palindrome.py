'''
PALINDROME DETECTOR
Ask user for a Word
Tell them if it is a PALINDROME or NOT
'''
def reverse(word):

      str = ""
      for i in word:
            str = i + str
            #print(str)
      return str

while(True):
      word = input("Give me a WORD please\n")
      if reverse(word) == word:
            print ("PALINDROME")
      else:
            print ("NOT A PALINDROME")



