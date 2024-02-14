#!/usr/bin/env python
# coding: utf-8

"""This program is a virtual Cafe. You can 'buy' coffee muffins, bagels, and croissants. It will then calculate the price based on the number purchased,
calculate the sales tax, and print you a receipt."""

#prints the top border and introductory text
print("***************************************\nJared's Cafe")

#asks the user for their order and stores it as an integer
coffeeNumber = int(input('Number of coffees bought?'))

muffinNumber = int(input('Number of muffins bought?'))

bagelNumber = int(input('Number of bagels bought?'))

croissantNumber = int(input('Number of croissants bought?'))

#prints the closing border
print('***************************************\n')

#multiplies number of orders by price to get cost of specific items
coffeeCost = 5 * coffeeNumber

muffinCost = 8 * muffinNumber

bagelCost = 4 * bagelNumber

croissantCost = 6 * croissantNumber

#adds together cost of items to get the sum cost
sumCost = coffeeCost + muffinCost + bagelCost + croissantCost

#calculates the final price after sales tax
finalCost = sumCost * 1.06

#calculates the sales tax
salesTax = sumCost * 0.06

#prints the opening border and first line of user's receipt
print('***************************************\nMy Coffee and Muffin Shop Receipt')

#prints the dollar amount spent on coffee
print(str(coffeeNumber),
    'Coffee(s) at 5$ Each: $',
    (str(coffeeCost)) + ('.00'))

#prints the dollar amount spent on muffins
print(str(muffinNumber),
    'Muffin(s) at 8$ Each: $',
    (str(muffinCost)) + ('.00'))

#prints the dollar amount spent on bagels
print(str(bagelNumber),
    'Bagels(s) at 4$ Each: $',
    (str(bagelCost)) + ('.00'))

#prints the dollar amount spent on croissants
print(str(croissantNumber),
    'Bagels(s) at 6$ Each: $',
    (str(croissantCost)) + ('.00'))

#prints the sales tax
print('6% tax: $' + (str(salesTax)))

#prints the seperator line
print('---------')

#prints the final cost
print('Total: $' + (str(finalCost)))

#prints the closing border of the user's receipt
print('***************************************')

#prints thank you message
print("Thanks for shopping at Jared's Cafe!")
