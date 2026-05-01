h = 10
for i in range(h):
  for j in range(h):
    if i == 0 or i == h - 1 or j == 0 or j == h -1:
      print("*", end="")    
    else:
      print(" ", end="")
  print()
