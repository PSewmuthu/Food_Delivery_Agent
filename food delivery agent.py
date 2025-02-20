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
