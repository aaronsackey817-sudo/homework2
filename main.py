import math
def sqr(num):
    return math.pow(num,2)
def sqr_root(num):
    return math.sqrt(num)

while True:
    print("select a operation: ")
    print("1.Square\n2.square root\n3.Exit")

    choice=input("enter choice: ")
    if choice=="1":
        num=int(input("enter number: "))
        result=sqr(num)
        print(f"answer: {result}")
    elif choice=="2":
        num=int(input("enter number: "))
        result=sqr_root(num)
        print(f"answer: {result}")
    elif choice=="3":
        print("goodbye")
        break