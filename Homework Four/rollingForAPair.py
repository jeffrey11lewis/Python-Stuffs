import random

class GVDie:  
   def __init__(self):      
      # set default values
      self.my_value = random.randint(1, 6)
      self.rand = random.Random()

   def roll(self):
       self.my_value = self.rand.randint(1, 6)  
      
   # set the random number generator seed for testing
   def set_seed(self, seed):
       self.rand.seed(seed)
   
   # allows dice to be compared if necessary
   def compare_to(self, other):
       return self.my_value - d.my_value
       

def rolling_for_pair(d1, d2, val):
    d1.roll()
    d2.roll()
    rolls = 1
    while d1.my_value != val or d2.my_value != val:
       d1.roll()
       d2.roll()
       rolls += 1
    return rolls

if __name__ == "__main__":
    die1 = GVDie()   # Create a GVDie object
    die2 = GVDie()   # Create a second GVDie object
    die1.set_seed(15)   # Set the first GVDie object with seed value 15
    die2.set_seed(15)   # Set the second GVDie object with seed value 15

    print("Enter the value of die you want to roll a pair of:")    
    val = int(input())
    rolls = rolling_for_pair(die1, die2, val) # Should return the number of rolls to reach total.
    print('It took {} rolls to get a pair of {}\'s.'.format(rolls, val))