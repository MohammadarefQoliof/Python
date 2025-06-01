import random
import time

#Introducing the rules
print("Qaydalar:\n1. Bu 2 nəfərlik oyundur.\n2. Sözü hazırlayan şəxs 2ci oyunçu üçün müvafiq sözü daxil etməlidir.\n3. 2ci oyunçu daxil olunan sözü tapmağa çalışmalıdır\n4. Bütün hərflər kiçik şiriftlə yazılmalıdır\n5. Sözlər ən azı 4 hərf, ən çoxu 15 hərf ola bilər\n6. Seçilən sözlər Azərbaycan lüğətində olmalıdır; əks halda oyun sonlandırılacaq\n7. Rəqəm daxil etmək qadağandır.\n8. Xal 10dan çox olmamalıdır.")
print()
print()

#inputing gamer names
while True:
    oyuncu1 = input("Oyunçu No 1 adını daxil edin: ")
    print()
    oyuncu2 = input("Oyunçu No 2 adını daxil edin: ")
    print()
    if any(char.isdigit() for char in oyuncu1):
        print("Rəqəm daxil etmək qadağandır\nBir daha yoxlayın")
        print()
    elif any(char.isdigit() for char in oyuncu2):
        print("Rəqəm daxil etmək qadağandır\nBir daha yoxlayın")
        print()
    elif oyuncu1 == oyuncu2:
        print("Oyunçu adları eyni olmamalıdlır!")
        print("Yenidən cəhd edin")
        print()
    else:
        break
        
#inputing the score
while True:
    try:
        bal_sayı = int(input("Xal sayını daxil edin: "))
        break
    except ValueError:
        print()
        print("Sadəcə sayı daxil etmək olar\nYazı daxil etmək qadağandır")
        print()
#variables which will be used during the game
c = 0
oyuncu1_bal = 0
oyuncu2_bal = 0

