def even_numbers(function):
    def wrapper(numbers):
        result = function(numbers)
        return [x for x in result if x % 2 == 0]
