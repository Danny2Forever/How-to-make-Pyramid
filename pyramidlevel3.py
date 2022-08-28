star = int(input())
tt = 1
time = star -1
for i in range(star):
  print(" "*time,end="")
  for j in range(tt):
    print("*",end="")
  print("")
  tt += 2
  time -= 1

time += 1 
tt -= 2
for k in range(star-1):
  time += 1
  tt -= 2
  print(" "*time,end="")
  for l in range(tt):
    print("*",end="")
  print("")