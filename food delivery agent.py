class FoodDeliveryAgent:
    def __init__(self):
        self.menu = {
            "Pizza": 8,
            "Burger": 5,
            "Pasta": 7,
            "Salad": 4
        }
        self.order = []
        self.total = 0
        self.address = ''

    def show_menu(self):
        '''
        Agent: Welcome to Food Delivery! Here are the items we have: 
        1. Pizza     -   $8 
        2. Burger    -   $5 
        3. Pasta     -   $7 
        4. Salad     -   $4 
        Please type the item(s) you want to order (separate with commas if more than one).
        '''

        print("\nAgent: Welcome to Food Delivery! Here are the items we have:")

        for num, (itm, amnt) in enumerate(self.menu.items(), 1):
            print(f"{num}. {itm}\t - \t${amnt}")

        print("Please type the item(s) you want to order (separate with commas if more than one).\n")

    def get_order(self):
        '''
        User: Pizza, Pasta 
        Agent: You have chosen Pizza and Pasta. The total is $15.
        '''

        choices = input("User: ")
        order = [itm.strip().title() for itm in choices.split(',')]
        unknown = []

        for item in order:
            if item in self.menu:
                self.order.append(item)
                self.total += self.menu[item]
            else:
                unknown.append(item)

        if unknown != []:
            if len(unknown) == 1:
                print(f"Agent: Sorry! {unknown[0]} is not on the menu.")
            else:
                print(
                    f"Agent: Sorry! {','.join(unknown)} are not on the menu.")

        if len(self.order) == 1:
            print(
                f"Agent: You have chosen {self.order[0]}. The total is ${self.total}.")
        elif len(self.order) == 2:
            order_str = ', '.join(self.order[:-1])
            order_str = order_str + ', and ' + self.order[-1]

            print(
                f"Agent: You have chosen {order_str}. The total is ${self.total}.")

    def get_address(self):
        '''
        Please provide your delivery address: 
        User: 123 Main St, Cityville 
        '''

        print("Please provide your delivery address:")
        self.address = input("User: ").strip()

    def start(self):
        '''
        Agent: Hello! How can I assist you today?
        User: I want to order food.
        '''

        print("Agent: Hello! How can I assist you today?")

        while True:
            prompt = input("User: ")

            if 'order food' in prompt.lower():
                break

            print("Agent: Please enter a valid phrase to proceed.")

        self.show_menu()
        self.get_order()
        self.get_address()
