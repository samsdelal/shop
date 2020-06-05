"""Этот проект я попробовал сделать полностью на англйиском"""
import json

class Loaditems:

    def __init__(self):
        with open('items.txt') as f1:
            self.items = json.loads(f1.read())


    def __repr__(self):
        return self.items['items']

class Market(Loaditems):

    check_out = {}

    def __init__(self):
        Loaditems.__init__(self)


    def add_check(self, item):
        try:
            self.check_out[item] = self.items['items'][item]
            print('✓ The product was successfully added to the cart!')
        except KeyError:
           print(f'Sorry, but we cannot find {item} in our shop ☹')

    def delete_item(self, item):
        try:
            del self.check_out[item]
            print('✓ The product was successfully deleted from the cart!')
        except KeyError:
            print(f'Sorry, but we cannot find {item} in our check ☹')

    def show_all(self):
        for i in (self.items['items']):
            print(f'✔ {i} ─ {self.items["items"][i]}$')
        print('☞If you want to buy some thing use add_check method\n☞If you want to delete some thing use  delete_item method')

    def my_cart(self):
        for i in (self.check_out):
            print(f'⇨ {i} ─ {self.check_out[i]}$')

    def buy(self):
        cost = 0
        for i in self.check_out:
            cost += int(self.check_out[i])
        print(f'Cost of your purchase is {cost}$. Thank you for your purchase!')


    def __str__(self):
        return self.items






