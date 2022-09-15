txt = input()
txt_r = len(txt)*2
pos = 0
word = 0
for i in range (len(txt)):
  txt_r -= 2
  print(" "*txt_r,end="")
  pos = word
  while pos >= 0:
    print(txt[pos],end=" ")
    pos -= 1
  pos = 1
  while pos <= word:
    print(txt[pos],end=" ")
    pos += 1
  print()
  word += 1