def start_playing(instance):
    return instance.play()


class Guitar:
    @staticmethod
    def play():
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))


class Children:
    @staticmethod
    def play():
        return "Children are playing"


children = Children()
print(start_playing(children))
