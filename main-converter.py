import length
import weight
import temperature
import volume

while True:
    print("---UNIT CONVERTER---")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature ")
    print("4. Volume")
    print("5. Exist")
    choice = input("Select a conversion category:")

    if choice == '1':
        print("Length selected")
        print("1. Kilometers to Meters")
        print("2. Meters to Kilometers")
        print("3. Meters to Centimeters ")
        print("4. Centimeters to meters")
        print("5.Centimeters to Millimeters")
        print("6. Millimeters to Centimeters")
        print("7. Miles to Kilometers")
        print("8. Kilometers to Miles")
        print("9. Inches to Centimeters ")
        print("10. Centimeters to Inches")
        conversion = input("Choose your conversion:")

        if conversion == '1':
            num = float(input("Enter kilometers:"))
            answer = length.km_to_m(num)
            print(answer, "meters")

        elif conversion == '2':
            num = float(input("Enter Meters:"))
            answer = length.m_to_km(num)
            print(answer, "kilometers")

        elif conversion == '3':
            num = float(input("Enter Meters"))
            answer = length.m_to_cm(num)
            print(answer, "centimeters")

        elif conversion == '4':
            num = float(input("Enter Centimeter"))
            answer = length.cm_to_m(num)
            print(answer, "meters")

        elif conversion == '5':
            num = float(input("Enter Centimeter"))
            answer = length.cm_to_mm(num)
            print(answer, "millimeters")

        elif conversion == '6':
            num = float(input("Enter millimeter"))
            answer = length.mm_to_cm(num)
            print(answer, "centimeters")

        elif conversion == '7':
            num = float(input("Enter Miles"))
            answer = length.miles_to_km(num)
            print(answer, "kilometers")

        elif conversion == '8':
            num = float(input("Enter Kilometers"))
            answer = length.km_to_miles(num)
            print(answer, "miles")

        elif conversion == '9':
            num = float(input("Enter Inches"))
            answer = length.inches_to_cm(num)
            print(answer, "centimeters")

        elif conversion == '10':
            num = float(input("Enter Centimeters"))
            answer = length.cm_to_inches(num)
            print(answer, "inches")

        else:
            print("Invalid Selection")



    elif choice == '2':
        print("Weight selected")
        print("1. Kilograms to Grams")
        print("2. Grams to Kilograms")
        print("3. Kilograms to Pounds ")
        print("4. Pounds to Kilograms")
        print("5. Grams to Milligrams")
        print("6. Milligrams to Grams")
        print("7. Kilograms to Milligrams")
        print("8. Milligrams to Kilograms")

        conversion = input("Choose your conversion:")
        if conversion == '1':
            num = float(input("Enter kilogram:"))
            answer = weight.kg_to_g(num)
            print(answer, "grams")

        elif conversion == '2':
            num = float(input("Enter grams:"))
            answer = weight.g_to_kg(num)
            print(answer, "kilograms")

        elif conversion == '3':
            num = float(input("Enter kilogram:"))
            answer = weight.kg_to_p(num)
            print(answer, "pounds")

        elif conversion == '4':
            num = float(input("Enter pounds:"))
            answer = weight.p_to_kg(num)
            print(answer, "kilograms")

        elif conversion == '5':
            num = float(input("Enter gram:"))
            answer = weight.g_to_mg(num)
            print(answer, "milligrams")

        elif conversion == '6':
            num = float(input("Enter milligrams:"))
            answer = weight.mg_to_g(num)
            print(answer, "grams")

        elif conversion == '7':
            num = float(input("Enter kilograms:"))
            answer = weight.kg_to_mg(num)
            print(answer, "milligrams")

        elif conversion == '8':
            num = float(input("Enter milligrams:"))
            answer = weight.mg_to_kg(num)
            print(answer, "kilograms")

        else:
            print("Invalid Selection")



    elif choice == '3':
        print("Temperature selected")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin ")
        print("4. Kelvin to Celsius")
        print("5. fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")

        conversion = input("Choose your conversion:")
        if conversion == '1':
            num = float(input("Enter Celsius :"))
            answer = temperature.c_to_f(num)
            print(f"{answer} ºF")

        elif conversion == '2':
            num = float(input("Enter Fahrenheit :"))
            answer = temperature.f_to_c(num)
            print(f"{answer} ºC")

        elif conversion == '3':
            num = float(input("Enter Celsius :"))
            answer = temperature.c_to_k(num)
            print(f"{answer} K")

        elif conversion == '4':
            num = float(input("Enter Kelvin :"))
            answer = temperature.k_to_c(num)
            print(f"{answer} ºC")

        elif conversion == '5':
            num = float(input("Enter Fahrenheit :"))
            answer = temperature.f_to_k(num)
            print(f"{answer} K")

        elif conversion == '6':
            num = float(input("Enter Kelvin :"))
            answer = temperature.k_to_f(num)
            print(f"{answer} ºF")

        else:
            print("Invalid Selection")


    elif choice == '4':
        print("Volume selected")
        print("1. Liters to Milliliters")
        print("2. Milliliters to Liters")
        print("3. Liters to Cups ")
        print("4. Cups to Liters")
        print("5. Cups to Milliliters")
        print("6. Milliliters to cups")
        print("7. Liters to Gallons")
        print("8. Gallons to Liters")

        conversion = input("Choose your conversion:")
        if conversion == '1':
            num = float(input("Enter Liters"))
            answer = volume.l_to_ml(num)
            print(answer, "ml")

        elif conversion == '2':
            num = float(input("Enter Milliliters:"))
            answer = volume.ml_to_l(num)
            print(answer, "l")

        elif conversion == '3':
            num = float(input("Enter Liters:"))
            answer = volume.l_to_cups(num)
            print(answer, "cups")

        elif conversion == '4':
            num = float(input("Enter Cups:"))
            answer = volume.cups_to_l(num)
            print(answer, "l")

        elif conversion == '5':
            num = float(input("Enter cups:"))
            answer = volume.cups_to_ml(num)
            print(answer, "ml")

        elif conversion == '6':
            num = float(input("Enter Milliliters:"))
            answer = volume.ml_to_cups(num)
            print(answer, "cups")

        elif conversion == '7':
            num = float(input("Enter Liters:"))
            answer = volume.l_to_gallons(num)
            print(answer, "gallons")

        elif conversion == '8':
            num = float(input("Enter Gallons:"))
            answer = volume.gallons_to_l(num)
            print(answer, "l")

        else:
            print("Invalid Selection")



    elif choice == '5':
        print("Thank you for using the converter!")
        break
    else:
        print("Invalid selection")
