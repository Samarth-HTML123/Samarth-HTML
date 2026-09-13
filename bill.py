# ================================
# GROCERY BILLING QUEUE
# ================================

print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: the five counters ----------
# YOUR CODE HERE
# Three counters for the price bands: low_price_items, medium_price_items,
# high_price_items — all start at 0.
# Two more for the day: customers_served and total_sales — both start at 0.
# Also make a variable  billing = True  to control the outer loop.


# ---------- PART 2: the OUTER while loop — one customer per repeat ----------
# YOUR CODE HERE
# while billing:
#     ask for the customer's name
#     ask how many items they are buying, wrapped in int()


# ---------- PART 3: continue on a bad item count ----------
# YOUR CODE HERE
# Still inside the outer loop, before anything else happens:
# if the item count is 0 or less, print a message and use continue.


# ---------- PART 4: the INNER while loop — one item per repeat ----------
# YOUR CODE HERE
# Set customer_total = 0 and item_number = 1 first.
# Then:  while item_number <= item_count:
#            ask for item name, price, quantity
#            (price and quantity wrapped in int())


# ---------- PART 5: item total and price band ----------
# YOUR CODE HERE
# Inside the inner loop:
#   if price or quantity is 0 or less -> print a message and continue
#   item_total = price * quantity
#   print the line:    item_name: quantity x price = item_total
#   add item_total to customer_total
#   add quantity to the right band:  under 50 = low, 50 to 100 = medium, over 100 = high
#   add 1 to item_number      <- forget this and the loop never ends


# ---------- PART 6: finish the customer, ask about the next ----------
# YOUR CODE HERE
# Back out in the outer loop, after the inner loop has finished:
#   add 1 to customers_served, add customer_total to total_sales
#   print the customer's total
#   ask "Next customer? (yes/no): "
#   if the answer is not yes, set billing = False


# ---------- PART 7: the NESTED for report ----------
# YOUR CODE HERE
# After the outer loop has ended:
#   an outer for loop over the three bands
#   an inner for loop printing one * per item in that band, using end=""
# Then print customers_served and total_sales.