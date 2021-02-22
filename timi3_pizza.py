import random
# class A

class Pizza:
    def __init__(self):
        self.pizza_id = 0
        self.new_id = 0

    def add_pizza(self, pizza_id, id_info, id_served, toppings):
        self.pizza_id = pizza_id
        id_served[pizza_id] = 'unserved'
        id_info[pizza_id] = random.choices(toppings, k=3)

    def mark_pizza_served(self, pizza_id, id_served):
        self.pizza_id = pizza_id
        id_served[pizza_id] = 'served'


    def all_pizzas(self, id_info):
        print('All Pizzas')
        for key, val in id_info.items():
            print('Pizza {}: {}'.format(key,val))

    def remove_all_served(self, id_info, id_served):
        for key in id_served.keys():
            if key == 'served':
                id_served.pop(key)
                id_info.pop(key)
        



def main():
    A = Pizza()
    id_served = {}
    with open("pizza.txt") as f:
        for line in f:
            (key,val) = line.split()
            id_served[int(key)] = val

    toppings = ['pepp', 'svepp', 'lauk', 'ólífur', 'ananas']
    id_info = {}
    for key in id_served.keys():
        id_info[key] = random.choices(toppings, k=3)
 
    A.mark_pizza_served(1, id_served)
    A.add_pizza(5, id_info, id_served, toppings)
    A.all_pizzas(id_info)
    A.remove_all_served(id_info, id_served)
    A.all_pizzas(id_info)


main()
    

