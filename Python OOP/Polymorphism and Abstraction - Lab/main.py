def start_playing(instance):
    return instance.play()


class Guitar:
    @staticmethod
    def play():
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))
