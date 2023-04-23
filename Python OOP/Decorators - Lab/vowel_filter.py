def vowel_filter(function):
    def wrapper():
        all_vowels = ["a", "o", "u", "y", "e", "i"]
        result = function()
        return [x for x in result if x in all_vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
