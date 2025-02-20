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
        1. Pizza - $8 
        2. Burger - $5 
        3. Pasta - $7 
        4. Salad - $4 
        Please type the item(s) you want to order (separate with commas if more than one).
        '''

        print("\nAgent: Welcome to Food Delivery! Here are the items we have:")

        for num, (itm, amnt) in enumerate(self.menu.items(), 1):
            print(f"{num}. {itm}\t - \t${amnt}")

        print("Please type the item(s) you want to order (separate with commas if more than one).\n")
