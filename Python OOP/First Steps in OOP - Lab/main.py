# Current output:
"""
global
outer: local
inner: nonlocal
outer: local
global
"""

x = "global"


def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)

# Expected output:
"""
global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!
"""

x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"
