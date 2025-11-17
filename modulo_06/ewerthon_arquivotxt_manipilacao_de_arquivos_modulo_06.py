text = input("Write any information\n")

with open ("dados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(text + '\n')

print("\nSave information with sucess")

print("\nReading files contents")

with open ("dados.txt", "r", encoding="utf-8") as arquivo:
    content = arquivo.read()
    print(content)