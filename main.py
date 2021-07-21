from data import data
from assets import art  # resources are imported from the resources file


class Printer:
    print(art.logo)
    print("TOCH-JOSH PRINTER")

    def __init__(self):  # resources are initialised in this init block
        self.resources_paper = data.resources['paper']
        self.resources_ink = data.resources['ink']
        self.profit = data.resources['profit']

        self.biyar = 5
        self.faiba = 10
        self.muri = 20
        self.wazobia = 50
        self.n_biyar = 0
        self.n_faiba = 0
        self.n_muri = 0
        self.n_wazobia = 0
        self.total_payment = 0
        self.cost = 0
        self.number_of_papers = 0
        self.ink_required = 0
        self.transaction_success = False
        self.user = ""
        self.continuity = ''
        self.ink_colored = data.FORMAT['coloured']['materials']['ink']
        self.price_colored = data.FORMAT['coloured']['price']
        self.ink_greyscale = data.FORMAT['greyscale']['materials']['ink']
        self.price_greyscale = data.FORMAT['greyscale']['price']
        self.prompt_user()

    def end_or_continue(self):  # This function ensure we are able to navigate through the prompt
        while True:
            try:
                print()
                self.continuity = input("Enter 'y' to continue or 'n' to turn off ")
                if self.continuity in ['y', 'n']:
                    if self.continuity.lower() == "y":
                        self.prompt_user()
                    else:
                        print("Goodbye :)")
                        exit()
                else:
                    raise Exception
            except Exception:
                print("invalid option")

    def prompt_user(self):
        while True:
            try:
                self.user = input("""
Hello there, what would you like to do?
>> enter 'c' for colored or 'g' for greyscale to choose print format
>> enter 'r' to view resources report
>> enter 'o' to switch off printer: """)  # the prompt start here
                if self.user in ["c", 'r', "g", "o"]:
                    # error is handled to ensure only the required options are entered
                    # all the functions are chained together here to ensure dynamism of the program
                    if self.user.lower() == "c":
                        self.check_colored_resources()
                        self.resources_update()
                        self.bill_processing()
                        self.end_or_continue()
                    elif self.user.lower() == "g":
                        self.check_greyscale_resources()
                        self.bill_processing()
                        self.resources_update()
                        self.end_or_continue()
                    elif self.user.lower() == 'r':
                        self.view_resources()
                        self.end_or_continue()
                    elif self.user.lower() == "o":
                        print("Goodbye :)")
                        exit()
                else:
                    raise Exception
            except Exception:
                print("Invalid option")

    def check_colored_resources(self):

        # this function checks if the available resources will cater for colored printing
        print()
        self.number_of_papers = int(input("How many papers would you like to print? "))
        self.ink_required = self.ink_colored * self.number_of_papers
        self.cost = self.number_of_papers * self.price_colored
        if self.number_of_papers <= self.resources_paper and self.ink_required <= self.resources_ink:
            print()
            print(f"Your bill is {self.cost} naira only")
        elif self.number_of_papers > self.resources_paper:
            print()
            print("There is not enough papers available")
            self.end_or_continue()
        elif self.ink_required > self.resources_ink:
            print()
            print("There is not enough ink available")
            self.end_or_continue()

    def check_greyscale_resources(self):

        # this function checks if the available resources will cater for greyscale printing
        self.number_of_papers = int(input("How many papers would you like to print? "))

        self.ink_required = self.ink_greyscale * self.number_of_papers
        self.cost = self.number_of_papers * self.price_greyscale
        if self.number_of_papers <= self.resources_paper and self.ink_required <= self.resources_ink:
            print()
            print(f"Your bill is {self.cost} naira only")
        elif self.number_of_papers > self.resources_paper:
            print()
            print("There is not enough papers available")
            self.end_or_continue()
        elif self.ink_required > self.resources_ink:
            print()
            print("There is not enough ink available")
            self.end_or_continue()

    def bill_processing(self):
        # this function processes the payment bill based on the consumed resources
        while True:
            try:
                self.n_biyar = int(input(">> how many biyar are you paying with? "))
                self.n_faiba = int(input(">> how many faiba are you paying with? "))
                self.n_muri = int(input(">> how many muri are you paying with? "))
                self.n_wazobia = int(input(">> how many wazobia are you paying with? "))
                if self.n_biyar is not int and self.n_faiba is not int and self.n_muri is not int and self.n_wazobia is not int:
                    raise Exception
            except Exception:
                print("Enter amount in numbers only")

            self.total_payment = (
                        (self.n_biyar * self.biyar) + (self.faiba * self.n_faiba) + (self.muri * self.n_muri) + (
                        self.wazobia * self.n_wazobia))

            if self.total_payment == self.cost:
                self.transaction_success = True
                print("Printing.....")
                print("Here is your Project. and Thank you for using our services")
                self.resources_update()
                self.end_or_continue()
            elif self.total_payment > self.cost:
                self.transaction_success = True
                print("Printing.....")
                print(f"Here's your change of {self.total_payment - self.cost}, and Thank you for using our services")
                self.resources_update()
                self.end_or_continue()
            else:
                print("Sorry that’s not enough money. Money refunded")
                self.end_or_continue()

    def resources_update(self):
        # this function updates the resources after every transaction
        if self.transaction_success:
            self.resources_paper -= self.number_of_papers
            self.resources_ink -= self.ink_required
            self.profit += self.cost

    def view_resources(self):
        # this function help is called to view the current status of the resources.
        print()
        print({"papers": self.resources_paper,
               "ink": self.resources_ink,
               "profit": self.profit
               })


Printer()
