class JokeObject:

    def __init__(self, setup = "En hund går ind på en bar og siger...", punchline = 'Jeg kan ikke se noget'):
        self.setup = setup
        self.punchline = punchline

    def print_joke(self):
        print(self.setup)
        print(self.punchline)