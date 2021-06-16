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

food_prices['chicken'] =  3
print('Te price of chicken after the price increase is', '$'+(chicken))