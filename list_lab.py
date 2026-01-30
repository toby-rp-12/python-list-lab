# List Lab Starter
# Students: fill in code for Series 1–4 below

def series1():
    #Step 1
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print("Series 1:", fruits)

    #Step 2
    fruits.append(input("Enter another fruit to add to the list: > "))
    print("Here is the list now:", fruits)

    #Step 3
    response = int(input("Now, please enter a number. > "))
    print("Fruit number", str(response), "in this list is:", fruits[response - 1])

    #Step 4
    fruits = [input("Enter another fruit to add to the list. > ")] + fruits
    print("Here is the list now:", fruits)

    #Step 5
    fruits.insert(0, input("Enter another fruit to add to the list. > "))
    print("Here is the list now:", fruits)

    #Step 6
    print("These are fruits that begin with the letter p:")
    for i in fruits:
        if i[0].lower() == "p":
            print(i)
    return fruits


def series2(fruits):
    # your code continues here, "pass" allows you to test your code with incomplete functions
    #Step 1
    print("Series 2 (aka series 1):", fruits)
    #Step 2
    fruits.pop()
    #Step 3
    print("Here is the new list, without the last fruit:", fruits)
    #Step 4
    response = input("Choose a fruit to remove from the list. > ")
    fruits.remove(response)
    print("Here's the list now:", fruits)


def series3(fruits):
    # your code continues here
    #Step 1
    for i in fruits[:]:
        #fruits[:] was a bug fix I found. It creates a copy of the list so multiple "no" answers don't mess up the loop.
        while True:
            response = input(f"Do you like {i.lower()}? > ").strip().lower()
            #Step 2
            if response == "no":
                fruits.remove(i)
                break
            elif response == "yes":
                break
            #Step 3
            else:
                print("Answer 'yes' or 'no' (all lowercase, no spaces).")
    #Step 4
    print("Here's the final list (fruits you like/series 3):", fruits)

def series4(fruits):
    # your code continues here
    #Step 1
    i_dont_wanna_name_this = [item[::-1] for item in fruits]
    #Step 2
    fruits.pop()
    #Step 3
    print("I just created a copy of the series 1 list where each string is reversed. Here it is:")
    print(i_dont_wanna_name_this)
    print("And here's the previous list (un-reversed) with the last item removed.")
    print(fruits)


def main():
    fruits = series1()
    #Again, using the same bug fix from series 3 to keep the list from series 1 as the one being modified in each series.
    fruitscopy1 = fruits[:]
    fruitscopy2 = fruits[:]
    series2(fruits)
    series3(fruitscopy1)
    series4(fruitscopy2)

# this just tells Python:
# "only run the code below if we are running THIS file directly"
# (not if another file tries to import this file)
# there is nothing to edit here
if __name__ == "__main__":
    main()
