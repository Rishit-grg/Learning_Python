a = input("Enter the sentence - ")
b = int(len(a))
n = 0
for i in range (0,b):
    if a[i] == "a":
        n+=1
    if a[i] == "e":
        n+=1
    if a[i] == "i":
        n+=1
    if a[i] == "o":
        n+=1
    if a[i] == "u":
        n+=1

print(n)

c = a[::-1]

if a == c:
    print("This is a palindrome")
else:
    print("Not a palindrome")