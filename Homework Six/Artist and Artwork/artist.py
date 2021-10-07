class Artist:
    def __init__(self, name = 'None', birthYear = 0, deathYear = 0):
        selfName = name
        self.BirthYear = birthYear
        self.deathYear = deathYear
    def printInfo(self):
        if self.deathYear == -1:
            print('Artist: {}, born {}'.format(self.name, self.BirthYear))
        else:
            print('Artist: {} ({}-{})'.format(self.name, self.BirthYear, self.deathYear))