def main():
    height_feet = int(input("Please enter your height (ft.): "))
    height_inch = int(input("Please enter your height (in.): "))
    weight = int(input("Please enter your weight (lbs.): "))

    # Calculate BMI based on values inputted
    bmi = round(calculate_bmi(height_feet, height_inch, weight), 1)
    #print("BMI: ", bmi)

    # Outputs message based on BMI value
    if bmi < 18.5:
        print("Underweight")
        
    elif bmi >= 18.5 or bmi < 25:
        print("Normal Weight")

    elif bmi >= 25 or bmi < 30:
        print("Overweight")

    elif bmi >= 30:
        print("Obese")


# Returns BMI value
def calculate_bmi(feet, inch, weight):

    # Step 1
    kg = weight * 0.45

    # Returns height in inches
    height_inch = calculate_height(feet, inch)

    # Step 2
    height_meter = height_inch * 0.025

    # Step 3
    height_meter *= height_meter

    # Step 4
    result = kg/height_meter

    return result


# Calculates height in inches
def calculate_height(feet, inch):
    flag = feet * 12
    flag += inch

    return flag


if __name__ == "__main__":
    main()



