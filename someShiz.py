aNumber = 50
print('Hello World')
print("Eyo " * aNumber)
x = 2145.235
print(x)
aList = [1,2,3,4,5]
print(aList * 5)
print(aList + [[1,2,3],[7,8,9]])
print(list(range(5,69,5)))
nums = [1,2,3,4,5,7]
nums.append(1)
print(len(nums))
print(nums)
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(51)))

def recursive(x):
    if x == 20:
        print(x)
        return x
    else:
        print(x)
        return x + recursive(x + 1)

recursive(5)

def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
		
print(power(2, 3))

try:
 file = open("C:/Users/kask/Desktop/Projekter/testingPython/testingSHiz/someText.txt")
 for line in file.readlines():
  print(line)
finally:
 file.close()
try:
 file = open("C:/Users/kask/Desktop/Projekter/testingPython/testingSHiz/someText.txt", "a")
 file.write("\nThis is a testbfhbfb")
finally:
 file.close
 print("\n")
try:
 file = open("C:/Users/kask/Desktop/Projekter/testingPython/testingSHiz/someText.txt", "w")
 msg = "sff"
 something = file.write(msg)
 print(something)
finally:
 file.close()
print("\n")
try:
 with open("C:/Users/kask/Desktop/Projekter/testingPython/testingSHiz/someText.txt") as f:
  print(f.read())
finally:
 f.close()