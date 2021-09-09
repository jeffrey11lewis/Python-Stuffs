import random

total_dollars = random.randint(1,101)
total_cents = random.randint(0,101)

#print('dollars: ' + str(total_dollars))
#print('cents: ' + str(total_cents))

total = float(total_dollars) + float(total_cents )/ 100
print('total: ' + "${:,.2f}".format(total))

payment = round(random.uniform(total, total+100),2)

print('our payment was: ' + "${:,.2f}".format(payment))

change = payment - total

print('our change should be: ' + "${:,.2f}".format(change))

remaining_change = change

print('our remaining change is: ' + "${:,.2f}".format(remaining_change))
#create our change dictionary

currency_names = {
    20 :"twenties",
    10 : "tens",
    5: "fives",
    1 :"ones",
    0.25:"quarters",
    0.10:"dimes",
    0.05:"nickels",
    0.01:"pennies",
} 

currency_values = {
    20: 0,
    10: 0,
    5: 0,
    1: 0,
    0.25: 0,
    0.10: 0,
    0.05: 0,
    0.01: 0,
}

#figuring out how much change to give
types_of_money = currency_values.keys()
for denomination in types_of_money:
    #print('Considering the denomination: ' + "${:,.2f}".format(denomination))
    while denomination <= remaining_change:
        remaining_change -= denomination
        currency_values[denomination] += 1
        #print('our remaining change is: ' + "${:,.2f}".format(remaining_change))
    #print('we are going to give back '+ str(currency_values[denomination]) + 'of ' + "${:,.2f}".format(denomination))
    #print('our remaining change is: ' + "${:,.2f}".format(remaining_change))
sorted_keys = currency_values.keys()
for key in sorted_keys:
    print(str(key) + ': ' + str(currency_values[key]))

#count back change

end_of_transaction_total = total
print('your total was: ' + "${:,.2f}".format(end_of_transaction_total))
for denomination in reversed(types_of_money)
end_of_transaction_total -=currency_values[denomination] * denomination
for denomination in types_of_money:
    print(str(currency_values[denomination]) +' of '+ currency_names[denomination] + 'makes' + "${:,.2f}".format(end_of_transaction_total) )

if(end_of_transaction_total > total):
    print('you are giving money away!')
elif(end_of_transaction_total == total):
    print('good job.')

else:
    print('you are a THIEF.')
""""
sorted_keys = currency_values.keys()
for key in sorted_keys:
    print(str(key) )"""