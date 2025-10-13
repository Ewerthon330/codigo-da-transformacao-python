print('-----------------------------')
print('------ Seja bem Vindo -------')
print('-----------------------------')


name = str(input("Whats your name?" "\nR:"))

print('---------------------------------')

age =  int(input("How old are you?" "\nR:"))

print('---------------------------------')

print(f"Thats cool {name} you are {age} years old" )

print('---------------------------------')

if age <= 17:
    print("You are a minor")
    print("You cant to participate of our program")
    print("\nSee you next time!")
else:
    print("You are of legal age")
    print("You can to participate of our program")
