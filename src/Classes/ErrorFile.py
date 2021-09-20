class File:

    UTF8 = 'utf-8'

    def __init__(self, name):
        self.name = name
        with open(self.name, 'a', encoding=self.UTF8) as f:
            pass

    def append_error(self, message):
        print(message)
        with open(self.name, 'a', encoding=self.UTF8) as f:
            f.write(message)

    def read(self):
        with open(self.name, "r", encoding=self.UTF8) as f:
            return f.read()

    def clean(self):
        with open(self.name, "r+", encoding=self.UTF8) as f:
            f.truncate(0)
