test_dict = {' Codingal' : 3,  ' best' : 2, 'for ' : 2, 'coding' : 1,}

print("The original dicyionary :" + str(test_dict))

k = 2

res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res +1
        
print("Frequency of k is :" + str(res))