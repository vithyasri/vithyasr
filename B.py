F=input()

if((F>='a' and F<='z') or (F>='A' and F<='Z')):
  if(F=='a' or F=='A' or F=='e' or F=='E' or F=='i' or F=='I' or F=='o' or F=='O' or F=='u' or F=='U'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
