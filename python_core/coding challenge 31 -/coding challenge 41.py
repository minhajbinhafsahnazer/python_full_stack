phone = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_list = sorted(phone,key = lambda x : int(x['model']))

for i in sorted_list:
    print(i)
