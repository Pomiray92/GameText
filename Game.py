while True:


    answer = input("What you like to play  (yes/no)  ")

    if answer.lower().strip() == "yes":

        answer = input("You reach a crossroad in the Forest, would you like to left?, rigth?, or forward? you kan not go back because you dont wont it. Just believe me: ").lower().strip()
        if answer == "left":
            answer = input("you encounter a MONSTER, would you like to ('run' or 'attack?')")
        
            if answer == "attack":
                print("That was not the greater idea, you lost!")
                break
            else:
                print("Good choice, you made it away safely.")

                answer = input("You see a car and a plane. Which would you like to take? (car/plane) ")

                if answer == "plane":
                    print("Unfortunately you do not know how to fly... Game is over!")
                    break
                else:
                    print("You won")
                    break
				


        elif answer == "rigth": 
            answer = input("Now you are on a small Path in the forest. On the end of it you see a House would you like to take a closer look at it ('yes' or 'no')")

            if answer == "yes":
                answer = input("You see an old House that have not dor and windows would you go in it? ('in') or go around ('left' or 'rigth')")

            if answer == "in":
                answer = input("You are in tha House and see an Alien. What wold yud doing next? would yu ('attack' or 'run')")
                
                if answer == "attack":
                    print("whatever you do you will die. sorry i have no idea anymore.")
                    break
            
            if answer == "left":
                answer = input("you find nothing and kom back to the dor")
                input = ("You see an old House that have not dor and windows would you go in it? ('in') or go around ('left' or 'rigth') and I kan say you when you go to the Rigth you would become the same result. go 'in' Brother")
                print(answer, "whatever you do you will die. sorry i have no idea anymore.")
               
                break
            elif answer == "rigth":
                answer = input("you find nothing and kom back to the dor")
                input = ("You see an old House that have not dor and windows would you go in it? ('in') or go around ('left' or 'rigth') and I kan say you when you go to the Rigth you would become the same result. go 'in' Brother")
                print(answer, "whatever you do you will die. sorry i have no idea anymore.")
                break

        else:
            print("Invalid choice, you lost!")      
		
    else:
        print("Maybe next Time. Bye")
        break    