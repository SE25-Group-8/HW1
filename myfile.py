print("Calculating Factors")
x = int(input("Input Number: "))

arr = []

for i in range(1, x):
    if (x % i) = 0:
        arr.append(i)

print(f"Factors: {arr}")