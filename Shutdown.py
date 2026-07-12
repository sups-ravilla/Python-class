def shutdown():

    user_input = input("Do you want to shut down? (Yes/No): ")

    if user_input == "Yes":
        next = input("Has all tabs been closed? (Yes/No): ")
        if next == "Yes":
            print("Shutting down computer")
        elif next == "No":
            sure=input("Do you still want to shut down and lose some of your unsaved work or not? (Yes/No):")
            if sure == "Yes":
                print("Computer shutting down")
            elif sure == "No":
                print("Finish your work then shut down")
    elif user_input == "No":
        print("abort shut down")
    else:
        print("sorry.")

shutdown()