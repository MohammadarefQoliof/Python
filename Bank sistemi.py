balans = 0
kredit = 0
def deposite():
    global balans
    alınacaq_məbləğ = int(input("Artırılacaq məbləği daxil edin: "))
    balans += alınacaq_məbləğ
    print("Balansınz artırıldı")
    return balans
    
def pulÇəkmək():
    global balans
    print("Mövcud balans:", balans, "AZN")
    götürüləcək_məbləğ = int(input("Alacağınız məbləği daxil edin: "))
    
    if balans < götürüləcək_məbləğ:
        print("Balansınızda kifayət qədər vəsait yoxdur")
    else:
        balans -= götürüləcək_məbləğ
        print("Məbləğ çıxarıldı")
    
    return balans
    
def kreditAlmaq():
    global balans
    global kredit
    alınacaq_kredit = int(input("Alacağınız krediti daxil edin: "))
    balans += alınacaq_kredit
    kredit += alınacaq_kredit
    print("Balans artırıldı")
    return balans, kredit

def borcuQaytarmaq():
    global kredit
    global balans
    
    qaytarılacaq_məbləğ = int(input("Qaytaracağınız borcu daxil edin: "))
    
    if kredit == 0:
        print("Borcunuz qalmadı")
        return balans, kredit

    if qaytarılacaq_məbləğ > kredit:
        print("Göstərilən məbləğ borcunuzdan çoxdur.")
        return balans, kredit
    
    if balans < qaytarılacaq_məbləğ:
        print("Balansınızda kifayət qədər vəsait yoxdur.")
        return balans, kredit

    balans -= qaytarılacaq_məbləğ
    kredit -= qaytarılacaq_məbləğ
    
    print("Borcunuz azaldı")
    print(kredit, "AZN borcunuz qaldı")
    
    return balans, kredit
while True:
    print("1. Balans\n2. Depozit\n3. Pul çəkmək\n4. Kredit almaq\n5. Kredit qaytarmaq\n6. Çıxış")
    print()
    choice = input()
    if choice == "1":
        print("Balans:",balans, "AZN")
    elif choice == "2":
        deposite()
    elif choice == "3":
        pulÇəkmək()
    elif choice == "4":
        kreditAlmaq()
    elif choice == "5":
        borcuQaytarmaq()
    elif choice == "6":
        break
    else:
        print("Təkrar daxil edin")