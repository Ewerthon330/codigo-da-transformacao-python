print("---------------")
print("Major or Minor")
print("---------------")

n1 = int(input("Insert a number: "))
n2 = int(input("Insert other number: "))

print("---------------------")

if n1 > n2:
    print(f"The number {n1} is major than the number {n2}")
elif n2 > n1:
    print(f"The number {n1} is minor than the number {n2}")
else:
    print(f"The numbers are the same")