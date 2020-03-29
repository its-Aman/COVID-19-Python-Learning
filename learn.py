x = 5
y = "Aman"

# print(x, type(x))
# print(y, type(y))

x = True
# print(x, type(x))

y = [1, "1", True]
# print(y, type(y))

a, b, c = 1, "1", False

# print(a, b, c)


def myfunc():
    global x
    x = "False"
    # print("Python is " + x)


myfunc()


def print_types():
    data_types = ['string was always my favorite data type', 1, 1.1, 1-2j, [1, 2], (False, True, True), range(5), {"name": "Aman"}, {
        "set1", "SET2", "Set#"}, frozenset({1, 2, 3}), True, b"Aman", bytearray(101), memoryview(bytes(4))]
    for d_t in data_types:
        print(d_t, type(d_t))
    print("was" in data_types[0])


print_types()


f = """
adfasdfasdf


"""

print("------------------------------------------")
print(f)


quantity = 3
itemno = 567
price = 49.95

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# myorder.

#   Arithmetic operators:  +,-,*,/,%,**,//
#   Assignment operators: =, +=,-+,*+,/=,%=, //=, **=, |=, ^=, >>=, <<=
#   Comparison operators: ==, !=, <, >, <=, >=
#   Logical operators: and, or, not
#   Identity operators: is, is not
#   Membership operators: in, not in
#   Bitwise operators: &, |, ^, ~, <<, >>


# Python Collections (Arrays)

# List,
# Tuple, 
# Set, 
# Dictionary

def t_r(k):
    if k>0:
        result=k+t_r(k-1)
        print(result)
    else:
        result=0
    return result

t_r(10)
