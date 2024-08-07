class MultipleFuncations():
    def list_fields():
        fields = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        print("Sub-fields in AI are:")
        for field in fields:
            print(field)
    ##############################################################################
    def odd_even():
        try:
            number = int(input("Enter a number: "))
            if number % 2 == 0:
                print(f"{number} is an Even number")
            else:
                print(f"{number} is an Odd number")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    ###############################################################################
    def eligibility_for_marriage():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        
        if gender.lower() == "male" and age >= 21:
            print("ELIGIBLE")
        elif gender.lower() == "female" and age >= 18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    ###################################################################################
    def find_percent():
        Subject1 = 98
        Subject2 = 87
        Subject3 = 95
        Subject4 = 95
        Subject5 = 93
        
        total_marks = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        max_marks = 500  
        percentage = (total_marks / max_marks) * 100
        
        print(f"Subject1= {Subject1}")
        print(f"Subject2= {Subject2}")
        print(f"Subject3= {Subject3}")
        print(f"Subject4= {Subject4}")
        print(f"Subject5= {Subject5}")
        print(f"Total : {total_marks}")
        print(f"Percentage : {percentage}")
    ######################################################################################
    def triangle():
        height = float(input("Height: "))
        breadth = float(input("Breadth: "))
        area = (height * breadth) / 2
        
        print(f"Area formula: (Height * Breadth) / 2")
        print(f"Area of Triangle: {area}")
        
        height1 = float(input("Height1: "))
        height2 = float(input("Height2: "))
        breadth2 = float(input("Breadth: "))  # Use a different variable name for the second breadth
        perimeter = height1 + height2 + breadth2
        
        print(f"Perimeter formula: Height1 + Height2 + Breadth")
        print(f"Perimeter of Triangle: {perimeter}")