while True:
    if c == 11:
        c -= 11
    #variables which should be restarted when this while true starts
    a = 10
    b = 10
    #cheking that the score not to be more than 10
    if bal_sayı > 10:
        print()
        print("Xal 10dan çox olmamalıdır!")
        print("Oyun bitdi")
        break
    #cheking that if a player reached to the identified score he/she celebrates
    if oyuncu1_bal == bal_sayı:
        print(f"Təbriklər, {oyuncu1} qazandı")
        print("Oyun bitdi")
        break
    if oyuncu2_bal == bal_sayı:
        print(f"Təbriklər, {oyuncu2} qazandı")
        print("Oyun bitdi")
        break
    #extra variables
    letters = []
    
    #making a loop to make players turn-by-turn of roles
    if c == 0:
        a += 5
        b -= 5
        print()
        print(oyuncu1, "- Sözü hazırlayan")
        print()
        print(oyuncu2, "- Sözü tapan")
        print()
    if c == 1:
        a -= 5
        b += 5
        print()
        print(oyuncu2, "- Sözü hazırlayan")
        print()
        print(oyuncu1, "- Sözü tapan")
        print()
    if c == 2:
        a += 5
        b -= 5
        print()
        print(oyuncu1, "- Sözü hazırlayan")
        print()
        print(oyuncu2, "- Sözü tapan")
        print()
    if c == 3:
        a -= 5
        b += 5
        print()
        print(oyuncu2, "- Sözü hazırlayan")
        print()
        print(oyuncu1, "- Sözü tapan")
        print()
    if c == 4:
        a += 5
        b -= 5
        print()
        print(oyuncu1, "- Sözü hazırlayan")
        print()
        print(oyuncu2, "- Sözü tapan")
        print()
    if c == 5:
        a -= 5
        b += 5
        print()
        print(oyuncu2, "- Sözü hazırlayan")
        print()
        print(oyuncu1, "- Sözü tapan")
        print()
    if c == 6:
        a += 5
        b -= 5
        print()
        print(oyuncu1, "- Sözü hazırlayan")
        print()
        print(oyuncu2, "- Sözü tapan")
        print()
    if c == 7:
        a -= 5
        b += 5
        print()
        print(oyuncu2, "- Sözü hazırlayan")
        print()
        print(oyuncu1, "- Sözü tapan")
        print()
    if c == 8:
        a += 5
        b -= 5
        print()
        print(oyuncu1, "- Sözü hazırlayan")
        print()
        print(oyuncu2, "- Sözü tapan")
        print()
    if c == 9:
        a -= 5
        b += 5
        print()
        print(oyuncu2, "- Sözü hazırlayan")
        print()
        print(oyuncu1, "- Sözü tapan")
        print()
    if c == 10:
        a += 5
        b -= 5
        print()
        print(oyuncu1, "- Sözü hazırlayan")
        print()
        print(oyuncu2, "- Sözü tapan")
        print()
    #a delay for see who is what
    print("Bir az gözləyin")
    print("Yüklənir...")
    time.sleep(10)
    
    print()
    #making a list of underline
    question_marks = ["_", "_", "_","_","_","_","_","_","_","_","_","_","_","_","_"]
    for i in range(20):
        print(".")
    #making a choice of categories
    print("Kateqoriyalar:\n1) Heyvanlar\n2) Bitkilər\n3) Rənglər\n4) Ölkələr\n5) Rayonlar\n6) Kəndlər\n7) Adlar\n8) Meyvələr\n9) Tərəvəzlər\n10) İdman növləri\n11) Nəqliyyat vasitələri\n12) Musiqi alətləri\n13) Dillər\n14) Filmlər\n15) Kitablar\n16) Mebellər\n17) Alətlər\n18) Elektronikalar\n19) Digər")
    while True:
        try:
            print()
            category_choice = int(input("Kateqoriyanı seçin: "))
            print()
            if category_choice > 19:
                print("Uyğun rəqəm daxil edin")
            else:
                break
        except ValueError:
            print()
            print("Yalnız rəqəm daxil edərək kateqoriyanızı seçə bilərsiniz\nYenidən cəhd edin")
    quiz_word = input("Sözü daxil edin: ")
    number_of_quiz_word = len(quiz_word)
    
    attempts = random.randint(3,11)
    
    #starting the game with this loop
        #cheking not to have a number in the quiz word
    if any(char.isdigit() for char in quiz_word):
        print()
        print("Rəqəm daxil etmək qadağandır. Bir daha yoxlayın")
        break
        print()
    if any(char.isupper() for char in quiz_word):
        print()
        print("Böyük hərf daxil etmək qadağandır. Bir daha yoxlayın")
        break
    #cheking if attempt is equal to zero give the score to the winner
    if attempts == 0:
        for i in range(15):
            print(".")
        print()
        print("Haqqınız tükəndi")
        print()
        print(f"Söz: {quiz_word}")
        if a == 15 and b == 5:
            print(f"{oyuncu1} qazandı")
            oyuncu1_bal += 1
        elif a == 5 and b == 15:
            print(f"{oyuncu2} qazandı")
            oyuncu2_bal += 1
        time.sleep(2)
        c += 1
        for i in range(3):
            print(".")
            time.sleep(0.3)
        print(f"{oyuncu1} - {oyuncu1_bal}")
        print(f"{oyuncu2} - {oyuncu2_bal}")
        time.sleep(3)
        for i in range(20):
            print(".")
        break
        #game starts
    for i in range(50):
        print(".")
    while True:
        if category_choice == 1:
            print("Kateqoriya - Heyvanlar")
            break
        elif category_choice == 2:
            print("Kateqoriya - Bitkilər")
            break
        elif category_choice == 3:
            print("Kateqoriya - Rənglər")
            break
        elif category_choice == 4:
            print("Kateqoriya - Ölkələr")
            break
        elif category_choice == 5:
            print("Kateqoriya - Rayonlar")
            break
        elif category_choice == 6:
            print("Kateqoriya - Kəndlər")
            break
        elif category_choice == 7:
            print("Kateqoriya - Adlar")
            break
        elif category_choice == 8:
            print("Kateqoriya - Meyvələr")
            break
        elif category_choice == 9:
            print("Kateqoriya - Tərəvəzlər")
            break
        elif category_choice == 10:
            print("Kateqoriya - İdman növləri")
            break
        elif category_choice == 11:
            print("Kateqoriya - Nəqliyyat vasitələri")
            break
        elif category_choice == 12:
            print("Kateqoriya - Musiqi alətləri")
            break
        elif category_choice == 13:
            print("Kateqoriya - Dillər")
            break
        elif category_choice == 14:
            print("Kateqoriya - Filmlər")
            break
        elif category_choice == 15:
            print("Kateqoriya - Kitablar")
            break
        elif category_choice == 16:
            print("Kateqoriya - Mebellər")
            break
        elif category_choice == 17:
            print("Kateqoriya - Alətlər")
            break
        elif category_choice == 18:
            print("Kateqoriya - Elektronikalar")
            break
        elif category_choice == 19:
             while True:
                your_choice = input("Yeni kateqoriyanı siz daxil edin: ")
                if any(char.isdigit() for char in your_choice):
                    print()
                    print("Rəqəm daxil etmək qadağandır. Bir daha yoxlayın")
                    print()
                else:
                    break
        else:
            print("Geçərsiz yazı. Yenidən yoxlayın")
    if category_choice == 19:
            print(f"Kateqoriya - {your_choice}")
    print()
    print(f"{number_of_quiz_word} ədəd hərf var")
    #cheking the number of quiz word and printing the underlines with the help of list which made before
    while True:
        if number_of_quiz_word == 4:
            print()
            print("Söz:",' '.join(map(str, question_marks[:4])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 5:
            print()
            print("Söz:",' '.join(map(str, question_marks[:5])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 6:
            print()
            print("Söz:",' '.join(map(str, question_marks[:6])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 7:
            print()
            print("Söz:",' '.join(map(str, question_marks[:7])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 8:
            print()
            print("Söz:",' '.join(map(str, question_marks[:8])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 9:
            print()
            print("Söz:",' '.join(map(str, question_marks[:9])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 10:
            print()
            print("Söz:",' '.join(map(str, question_marks[:10])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 11:
            print()
            print("Söz:",' '.join(map(str, question_marks[:11])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 12:
            print()
            print("Söz:",' '.join(map(str, question_marks[:12])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 13:
            print()
            print("Söz:",' '.join(map(str, question_marks[:13])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 14:
            print()
            print("Söz:",' '.join(map(str, question_marks[:14])))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word == 15:
            print()
            print("Söz:",' '.join(map(str, question_marks)))
            print()
            print("Yazılmış hərflər:",' '.join(map(str, letters)))
            print()
        elif number_of_quiz_word < 4:
            print()
            print("Söz 4 hərfdən az olmamalıdır!")
            break
        elif number_of_quiz_word > 15:
            print()
            print("Söz 15 hərfdən çox olmamalıdır!")
            break

        #game started
        print("Sözü tapmaq üçün", attempts, "haqqınız var")
        print()
        print()
        print("Seçim edin:\n1) Hərf təxmini\n2) Söz təxmini\n3) Qazanılmış xallar")
        print()
        #making a choice
        choice = input()
        if choice == "1":
            for i in range(30):
                print(".")
            while True:
                #detecting that the word which has been inputed is correct or not
                if number_of_quiz_word == 4:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 5:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 6:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[5]:
                        print("Təxmin doğrudur")
                        question_marks[5] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 7:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[5]:
                        print("Təxmin doğrudur")
                        question_marks[5] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[6]:
                        print("Təxmin doğrudur")
                        question_marks[6] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 8:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[5]:
                        print("Təxmin doğrudur")
                        question_marks[5] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[6]:
                        print("Təxmin doğrudur")
                        question_marks[6] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[7]:
                        print("Təxmin doğrudur")
                        question_marks[7] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 9:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[5]:
                        print("Təxmin doğrudur")
                        question_marks[5] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[6]:
                        print("Təxmin doğrudur")
                        question_marks[6] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[7]:
                        print("Təxmin doğrudur")
                        question_marks[7] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[8]:
                        print("Təxmin doğrudur")
                        question_marks[8] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 10:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[5]:
                        print("Təxmin doğrudur")
                        question_marks[5] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[6]:
                        print("Təxmin doğrudur")
                        question_marks[6] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[7]:
                        print("Təxmin doğrudur")
                        question_marks[7] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[8]:
                        print("Təxmin doğrudur")
                        question_marks[8] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[9]:
                        print("Təxmin doğrudur")
                        question_marks[9] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 11:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[5]:
                        print("Təxmin doğrudur")
                        question_marks[5] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[6]:
                        print("Təxmin doğrudur")
                        question_marks[6] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[7]:
                        print("Təxmin doğrudur")
                        question_marks[7] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[8]:
                        print("Təxmin doğrudur")
                        question_marks[8] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[9]:
                        print("Təxmin doğrudur")
                        question_marks[9] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[10]:
                        print("Təxmin doğrudur")
                        question_marks[10] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 12:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[5]:
                        print("Təxmin doğrudur")
                        question_marks[5] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[6]:
                        print("Təxmin doğrudur")
                        question_marks[6] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[7]:
                        print("Təxmin doğrudur")
                        question_marks[7] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[8]:
                        print("Təxmin doğrudur")
                        question_marks[8] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[9]:
                        print("Təxmin doğrudur")
                        question_marks[9] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[10]:
                        print("Təxmin doğrudur")
                        question_marks[10] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[11]:
                        print("Təxmin doğrudur")
                        question_marks[11] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 13:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[5]:
                        print("Təxmin doğrudur")
                        question_marks[5] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[6]:
                        print("Təxmin doğrudur")
                        question_marks[6] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[7]:
                        print("Təxmin doğrudur")
                        question_marks[7] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[8]:
                        print("Təxmin doğrudur")
                        question_marks[8] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[9]:
                        print("Təxmin doğrudur")
                        question_marks[9] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[10]:
                        print("Təxmin doğrudur")
                        question_marks[10] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[11]:
                        print("Təxmin doğrudur")
                        question_marks[11] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[12]:
                        print("Təxmin doğrudur")
                        question_marks[12] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 14:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[5]:
                        print("Təxmin doğrudur")
                        question_marks[5] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[6]:
                        print("Təxmin doğrudur")
                        question_marks[6] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[7]:
                        print("Təxmin doğrudur")
                        question_marks[7] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[8]:
                        print("Təxmin doğrudur")
                        question_marks[8] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[9]:
                        print("Təxmin doğrudur")
                        question_marks[9] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[10]:
                        print("Təxmin doğrudur")
                        question_marks[10] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[11]:
                        print("Təxmin doğrudur")
                        question_marks[11] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[12]:
                        print("Təxmin doğrudur")
                        question_marks[12] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[13]:
                        print("Təxmin doğrudur")
                        question_marks[13] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                elif number_of_quiz_word == 15:
                    print("Yazılmış hərflər:",' '.join(map(str, letters)))
                    print()
                    letter_guess = input("Hərf təxmin edin: ")
                    for i in range(20):
                        print(".")
                    if letter_guess in quiz_word[0]:
                        print("Təxmin doğrudur")
                        question_marks[0] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[1]:
                        print("Təxmin doğrudur")
                        question_marks[1] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[2]:
                        print("Təxmin doğrudur")
                        question_marks[2] = letter_guess
                        print()
                    letters.append(letter_guess)
                    if letter_guess in quiz_word[3]:
                        print("Təxmin doğrudur")
                        question_marks[3] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[4]:
                        print("Təxmin doğrudur")
                        question_marks[4] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[5]:
                        print("Təxmin doğrudur")
                        question_marks[5] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[6]:
                        print("Təxmin doğrudur")
                        question_marks[6] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[7]:
                        print("Təxmin doğrudur")
                        question_marks[7] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[8]:
                        print("Təxmin doğrudur")
                        question_marks[8] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[9]:
                        print("Təxmin doğrudur")
                        question_marks[9] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[10]:
                        print("Təxmin doğrudur")
                        question_marks[10] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[11]:
                        print("Təxmin doğrudur")
                        question_marks[11] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[12]:
                        print("Təxmin doğrudur")
                        question_marks[12] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[13]:
                        print("Təxmin doğrudur")
                        question_marks[13] = letter_guess
                        print()
                        letters.append(letter_guess)
                    if letter_guess in quiz_word[14]:
                        print("Təxmin doğrudur")
                        question_marks[14] = letter_guess
                        print()
                        letters.append(letter_guess)
                    elif letter_guess not in quiz_word:
                        print("Hərf təxmini yanlışdır")
                        print()
                        letters.append(letter_guess)
                        attempts -= 1
                break
        elif choice == "2":
            for i in range(40):
                print(".")
            word_guess = input("Sözü daxil edin: ")
            if quiz_word == word_guess:
                for i in range(40):
                    print(".")
                print("Təbriklər, sözü tapdınız")
                print()
                if a == 15 and b == 5:
                    print(f"{oyuncu2} qazandı")
                    oyuncu2_bal += 1
                elif a == 5 and b == 15:
                    print(f"{oyuncu1} qazandı")
                    oyuncu1_bal += 1
                time.sleep(2)
                c += 1
                for i in range(3):
                    print(".")
                    time.sleep(0.3)
                print(f"{oyuncu1} - {oyuncu1_bal}")
                print(f"{oyuncu2} - {oyuncu2_bal}")
                time.sleep(3)
                for i in range(100):
                    print(".")
                break
            else:
                for i in range(40):
                    print(".")
                print("Söz yanlışdır")
                print()
                if a == 5 and b == 15:
                    print(f"{oyuncu2} qazandı")
                    oyuncu2_bal += 1
                elif a == 15 and b == 5:
                    print(f"{oyuncu1} qazandı")
                    oyuncu1_bal += 1
                time.sleep(2)
                c += 1
                for i in range(3):
                    print(".")
                    time.sleep(0.3)
                print(f"{oyuncu1} - {oyuncu1_bal}")
                print(f"{oyuncu2} - {oyuncu2_bal}")
                time.sleep(3)
                for i in range(100):
                    print(".")
                break
        elif choice == "3":
            print()
            print(f"{oyuncu1} - {oyuncu1_bal}")
            print(f"{oyuncu2} - {oyuncu2_bal}")
            print()
            for i in range(5,0,-1):
                print(i)
                time.sleep(1)
            for i in range(100):
                print(".")
        else:
            for i in range(20):
                print(".")
            print("Geçərsiz yazı. Yenidən yoxlayın")
            print()