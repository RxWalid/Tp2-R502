def affiche(n1, n2):
    for i in range(n1, n2 + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if not output:
            output = str(i)
        print(output, end='')

affiche(5, 10)
print()

affiche(10, 16)
print()
