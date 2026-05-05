a = [1, 2]

#a = "Hello "

# try:
#     print(b)
#     print(a[2])
# except IndexError:
#     print("Out of bounds exception!")
# except NameError:
#     print("Invalid Name")

b = "Python"
try:
    c = a + b
except TypeError:
    print(b)
else:
    print(c)
finally:
    print("Life goes on!")