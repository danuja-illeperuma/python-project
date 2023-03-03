
while True:
    try:
        num1=int(input("enter number 1 :"))
        num2=int(input("enter number 2 : "))
        op=input("enter operation :(* , / , + , - , %,** ) :  ")
        if op == "+":
                  print(num1+num2)
        elif op =="-":
                  print(num1 - num2)
        elif op =="*":
                  print(num1 * num2)
        elif op =="/":
                  print(num1 / num2)
        elif op =="%":
                  print(num1 % num2)
        elif op =="**":
                  print(num1 ** num2)
        else:
                 print("invalid try again!!")

    except ValueError:
                  print("invalid input try again")







