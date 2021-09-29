if __name__ == "__main__":
    
    from vendingMachineExtension import VendingMachine
    #  Create VendingMachine object
    theMachine = VendingMachine()
    # Purchase input number of drinks
    print("Initial Inventory: 20" )
    print("Enter the amount of drinks purchased:")
    purchaseInput = int(input())
    theMachine.purchase(purchaseInput)
    #  Restock input number of bottles
    print("Enter the amount of drinks restocked:")
    restockInput = int(input())
    theMachine.restock(restockInput)
    # Report inventory
    theMachine.report()


    