string = input("Mətn daxil edin: ")
vowels = "eəiöüaıou"

saitSayı = 0

for i in string:
    if i in vowels:
        saitSayı += 1

print()
print(saitSayı, "ədəd sait var")