str=input("please enter the string")
vowels=0
consonant=0

for i in str:
      if(i=='a' or i=='e'or i=='i'or i=='o' or i=='u' or i=='A' or i=='E' or i=='I'or i=='O'or i=='U'):
          vowels=vowels+1
      else:consonant=consonant+1
      print("number of vowels:",vowels)
      print("the number of consonants:",consonant)
         
