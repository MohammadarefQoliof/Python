while True:
    first_number = int(input("I sayı daxil edin: "))
    second_number = int(input("II sayı daxil edin: "))
    
    print()
    print("select one of them:")
    print("1) +")
    print("2) -")
    print("3) *")
    print("4) /")
    print()

    sign_selection = input()


    if sign_selection == "1":
        print()
        print(first_number + second_number)
    elif sign_selection == "2":
        print()
        print(first_number - second_number)
    elif sign_selection == "3":
        print()
        print(first_number * second_number)
    elif sign_selection == "4":
        print()
        print(first_number / second_number)
    elif sign_selection == "exit":
        break
    else:
        print("Geçərsiz yazı. Yenidən yoxlayın")