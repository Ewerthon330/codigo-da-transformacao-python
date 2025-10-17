print("----------------------")
print("--- Faixa Etaria ---")
print("----------------------")

year = int(input("Digite o ano atual: "))
birth = int(input("Digite seu ano de nascimento: "))

age = year - birth

if age <= 11 :
    print("You are kid")
elif 12 <= age <= 17:
    print("You are teenager")
elif 18 <= age <= 50:
    print("You are Adult")
else:
    print("You are elderly")
