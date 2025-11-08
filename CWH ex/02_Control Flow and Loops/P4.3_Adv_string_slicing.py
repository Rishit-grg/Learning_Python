#write a program to reverse a given number, for eg 123 should become 321 

num = input("Enter a number to reverse:")

print(int(str(num[::-1])))  # Advanced string slicing 