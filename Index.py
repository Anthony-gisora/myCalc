Print("welcome to this app. Ready for some calculation...")
def get_values(a=0,b=0,c=0,d=0, oper):
  if oper == "+":
    ans == a + b + c + d
    print(f"{a} + {b} + {c} + {d} = {ans}")
  elif oper == "-":
    ans = a - b - c - d
    print(f"{a} - {b} - {c} - {d} = {ans}")
  elif oper == "*":
    ans = a * b * c * d
    print(f"{a} * {b} * {c} * {d} = {ans}")
  elif oper == "/":
    print("system under constructuin")
  else:
    print("invalid entry")
  
op = input("Choose an operation: 1) +\n 2) -\n 3) *\n 4) / \n")
a = input("Enter a number: ")
b = input("Enter a number: ")
c = input("Enter a number: ")
d = input("Enter a number: ")

get_values(a,b,c,d, op)

