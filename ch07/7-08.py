sandwich_orders = ['aaa', 'bbb', 'ccc']
finished_sandwichs = []

while 1:
    if len(sandwich_orders) == 0:
        break
    else:
        print("made your " + sandwich_orders[0] + " sandwich")
        finished_sandwichs.append(sandwich_orders[0])
        sandwich_orders.remove(sandwich_orders[0])

# print(finished_sandwichs)