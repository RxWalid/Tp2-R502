def affiche(n):
    results = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if not output:
            output = i
        results.append(output)
    return results
n = 100
output_list = affiche(n)
for item in output_list:
    print(item)