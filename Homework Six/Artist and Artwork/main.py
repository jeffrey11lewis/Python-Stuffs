#from artistFile import Artist
#from Artwork import Artwork
from Artwork import Artwork

from artist import Artist
from artistFile import Artist
if __name__ == "__main__":
    print('enter Artist Name:')
    userArtistName = input()
    print('enter birth year')
    userBirthYear = int(input())
    print('enter death year (if alive, just ):')
    userDeathYear = int(input())
    print('enter title')
    userTitle = input()
    print('enter year created:')
    userYearCreated = int(input())

    userArtist = Artist(userArtistName, userBirthYear, userDeathYear)
    newArtwork = Artwork(userTitle, userYearCreated, userArtist)

    newArtwork.printInfo()