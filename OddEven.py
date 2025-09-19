def calculation(num):
    if(num %2 == 0):
        print("The number",num,"is even")
    else:
        print("The number ", num, " is odd")


def main():
    number = int(input("Enter a number: "))
    calculation(number)
main()
   