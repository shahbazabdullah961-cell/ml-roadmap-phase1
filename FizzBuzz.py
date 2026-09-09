number = 1
n=int(input("Write any number::"))
fizz=0
buzz=0
fizzBuzz=0
while number <= n:
  if(number%3==0 and number%5==0):
    print("FizzBuzz")
    fizzBuzz+=1
  elif(number%3==0):
    print("Fizz")
    fizz+=1
  elif(number%5==0):
    print("Buzz")
    buzz+=1
  else:
    print(number)
  number+=1
print(f"The amount in range 1-{n}")
print(f"Amount of Fizz is    :{fizz}")
print(f"Amount of Buzz is    :{buzz}")
print(f"Amount of FizzBuzz is:{fizzBuzz}")

  
