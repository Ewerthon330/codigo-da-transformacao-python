from faker import Faker

fake = Faker("pt_BR")

print("Nome gerado:", fake.name())
print("Email gerado:", fake.email())
print("Cidade gerada:", fake.city())
