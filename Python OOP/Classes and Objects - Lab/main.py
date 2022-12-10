class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = True if not self.is_on else False

    def install(self, app, app_memory):
        if app_memory > self.memory:
            return f"Not enough memory to install {app}"
        elif not self.is_on:
            return f"Turn on your phone to install {app}"
