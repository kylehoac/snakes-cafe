
print("*"*38)
print("""**    Welcome to the Snakes Cafe    **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **""")
print("*"*38)
print("""
Appetizers
----------
Wings
Cookies
Spring Rolls
""")

print("""Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
""")

print("""Desserts
--------
Ice Cream
Cake
Pie
""")

print("""Drinks
------
Coffee
Tea
Unicorn Tears
""")

menu_items = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0,
}
cart = []

while True:
    print("*"*35)
    print("** What would you like to order? **")
    print("*"*35)
    response = input("> ")
    if response == "exit":
        break
    else:
        menu_items[response] += 1
        order_count = menu_items[response]
        print(f"** {order_count} order of {response} have been added to your meal **")