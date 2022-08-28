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