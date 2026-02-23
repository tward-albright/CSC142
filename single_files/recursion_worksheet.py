# Returns the sum of a list
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])


# Count the occurences of an item in a list
def count_occurences(lst, target):
    if len(lst) == 0:
        return 0
    if lst[0] == target:
        return 1 + count_occurences(lst[1:], target)
    return count_occurences(lst[1:], target)


# reverse a string
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


# sum the digits of an integer
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


print(sum_digits(4721))
