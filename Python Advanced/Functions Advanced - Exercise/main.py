def func_executor(*args):

    result = []

    for func_ref, func_arg in args:
        func_name = func_ref.__name__
        func_result = func_ref(*func_arg)
