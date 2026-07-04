# Python program to shuffle deck of cards

import random, itertools

deck = list(itertools.product(range(1, 14), ['Spades', 'Hearts', 'Diamonds', 'Clubs']))
random.shuffle(deck)
print(deck)

for i in range(5):
    print(deck[i][0], "of", deck[i][1])


# Python program to display calender

import calendar

year=int(input("Enter year:"))
month=int(input("Enter month:"))

calendar=calendar.month(year,month)
print(calendar)
