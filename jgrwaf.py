try:
 file = open("C:/Users/kask/Desktop/Projekter/testingPython/testingSHiz/someText.txt", "r")
 for l in file.readlines():
  word = ""
  s = l.split(" ")
  for p in s:
   word += (p[0])
  print(word)
#your code goes here
finally:
 file.close()