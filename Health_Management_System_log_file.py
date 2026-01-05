
            if client == '1':
                excersise = input("Which excersise has been you done?\n⤷ ").strip().title()
                set_up("Excersise.log", client_name, excersise)
            
            elif client == '2':
                diet = input("Which diet has been you taken?\n⤷ ").strip().title()
                set_up("Diet.log", client_name, diet)
                
            else:
                print("Invalid input!")
                
    else: 
        print("Invalid input!!")

except KeyboardInterrupt:
    print(f"\nOperation cancelled by user")

finally:
    print("DONE")