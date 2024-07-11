def menu():
    # Function to display the main menu
    print(" ")
    print("**MAIN MENU**")
    print(" ")
    welcome_list = ["Welcome to the COVID 19 support service. Please select an option below:",
                    "1. Statistics",
                    "2. Prevention",
                    "3. Symptoms",
                    "4. Treatment",
                    "5. Report case",
                    "6. Exit"]

    # Loop through the welcome list to print each menu option
    for options in welcome_list:
        print(options)

menu() # Call the menu function to display the menu

# Get user's choice from the menu
choice = input("Enter choice (1/2/3/4/5/6):")

# Initial confirmed cases for different countries
SA_Case_num = 27403
China_Case_num = 170000
USA_Case_num = 82995

# Start a loop to process user's choice
while choice != 6:
    if choice == '1':
        # Option 1: Display statistics
        print("STATISTICS")
        print("Currently in SA there are", SA_Case_num, "Confirmed cases")
        print("Currently in China there are", China_Case_num, "Confirmed cases")
        print("Currently in USA there are", USA_Case_num, "Confirmed cases")
        print(" ")

         # Ask if the user wants to see more cases from random countries
        more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()

        def cases_menu():
            # Function to display the menu again and get user's new choice
            if more_cases == "n":
                menu()
                choice = int(input("Enter choice (1/2/3/4/5/6):"))

        cases_menu()
        # Loop to display confirmed cases for random countries
        while more_cases != "n":
            if more_cases == "y":
                num = input("To select a random Country, type a number from 0 TO 9:")
                if num == '0':
                    print("New Zealand has 4512 confirmed cases")
                    more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                    cases_menu()
                elif num == '1':
                    print("Ireland has 5287 confirmed cases")
                    more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                    cases_menu()
                elif num == '2':
                    print("Japan has 6363 confirmed cases")
                    more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                    cases_menu()
                elif num == '3':
                    print("Switzerland has 9896 confirmed cases")
                    more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                    cases_menu()
                elif num == '4':
                    print("Canada has 7123  confirmed cases")
                    more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                    cases_menu()
                elif num == '5':
                    print("Sweden has 8121 confirmed cases")
                    more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                    cases_menu()
                elif num == '6':
                    print("Australia has 7155 confirmed cases")
                    more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                    cases_menu()
                elif num == '7':
                    print("Thailand has 2166 confirmed cases")
                    more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                    cases_menu()
                elif num == '8':
                    print("Portugal has 7911 confirmed cases")
                    more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                    cases_menu()
                elif num == '9':
                    print("Germany has 3999 confirmed cases")
                    more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                    cases_menu()
                else:
                    print("Enter a number between 0 to 9")
                    cases_menu()
            else:
                print("Enter Y for Yes or N for No")
                more_cases = input("Would you like to see the Confirmed cases for a random country? y/n:").lower()
                cases_menu()

    if choice == '2':
        # Option 2: Display prevention tips
        print("PREVENTION")
        list_2 = ["To prevent the spread of Covid – 19:",
                "Clean your hands often, using soap and water, or alcohol-based hand rub.",
                "Maintain a safe distance from anyone who is coughing or sneezing.",
                "Don’t touch your nose and mouth with your bent elbow or a tissue when you cough or sneeze.",
                "Stay home if you feel unwell.",
                "Choose open, well-ventilated spaces over closed ones. Open a window if indoors.",
                "If you have a fever, cough and difficulty breathing, seek medical attention. Call in advance",
                "Follow the directions of your local health authority."
                ]

        # Loop through the prevention list to print each tip
        for option_2 in list_2:
            print(option_2)

       # Display the menu again and get user's new choice
        menu()
        choice = input("Enter choice (1/2/3/4/5/6):")

    elif choice == '3':
         # Option 3: Display symptoms
        print("SYMPTOMS")
        list_3 = [" ",
                "Most common symptoms:",
                "*Fever",
                "*Dry cough",
                "*Tiredness",
                "*Loss of taste or smell",
                " ",
                "Less common symptoms:",
                "*Sore throat",
                "*Headache",
                "*Aches and pains",
                "*Diarrhoea",
                " ",
                "Serious symptoms:",
                "*Difficulty breathing or shortness of breath",
                "*Loss of speech or mobility, or confusion",
                "*Chest pain"
                ]

        # Loop through the symptoms list to print each symptom
        for option_3 in list_3:
            print(option_3)

        # Display the menu again and get user's new choice
        menu()
        choice = input("Enter choice (1/2/3/4/5/6):")

    elif choice == '4':
         # Option 4: Display treatment tips
        print("TREATMENT")
        list_4 = ["If you feel sick you should rest, drink plenty of fluids, and eat nutritious food.",
                "Quarantine and stay in a separate room from other family members, and use a dedicated bathroom if possible.",
                "Clean and disinfect frequently touched surfaces.",
                "Call your health care provider immediately if you have any of these danger signs: difficulty breathing, loss of speech or mobility, confusion or chest pain.",
                "Stay positive by keeping in touch with loved ones by phone or online, and by exercising at home."
                ]
        # Loop through the treatment list to print each tip
        for option_4 in list_4:
            print(option_4)

         # Display the menu again and get user's new choice
        menu()
        choice = input("Enter choice (1/2/3/4/5/6):")

    elif choice == '5':
        # Option 5: Report a case
        print("REPORT CASE")
        symptoms = input("Do you have any of the symptoms? Y/N:").lower()

        if symptoms == "n":
            print("You do not have COVID-19")
            menu()
            choice = input("Enter choice (1/2/3/4/5/6):")

        elif symptoms == "y":
            temp = input("Is your temperature above 38.5°C? Y/N:").lower()
            if temp == "n":
                print("You do not have COVID-19")
                menu()
                choice = input("Enter choice (1/2/3/4/5/6):")

            if temp == "y":
                option_list = ["In which country are you select an option below",
                            "1. SA",
                            "2. China",
                            "3. USA"
                           ]
                # Loop through the option list to print each country
                for options in option_list:
                    print(options)

                num = input("Enter option (1/2/3):")

                if num == '1':
                    SA_Case_num += 1
                    print("You have COVID-19 please see Treatment")
                    print("Currently in SA there are", SA_Case_num, "Confirmed cases")
                    menu()
                    choice = input("Enter choice (1/2/3/4/5/6):")

                elif num == '2':
                    China_Case_num += 1
                    print("You have COVID-19 please see Treatment")
                    print("Currently in China there are", China_Case_num, "Confirmed cases")
                    menu()
                    choice = input("Enter choice (1/2/3/4/5/6):")

                elif num == '3':
                    USA_Case_num += 1
                    print("You have COVID-19 please see Treatment")
                    print("Currently in USA there are", USA_Case_num, "Confirmed cases")
                    menu()
                    choice = input("Enter choice (1/2/3/4/5/6):")

                else:
                    print("Enter a number between 1 to 3")
        else:
            print("Enter Y for Yes or N for No")

    elif choice == '6':
        # Option 6: Exit the program
        print("Thank you for using my program GOODBYE:)")
        exit()

    else:
        # Handle invalid input for the menu choice
        print(" ")
        print("!ENTER A NUMBER BETWEEN 1 to 6!")
        menu()
        choice = input("Enter choice (1/2/3/4/5/6):")







