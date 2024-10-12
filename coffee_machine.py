MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            
        },
        "cost": 30#1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50#2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 100#3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
def is_resouces_suffiecent(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry there is no enough item{item}")
            return False
    return True

def process_coin():
    print("enter money ::")
    total = int(input("how much you have 10 notes "))*10
    total += int(input("how much you have 20 notes"))*20
    total += int(input("how much you have 50 notes"))*50
    total += int(input("how much you have 100 notes"))*100
    total += int(input("how much you have 200 notes"))*200
    return total

def is_transaction_complete(money_recive,drink_cost):
    if money_recive > drink_cost:
        change = money_recive-drink_cost
        print(f"your change sir ={change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("you dont have enough money your money refunded")
        return False
    
    
def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("your coffee sir")
    
    
    
    
profit = 0
should_continue = True
while should_continue:

    choice = input("What would you like? (espresso = 30rs /latte = 50rs /cappuccino = 100rs):")
    
    if choice == "off":
        print("thank you sir")
        should_continue = False
    
    elif choice == "report":
        print(f"water :{resources["water"]}")
        print(f"milk :{resources["milk"]}")
        print(f"coffee :{resources["coffee"]}")
        print(f"money:{profit}")
        
    else:
        drink = MENU[choice]
        if is_resouces_suffiecent(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_complete(payment,drink["cost"]):
                make_coffee(drink["ingredients"])
                
            
            
        


