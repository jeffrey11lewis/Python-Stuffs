
from Artist import Artist


class Artwork:
    def __init__(self, title = 'None', yearCreated = 0, artist = Artist()):
        self.title = title
        self.yearCreated = yearCreated
        self.artist = artist

    def printInfo(self):
        self.artist.printInfo()
        print('Title: %s, %d' % (self.title, self.yearCreated))