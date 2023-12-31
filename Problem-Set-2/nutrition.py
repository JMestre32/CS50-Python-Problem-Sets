#Hints: Rather than use a conditional with 20 Boolean expressions, 
#one for each fruit, better to use a dict to associate a fruit 
#with its calories!
#If k is a str and d is a dict, you can check whether k 
#is a key in d with code like:

#if k in d:
    #...
#Take care to output the fruit’s calories, not calories from fat!


#Declare a dict of fruits 

fruits = [
   {"name" : "apple", "calories": "130 Calories"},
    {"name" : "avocado" , "calories": "50 Calories"},
    {"name" : "banana" , "calories": "110 Calories"},
    {"name" :"cantaloupe" , "calories": "50 Calories"},
    {"name" :"grapefruit" , "calories": "60 Calories"},
    {"name" :"grapes" , "calories": "90 Calories"},
    {"name" :"honeydew melon" , "calories": "50 Calories"},
    {"name" :"kiwifruit" , "calories": "90 Calories"},
    {"name" :"lemon" , "calories": "15 Calories"},
    {"name" :"lime" , "calories": "20 Calories"},
    {"name" :"nectarine" , "calories": "60 Calories"}, 
    {"name" :"orange" , "calories": "80 Calories"},
    {"name" :"peach" , "calories": "60 Calories"},
    {"name" :"pear" , "calories": "110 Calories"},
    {"name" :"pineapple" , "calories": "50 Calories"},
    {"name" :"plums" , "calories": "70 Calories"},
    {"name" :"strawberries" , "calories": "50 Calories"},
    {"name" :"sweet cherries" , "calories": "100 Calories"},
    {"name" :"tangerine" , "calories": "50 Calories"},
    {"name" :"watermelon" , "calories": "80 Calories"}
]

fruit = input("Item: ").strip().lower()

#Look through fruit "name" section to see if it exists
#If it exists print it's "calories"

for f in fruits:
    if fruit in f["name"]:
        print(f["calories"])
        break

#So, f is essentially a temporary variable that takes on the value
#of each dictionary (fruit) in the fruits list one at a time. 
#The loop goes through each fruit in the list and checks if 
#the input fruit matches the name of that fruit. 
#If it finds a match, it prints the associated calories and 
#exits the loop. If no match is found after looping through 
#all the fruits, nothing is printed.