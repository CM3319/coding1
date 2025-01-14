# lists are a datatype for collecting and grouping together
# other pieces of data 

# list can contain data types, including other lists.
# list can contain duplicate data

# input is a function that allows us to enter data directly into
# our program from the terminal
# data that is passed in from an input from an input function automatically becomes

name = input('What is your name?')
print(name)

# list functions

# insert()

skiiTripItems_ShoppingCart = ['gloves']
# insert() - Allows us to enter a new list item
# based on an index position
# insert requires 2 arguments to work.

skii_TripItems.insert('1, snow boots')
skii_TripItems.insert(2,'goggles')
print(skii_TripItems)

# append() - Allows to enter a new item into a list,
# without having to provide an index location, append() will
# automatically put the new item at the end of the list.


# remove() - allows us to remove an item on a list

skii_TripItems.remove('scarf')
print(skii_TripItems)

pop() - Allows us to remove last item in our list

skii_TripItems.pop()
print(skii_TripItems)

clear()/ del() - Allow us to delete/ remove all the 
# items in a list

del skii_TripItems


skii_TripItems.clear()
print(skii_TripItems)