h = 5
for i in range(h):
  for j in range(h - i - 1):
    print(" ", end="")
  for k in range(2 * i + 1):
      print("*", end="")
  print()

for i in range(h - 2, - 1, - 1):
  for j in range(h - i - 1):

    print(" ", end="")
  for k in range(2 * i + 1):

    print("*", end="")
  print()  
