class VendingMachine:
    def __init__(self):
        self.bottles = 20
    
    def purchase(self, amount):
        comparisonNumber = self.bottles
        self.bottles = self.bottles - amount
        
        if amount > comparisonNumber:
            print("Please try again with a number less than inventory.")
            exit()

        
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print('Inventory: {} bottles'.format(self.bottles))
