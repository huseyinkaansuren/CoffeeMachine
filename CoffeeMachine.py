MENU = {
    "espresso": {"ingredients": {"water": 50,"coffee": 18,}, "cost": 1.5,},
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


profit=0
should_continue=True
#QUARTERS=$0.25
#DIME=$0.10
#NICKEL=$0.05
#PENNY=$0.01

# TODO:1.print report of all coffee machine resources
def report(resource_water, resource_milk, resource_cofee,money):
    print(f"Coffee Machine Resource Report:")
    print(f"Water:{resource_water}ml")
    print(f"Milk:{resource_milk}ml")
    print(f"Coffee:{resource_cofee}g")
    print(f"Money:${money}")


#TODO:5.after getting coffee calculate machine resources
def coffee_maker(selected_coffee,coffee_resources):
    for item in coffee_resources:
        resources[item]-=coffee_resources[item]
    print(f"Here is your {selected_coffee}, Enjoy :)")

#TODO:2.check machine resources
def is_enough_resource(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item]>resources[item]:
            print("Sorry not enough resource in machine")
            return False
    return True
#TODO:3.proccess money
def insert_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?:")) * 0.25
    dimes = int(input("How many dimes?:")) * 0.10
    nickel = int(input("How many nickels?:")) * 0.05
    penny = int(input("How many pennies?:")) * 0.01
    total = quarters + dimes + nickel + penny
    return total
#TODO:4.calculate the coffee amount and check it
def is_money(money,amount):
    if money >= amount:
        change=round(money-amount,2)
        print(f"Here is ${change} in change")
        global profit
        profit+=amount
        return True
    else:
        print("Not Enough Money")
        return False


while should_continue:
    selection=input("What would you like? (espresso/latte/cappuccino):").lower()
    if selection=="report":
        report(resources["water"], resources["milk"], resources["coffee"],profit)
    elif selection=="off":
        print("Closing")
        should_continue=False
    else:
        coffee=MENU[selection]
        if is_enough_resource(coffee["ingredients"]):
            user_price=insert_money()
            if is_money(user_price,coffee["cost"]):
                coffee_maker(selection,coffee["ingredients"])
