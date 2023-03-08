import random
import sys

def printer(input):
  sys.stdout.buffer.write(input.encode())
  sys.stdout.flush()


def guessTheNumber(num):
  for n in range(5):
    sys.stdout.buffer.write(b'Please guess the number\n')
    sys.stdout.flush()
    userInput = sys.stdin.buffer.readline()
    answer = int(userInput.decode())
    if(answer > num):
      printer("Your num is high! ")
    elif(answer < num):
      printer("Your num is low! ")
    elif(num == answer):
      printer("You Win!")
      sys.exit(0)
  return printer("You Lose!")
  
def main():

  printer("Please type min number: ")
  min = sys.stdin.buffer.readline()
    
  printer("Please type max number: ")
  max = sys.stdin.buffer.readline()

  if (type(int(min)) != int or type(int(max)) != int):
    printer("Please type number")
    sys.exit(1)
  
  minNum = int(min.decode())
  maxNum = int(max.decode())

  if (minNum > maxNum):
    printer("minNum should be smaller than maxNum.")
    sys.exit(1)

  randomNumber = random.randint(minNum, maxNum+1)

  guessTheNumber(randomNumber)
  

if __name__ == "__main__":
  main()
