"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    # SOLUTION 1:
    for item in items:
        print item


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """

    # SOLUTION 1:
    # long_words = []
    # for word in words:
    #     if len(word) > 4:
    #         long_words.append(word)
    # return long_words

    #SOLUTION 2:
    long_words = [word for word in words if len(word) > 4]

    return long_words


def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    # SOLUTION 1:
    # n_long_words = []
    # for word in words:
    #     if len(word) > n:
    #         n_long_words.append(word)
    # return n_long_words

    # SOLUTION 2:
    n_long_words = [word for word in words if len(word) > n]

    return n_long_words


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """

    # SOLUTION 1:
    # if numbers == []:
    #     return

    # else:
    #     smallest_num = ""
    #     for index in range(len(numbers)):
    #         compare1 = numbers[index]
    #         if compare1 < smallest_num:
    #             smallest_num = compare1
    #         elif compare1 > smallest_num:
    #             smallest_num = smallest_num
    #     return smallest_num

    # SOLUTION 2:
    # if numbers == []: # If the list is empty, return "None"
    #     return

    # else:
    #     smallest_num = ""
    #     for number in numbers:
    #         if type(number) != int: # If there is an input that is not an integer, inform the user and break.
    #             return "Invalid Entry: Input must be given as a list of integers."
    #             break
    #         else:
    #             if number < smallest_num:
    #                 smallest_num = number

    #     return smallest_num

    # SOLUTION 3: (barely changed from SOL2 -- just gave smallest_num an int value to start).
    if numbers == []: # If the list is empty, return "None"
        return

    else:
        smallest_num = numbers[0]
        for number in numbers: # Decided not to start at numbers[1] just in case the user only put in one argument.
            if type(number) != int: # If there is an input that is not an integer, inform the user and break.
                return "Invalid Entry: Input must be given as a list of integers."
                break
            else:
                if number < smallest_num:
                    smallest_num = number

        return smallest_num


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """

    if numbers == []: # If the list is empty, return "None"
        return

    else:
        largest_num = numbers[0]
        for number in numbers: # Decided not to start at numbers[1] just in case the user only put in one argument.
            if type(number) != int: # If there is an input that is not an integer, inform the user and break.
                return "Invalid Entry: Input must be given as a list of integers."
                break
            else:
                if largest_num < number:
                    largest_num = number

        return largest_num


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    return [number/float(2) for number in numbers]


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """

    return [len(word) for word in words]


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """

    sum_all = 0
    for number in numbers:
        sum_all += number

    return sum_all


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """

    product = 1
    for number in numbers:
        product *= number

    return product


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """

    joined_string = ""
    for word in words:
        joined_string += word

    return joined_string


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """
    if numbers == []:
        return "I can't give you an average without any numbers!"

    else:
        number_of_numbers = len(numbers)
        sum_all = 0

        for number in numbers:
            if type(number) != int: # This is to break the process and return an error if non integer input is received.
                return "No can do -- averages are only for nummy numbers!"
                break
            else:
                sum_all += number

        average = sum_all / float(number_of_numbers)

    return average


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    if words == []: # In case there is an empty string
        return "Please give me some input to nom nom nom on."

    else:
        joined_strings_w_comma = words[0]

        for word in words[1:]: # Starting at 1 so if there's only one word it doesn't come out with a comma and space.
            joined_strings_w_comma += ", " + word

        return joined_strings_w_comma


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    # SOLUTION 1:
    return items[::-1]

    # SOLUTION 2:
    # return [item for item in items[::-1]]

    # SOLUTION 3:
    # reversed_items = []
    # countdown = len(items)

    # for index in range(countdown):
    #     reversed_items.append(items[countdown-1])
    #     countdown -= 1

    # return reversed_items


def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """

    for item in items[len(items)-1::-1]:
        items.remove(item)
        items.append(item)

    return


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """

    duplicates_set = set([])

    for item in items:
        if items.count(item) > 1:
            duplicates_set.add(item)

    duplicates = list(sorted(duplicates_set))

    return duplicates


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    letter_indices = []

    for word in words:
        if "o" in word:
            counter = 0
            for char in word:
                if char == "o":
                    letter_indices.append(counter)
                    break
                else:
                    counter += 1
        else:
            letter_indices.append(None)

    return letter_indices


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
