str = input("Enter string to count # of vowels:")
vc = 0
for vow in str:
  if vow == "a" or vow == "e" or vow == "i" or vow == "o" or vow == "u":
    vc = vc + 1
    print("Vowel in the given string:",vow)
print("# of vowels in the string are:", vc)
