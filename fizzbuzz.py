import sys
try:
    n = int(sys.argv[1])
except (IndexError, ValueError):
    while True:
        try:
            n = int(input("Choose a number to count up to:"))
            break
        except ValueError:
            print("Numbers only please eg 120...")

print("Fizz buzz counting up to", n)
c = 1
while c <= n:
    if c % 3 == 0 and c % 5 == 0:
        print("fizz buzz")
        c += 1
    if c % 3 == 0:
        print("fizz")
        c += 1
    if c % 5 == 0:
        print("buzz")
        c += 1
    else:
        print(c)
        c += 1