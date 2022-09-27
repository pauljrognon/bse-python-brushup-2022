#
# 1)
# Write a function "only_adults" that
# takes as input a list of numbers and
# returns only those numbers >= 18
def only_adults(ages):
    return [age for age in ages if age >= 18]
#
# 2)
# Write a function "get_only_adults" that
# takes as input a list of numbers and
# returns only those numbers >= 18
# and removes any None values from the list
def get_only_adults(ages):
    return [age for age in ages if age and (age >= 18)]
#
# 3)
# Write a function "are_all_adults" that
# takes as input a list of numbers
# and returns True if they are all >= 18,
# and returns False otherwise
# Is this a map, filter, or reduce? Answer: it is reduce because it reduces a collection of elements to a one element/number.
def are_all_adults(ages):
    for i in range(len(ages)):
        if ages[i] < 18:
            return False
    return True
#
# 4)
# Write a function "count_nones" that
# takes as input a list of any type of element
# and returns a count of how many of those
# elements are None types.
# Is this a map, filter, or reduce? Answer: this is also reduce.
def count_nones(li):
    return sum([1 if x is None else 0 for x in li])
#
# 5)
# Write a function "longest_word" that
# takes as input a list of strings
# and returns the longest string in the
# list.
# Hint: you will need to use two "accumulators"
def longest_word(li):
    word_lengths = [len(word) for word in li]
    longest_ind = 0
    for i in range(len(li)):
        if word_lengths[i] > word_lengths[longest_ind]:
            longest_ind = i
    return li[longest_ind]
#
# 5)
# Write a function "factorial"
#
# It takes a number and returns the
# factorial of that number.
#
# The factorial of n is the product of all
# positive integers less than or equal to n
#
# HINT: use range()
# https://docs.python.org/3/library/stdtypes.html#typesseq-range
#
# range(n) produces an iterable of length n:
# [0,1,2,...,n-1]
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('Factorial is defined only for non-negative integers.')
    cumulative_product = 1
    for x in range(n):
        cumulative_product *= x + 1
    return cumulative_product

# alternative with recursions
# def factorial(n):
#     if not isinstance(n, int) or n < 0:
#         raise ValueError('Factorial is defined only for non-negative integers.')
#     if n == 0: return 1
#     elif n == 1: return 1
#     else: return n * factorial(n - 1)
#
# 6)
# Write a function "second_highest_number"
# that takes as input a list of numbers
# and returns the second highest. Assume
# that the numbers will be unique (no duplicates).
#
# NOTE: Only use the operations and functions
# we have learned so far! No cheating!
#
# HINT: You might want to write two functions!
def max_value(nums):
    pointer = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > pointer:
            pointer = nums[i]
    return pointer

def second_highest_number(nums):
    return max_value([num for num in nums if num < max_value(nums)])

#####################################################
# BONUS EXERCISES
# Uncomment the commented-out tests in test_exercises.py
# to unlock the bonus exercises.
#####################################################



#
# 7)
# Write a function "n_highest_number"
# with two parameters:
# 1. a list of numbers
# 2. an integer
#
# "n_highest_number" should return the nth
# highest number in the list, where n is the
# second parameter of the function. Assume
# that the numbers will be unique (no duplicates).
# Also assume that n <= the number of elements
# in the list.
#
# NOTE: Only use the operations and functions
# we have learned so far! No cheating!
#
# HINT: Can you reuse anything from the previous
# exercise? That may or may not work, depending
# on how you implemented it.
#
# HINT HINT: use the function "range"!
def n_highest_number(nums, n):
    while n > 1:
        nums = [num for num in nums if num < max_value(nums)]
        n -= 1
    return max_value(nums)
#
# 8)
# Write a function "every" that
# takes two parameters:
# 1. a list of elements of data type E
# 2. a predicate function (E) -> bool. In
# other words, a function that has a single
# parameter, which is the same type as the
# elements of the list, and returns a boolean.
#
# "every" should return True if the predicate
# evaluates to true for every element in the list.
# Otherwise, it returns False.
#
# NOTE: we haven't yet seen functions
# passed as arguments, so this might
# feel strange. But it works!
def every(li, predicate):
    predicates = [predicate(elem) for elem in li]
    for pred in predicates:
        if not pred:
            return False
    return True