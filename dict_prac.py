# declare dictionary of foods

food_prices = {"Chicken": 1.59,
                 "Beef": 1.99,
                 "Cheese": 1,
                 "Milk": 2.5}

video_games = {'Halo': 'Shooter',
                'FiFA 21' : 'Sport',
                'It Takes Two': 'Adventure',
                'Outlast II' :'Horror'}

print("Halo is a", video_games['Halo'])

chicken = food_prices['chicken']
beef = food_prices['Beef']
pork = food_prices['Pork']
tofu = food_prices['Tofu']

print('The price of chicken is', '$'+str(chicken))
print('The price of beef is', beef)
print('The price of pork is', pork)
print('The price of tofu is', tofu)

food_prices["chicken"] =  3
chicken = food_prices['chicken']

print('The price of chicken after the price increase is', '$'+(chicken))

#Lab 4 functons
def total_price(food_1, food_2):
    """Returns the total price of given foods"""
    
    total = food_prices[food_1] + food_prices[food_2]

    return total

print(total_price('beef', 'Pork'))

"""values = food_prices.values()
print(food_prices)  
print(list(values)[0]) This prints the value of foodprice by converting the values from
the dictionary to a list"""

def price_diference(food_1, food_2):
    """Returns the difference of given foods"""
    
    difference = food_prices[food_1] - food_prices[food_2]

    if difference < 0:
        return "Price cannot be less than 0."
    else:
        return difference

print(total_price('Tofu', 'Pork'))

def Full_price(Item1,Item2):
    price = food_prices[Item1] + food_prices[Item2] 
    print("Total price of", Item1 , "and" , Item2 ,"is", price)

Full_price("Chicken","Beef")
