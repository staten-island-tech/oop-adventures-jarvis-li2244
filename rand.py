x = input("Number: ")

def palindrome(x):
    y = []
    for i in x:
        y.insert(0, i)
    z = "".join(y)
    if z == x:
        return True
    return False

print(palindrome(x))