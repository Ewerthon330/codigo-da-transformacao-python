from datetime import datetime

print('-----------------------------')
print('------ Seja bem Vindo -------')
print('-----------------------------')

rightNow = datetime.now()

name = str(input("Whats your name?" "\nR:"))

print('---------------------------------')

print(f"Welcome {name}, its a pleasure. Now its {rightNow.strftime('%H:%M:%S')} in Brasilia time" )

print('---------------------------------')