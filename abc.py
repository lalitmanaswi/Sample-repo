import sys

print(sys.version)
print(sys.executable)


def who_to_greet(greet):
    greeting = "Hello, {}".format(greet)
    return greeting


print(who_to_greet("World"))
print(who_to_greet("Lalit"))

