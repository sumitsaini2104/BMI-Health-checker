# Simple BMI Health Checker
# field: healthcare

def calc_bmi(weight, height):
    # weight in kg, height in meter
    bmi = weight / (height * height)
    return bmi

def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== BMI Health Checker ===")
    print("Type q at any time to exit.\n")

    history = []  # to store past BMI values (optional, just a simple list)

    while True:
        wt = input("Enter weight in kg (or q to quit): ")
        if wt.lower() == "q":
            break

        ht = input("Enter height in meter (or q to quit): ")
        if ht.lower() == "q":
            break

        # basic check
        if wt.strip() == "" or ht.strip() == "":
            print("Please enter some value.\n")
            continue

        try:
            wt = float(wt)
            ht = float(ht)
        except ValueError:
            print("Please enter numbers only.\n")
            continue

        if wt <= 0 or ht <= 0:
            print("Weight and height must be positive.\n")
            continue

        bmi = calc_bmi(wt, ht)
        status = bmi_status(bmi)

        history.append(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Status: {status}\n")

    # when loop ends
    print("\nProgram ended.")
    if history:
        print("You calculated BMI", len(history), "time(s) in this session.")

if __name__ == "__main__":
    main()