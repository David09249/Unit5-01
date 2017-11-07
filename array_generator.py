# Created by: David Wang
# Created on: 13-Nov-2017
# Created for: ICS3U
# Daily Assignment - Unit5-01
# This program generates 10 random numbers from 1-100 and calculates the average of those numbers

import ui
from numpy import random

my_numbers = []

def generate_random_numbers_touch_up_inside(sender):
    global my_numbers
    view['random_numbers_textview'].text = ''
    my_numbers = []
    for index1 in range(0, 10):
        my_numbers.append(float(random.randint(1, 100)))
        view['random_numbers_textview'].text = (view['random_numbers_textview'].text + str(my_numbers[index1]) + '\n')

def calculate_average_touch_up_inside(sender):
    average = 0
    global my_numbers
    for index2 in my_numbers:
        average = average + index2
    average = average / len(my_numbers)
    view['average_label'].text = 'The average of the numbers is: ' + str(average)

view = ui.load_view()
view.present('fullscreen')
