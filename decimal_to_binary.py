#Hello thank you for using my program
#By Bluedrummer or https://github.com/bluedrummer?tab=repositories at github.
#This works with Python3.
#What does this propgram do?: This program converts any decimal digit to binary just give it a decimal number.
#WARNING!: Numbers with decimal points will not work.
#Thank you for using.

decimal_number = ""


print("This program will convert a decimal number to binary.")
print()
print("Please enter a decimal number.")
while True:
    decimal_number = input()
    if decimal_number.isdecimal():
        decimal_number = int(decimal_number)
        break 
    else:
        print("Please enter a decimal number.")

def decimal_to_binary(n1):
    binary = ""
    while True:
        n2 = n1//2
        binary_digit = n1 - (n2 * 2)
        n1 = n2
        binary_digit = str(binary_digit)
        binary = binary_digit + binary
        if n1 == 0:
            return binary
            break

binary_string = decimal_to_binary(decimal_number)
print(f"Your decimal number {decimal_number} is {binary_string} in binary.")
print("Thank you for using this program!")
