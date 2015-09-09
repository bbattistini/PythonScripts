import sys

def main(args):
 global count
 iters = []
 
 for i in range (int(args[0])):
  inp = raw_input("Input interval for analysis {0} of {1} times in the form eg. 1-34 \n".format(i + 1, args[0]))
  iters.append(inp.split("-"))
 count = 0
 
 for turn in iters:
  for it in range(int(turn[0]), int(turn[1]) + 1):
    calc(it)
    print "Number of iterations for {0} is {1}".format(it, count)
    count = 0
 print "The End!"

def calc(number):
 global count 
  
 count +=  1 

 if number == 1:
  return
 else:
  if number % 2 == 0:
   number = number / 2
  else:
   number = number * 3 + 1

  calc(number)

if __name__ == "__main__":
 main(sys.argv[1:])
