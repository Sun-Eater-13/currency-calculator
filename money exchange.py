import math

def exchange_money(budget, exchange_rate):
    return round(budget / exchange_rate, 2)
def get_change(budget, exchanging_value):
    return round(budget-exchanging_value, 2)
def get_value_of_bills(denomination, number_of_bills):
    return int(denomination*number_of_bills)
def get_number_of_bills(amount, denomination):
    return int(amount//denomination)
def exchangeable_value(budget, exchange_rate, spread, denomination):
    return budget/(exchange_rate*(1+spread))//denomination*denomination

def user_input_float(message):
    global user_input
    while True:
        try:
            user_input=float(input(message))
            if user_input>0:
                break
            else:
                print("Input proper number")
        except ValueError:
            print("Input proper number")

while True:
    user_input_float("Input your budget: ")
    budget=user_input
    budget1=round(budget, 2)
    if budget==budget1:
        break
    else:
        print("Input proper number")

user_input_float("Input exchange rate: ")
exchange_rate=user_input
user_input_float("Input spread (in %): ")
spread=user_input/100

while True:
    user_input_float("Input denomination: ")
    denomination=user_input
    denomination1=round(denomination, 0)
    if denomination==denomination1:
        break
    else:
        print("Input proper number")

exchanging_value=exchange_rate*exchange_money(budget, exchange_rate)
number_of_bills=math.floor(exchange_money(budget, exchange_rate)//denomination)
amount=exchange_money(budget, exchange_rate)

print(f"You should get: {exchange_money(budget, exchange_rate)} of new currency")
print(f"The remaining part of budget should be: {get_change(budget, exchanging_value)} of the original currency")
print(f"The value of bills you will actually get is: {get_value_of_bills(denomination, number_of_bills)} of the new currency")
print(f"The number of bills is: {get_number_of_bills(amount, denomination)}")
print(f"The exchangeable value is: {exchangeable_value(budget, exchange_rate, spread, denomination)} of the original currency")
