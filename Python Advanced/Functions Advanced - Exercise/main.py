def grocery_store(**kwargs):
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
