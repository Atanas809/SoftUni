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
