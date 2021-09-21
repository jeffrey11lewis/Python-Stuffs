class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print('Inventory: {} bottles'.format(self.bottles))

if __name__ == "__main__":
    # TODO: Create VendingMachine object
    theMachine = VendingMachine()
    # TODO: Purchase input number of drinks
    print("Enter the amount of drinks purchased:")
    purchaseInput = int(input())
    theMachine.purchase(purchaseInput)
    # TODO: Restock input number of bottles
    print("Enter the amount of drinks restocked:")
    restockInput = int(input())
    theMachine.restock(restockInput)
    # TODO: Report inventory
    theMachine.report()
    