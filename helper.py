
class DailyMessage:

    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter today's message: ")

    def print_message(self):
        print("Here is your message capitalised:", self.message.upper())


daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()


class HelperSession:

    def __init__(self):
        print("Helper session created")

    def __del__(self):
        print("Helper session ending")

    def create_session():
        print("Making your session")
        session = HelperSession()
        print("Session is ready")
        return session


print("")
print("Calling create_session() function...")
session_obj = HelperSession.create_session()
print("Program is still running...")
class PairFinder:
 
    def find_pair(self, numbers, target):
        lookup = {}
 
        for index, number in enumerate(numbers):
            needed_number = target - number
 
            if needed_number in lookup:
                return (lookup[needed_number], index)
 
            lookup[number] = index
 
        return None
 
 
numbers = (10, 20, 30, 40, 50, 60, 70)
 
target_value = int(input("Enter the ammount of time you want to study today: "))
 
result = PairFinder().find_pair(numbers, target_value)
 
if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found.")
 
del session_obj
print("Program End")

