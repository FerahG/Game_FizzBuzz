row=0
for n in range(1,100):
  row=row+1
  if row%15==0:
    print("FizzBuzz")
  elif row%3==0:
    print("Fizz")
  elif row%5==0:
    print("Buzz")
  else:
    print(row)