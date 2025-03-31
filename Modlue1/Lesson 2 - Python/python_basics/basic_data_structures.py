def main():
    print("====================TUPLE====================")
    # Tuple should be used when we just want to iterate over,
    # and don't want to add or remove anything, a tuple can be used
    # as a dict key since it is often hashable
    # https://stackoverflow.com/a/46335018 is the case where tuple is not hashable
    my_tuple = (1, 2, 3, 1)
    # my_tuple[1] = 4 # Error, since tuple is immutable
    print("My tuple: ", my_tuple)
    # Now, try to add elemenets to the tuple
    print(f"Old tuple id: ", id(my_tuple))
    my_tuple += (0, 0)
    # But the id of my_tuple has been changed
    print(f"New tuple id: ", id(my_tuple))

    print("====================LIST====================")
    # List is mutable, so we can add or remove elements,
    # but looking up elements is expensive in comparison with tuple
    # https://stackoverflow.com/a/40963434
    my_list = [1, 2, 3]
    print("My original list: ", my_list)
    print("My list with 3 appended: ", my_list + [3])
    print("My list with 0 prepended: ", [0] + my_list)

    print("====================SET====================")
    # Set is also mutable, but all the elements are unique,
    # and the order is not guaranteed
    my_set = set(my_tuple)
    print("My old set ID: ", id(my_set))
    # Add an element to the set
    my_set.add(4)
    # Add multiple elements to the set
    my_set.update([ 5, 6, 7])
    # Remove one
    my_set.remove(1)
    # It does not provide an untility option to remove multiple
    # use my_set - set([1, 1]) instead
    print("My new set ID: ", my_set)

    print("====================DICT====================")
    # Dict is mutable, used to store key/value pairs
    my_dict = {
        "a": 1,
        "b": 2
    }
    print("My dict: ", my_dict)
    print("Value of a: ", my_dict["a"])
    # Now add a different key
    my_dict["c"] = 3
    print("My new dict: ", my_dict)
    del my_dict["c"]
    print("My dict: ", my_dict)

    # Take a look at this to see more details about differences
    # between the above types https://i.stack.imgur.com/z3m5U.png

# This is only executed when invoking this script
if __name__ == '__main__':
    main()
