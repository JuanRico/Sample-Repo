import sys

print("Version: ", sys.version)
print("Executable: ", sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


name = input("your name? ")
print(greet("World"))
print("Hello,", name)