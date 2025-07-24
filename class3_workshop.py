Watch = 20
Gun = 15
Chicken = 10

while True :

    Rung_Pom = 50

    choice_1 = int(input("Fight Monster [1] / Escape [2] : "))

    if choice_1 == 1:
        Round = 0
        choice_2 = int(input("Enter Fight Round : "))
        for i in range(choice_2) :
            Round = Round + 1
            print("/// Round : ",Round)
            print("[1] Watch:20 , [2] Gun:15 , [3] Chicken:10 ")
            Weapon_choice = int(input("Choose Weapon : "))
            
            if Weapon_choice == 1:

                Rung_Pom = Rung_Pom - Watch

                if Rung_Pom == 0 :
                    print("Rung_Pom Died")
                    break
                elif Rung_Pom < 0 :
                    Rung_Pom = 20
                print("Rung_Pom [HP] = ",Rung_Pom)
                
            if Weapon_choice == 2:

                Rung_Pom = Rung_Pom - Gun

                if Rung_Pom == 0 :
                    print("Rung_Pom Died")
                    break
                elif Rung_Pom < 0 :
                    Rung_Pom = 20
                print("Rung_Pom [HP] = ",Rung_Pom)

            if Weapon_choice == 3:

                Rung_Pom = Rung_Pom - Chicken

                if Rung_Pom == 0 :
                    print("Rung_Pom Died")
                    break
                elif Rung_Pom < 0 :
                    Rung_Pom = 20
                print("Rung_Pom [HP] = ",Rung_Pom)

        if Round == choice_2 :
            if Rung_Pom != 0 :
                print("!!! Player Died !!!")

    if choice_1 == 2:
        print("// Escape //")
        break
