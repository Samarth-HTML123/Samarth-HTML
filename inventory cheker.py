items = ["pencil", "eraser", "notebook", "sharpener", "glue"]
stock_count = [12, 0, 8, 5, 3]

inventory = {item: count for item, count in zip(items, stock_count)}
print("Full inventory:",inventory)

in_stock_items = [item for item in items if inventory[item] > 0 ]
print("Items in stock:", in_stock_items)

choose_item = input("Which item do you want to buy?")

if choose_item not in inventory or inventory[choose_item] == 0:
    print(choose_item, "is out of stock! Stopping the checker.")
    exit()
    
price = [10, 5, 40, 15, 20]
markup = int(input("Enter the markup amount to add to every price:"))

marked_up_prices = list(map(lambda p: p + markup, price))
print("Marked up Prices:", marked_up_prices)

item_index = items.index(choose_item)
chosen_price = marked_up_prices(item_index)
print("Print of", choose_item, "after markup:", chosen_price)

inventory[choose_item] = inventory[choose_item] - 1
print(choose_item, "purchased! Remaning stock:", inventory[choose_item])

print("")
print("==== SCHOOL STORE INVENTORY CHECKER ====")
print("Item Bought:", choose_item)
print("Price Paid:", chosen_price)
print("Updated inventory:", inventory)
print("=========================================")
    
    
