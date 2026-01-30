# python-list-lab
This is my first list program in python.

## Project Overview

This project is a Python list lab that walks through four different exercises (Series 1–4) focused on practicing list operations, user input, loops, and string manipulation.

The program is interactive and runs entirely in the command line.

The goal of this lab is to build familiarity with Python lists by:
- Adding and removing items
- Accessing items by index
- Copying lists safely
- Iterating through lists
- Modifying lists based on user input
- Working with strings inside lists

Each “series” builds on the previous one while demonstrating different list behaviors.

## Key Features

- Interactive user input
- List appending, inserting, and removing
- Index-based list access
- Input validation using loops
- Safe list copying to avoid iteration bugs
- String reversal using list comprehensions
- Clear separation of tasks into functions
## Series Breakdown

### Series 1
- Starts with a predefined list of fruits
- Allows the user to add fruits
- Accesses fruits by number
- Inserts fruits at the beginning of the list
- Displays fruits that start with the letter **P**

### Series 2
- Removes the last fruit from the list
- Allows the user to choose a fruit to remove
- Prints the updated list

### Series 3
- Asks the user whether they like each fruit
- Removes fruits the user does not like
- Validates input to accept only `yes` or `no`
- Displays a final list of liked fruits

### Series 4
- Creates a copy of the original list with each fruit name reversed
- Removes the last fruit from the original list
- Prints both the modified original list and the reversed copy

## Requirements & How to Run

### Requirements:
- Python 3.x
- No external libraries required

### How to Run:

1. Make sure Python 3 is installed.
2. Save the file, calling it something like:
```
list_lab.py
```
3. Navigate to the folder containing the file.
4. Run the program using python.

## Example Interaction
```
Series 1: ['Apples', 'Pears', 'Oranges', 'Peaches']
Enter another fruit to add to the list: > Mango
Now, please enter a number. > 2
Fruit number 2 in this list is: Pears
Do you like apples? > yes
Do you like pears? > no
Answer 'yes' or 'no' (all lowercase, no spaces).
```
