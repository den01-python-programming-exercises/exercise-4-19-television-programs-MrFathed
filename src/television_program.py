class TelevisionProgram:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def is_awesome(self):
        return "master_chef" in self.name

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def __str__(self):
        return self.name + ", " + str(self.duration) + " minutes"
