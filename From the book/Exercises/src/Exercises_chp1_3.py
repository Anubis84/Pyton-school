# -*- coding: utf-8 -*-

'''
Created on 06/11/2012

@author: Anubis
'''
dairy_section = ['milk', 'chees','yhougert','something else']
print(dairy_section[0] + " " + dairy_section[-1])
milk_expiration = (24, 12, 2014)
print("this milk will expira on the %i in the %i month in the year of %i"%milk_expiration )
milk_carton = {}
milk_carton ["expiration"] = milk_expiration
milk_carton ["fl_oz"] = "2 liter"
milk_carton ["cost"] = 20
milk_carton ["brand_name"] = "Arla"

print(milk_carton.values())

print(milk_carton.get("cost")*6)

cheeses = ["ny ost", "baal ost", "ryge ost", "gammle ost"]

dairy_section.append(cheeses)

print(dairy_section)

dairy_section.remove(cheeses)

print(dairy_section)

print(len(cheeses))

print(cheeses[0][0:5])