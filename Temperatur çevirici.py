while True:
    temperature = float(input("Temperatur daxil edin: "))
    print("Hansına çevrilsin?\n1. Selsiusa\n2. Farenheita\n3. Çıxış")
    
    choice = int(input("Seçiminizi daxil edin: "))
    if choice == 1:
        celsius = (temperature - 32) / 1.8
        print("C°: ", celsius)
    elif choice == 2:
        fahrenheit = (temperature * 1.8) + 32
        print("F°:", fahrenheit)
    elif choice == 3:
        break
    else:
        print("Geçərsiz yazı.")