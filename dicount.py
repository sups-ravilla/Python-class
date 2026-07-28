valid = False

while not valid:
    try:
        bill_amount, discount_percent, people = input(
            "Enter bill amount, discount percent, and people separated by commas: "
        ).split(",")

        alcohol = input("Have you purchased alcohol? (yes/no): ")

        bill_amount = float(bill_amount)
        discount_percent = float(discount_percent)
        people = int(people)

        if bill_amount <= 0 or discount_percent < 0 or people <= 0:
            raise ValueError

        discount_amount = bill_amount * discount_percent / 100
        final_amount = bill_amount - discount_amount
        amount_per_person = final_amount / people

    except ValueError:
        print("Invalid input! Enter values like this: 1000,10,2")

    except ZeroDivisionError:
        print("People cannot be 0. Please enter at least 1 person.")

    else:
        print("Original Bill:", bill_amount)
        print("Discount Percent:", discount_percent)
        print("Discount Amount:", discount_amount)
        print("Final Amount:", final_amount)
        print("Amount Per Person:", round(amount_per_person, 2))

        if alcohol.lower() == "yes":
            age = int(input("You have purchased alcohol. Please enter your age: "))
            if age < 21:
                print("You are not allowed to purchase alcohol. Please remove it from your bill.")
            else:
                print("You are allowed to purchase alcohol.")

        valid = True  

    finally:
        print("Thank you for shopping here at our store and we hope the products we sell meet up to your expectations and we hope to see you again soon.")