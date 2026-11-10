import math


def calcFee(hours, decimals=2):
    fee = 5 + 2.50 * hours
    return round(fee, decimals)


def displayFee(fee):
    print("Parking fee: $", fee)


def movieModel(adCost):
    additional_attendees = 2 * round(math.sqrt(adCost))
    ticket_sales = (20 + additional_attendees) * 10
    profit = ticket_sales - (200 + adCost)
    return profit, additional_attendees


hours = float(input("Enter hours parked: "))
fee = calcFee(hours)
displayFee(fee)

print()
ad_cost = float(input("Enter advertising ($): "))
profit, additional_attendees = movieModel(ad_cost)
print("Additional Attendees:", additional_attendees)
print("Profit: $", round(profit, 2))
