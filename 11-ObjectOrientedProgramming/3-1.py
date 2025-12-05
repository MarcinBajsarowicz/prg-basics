# class definition
class Song:
   def __init__(self,performer,title,album,year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year
   def __str__(self):
        return f'Performer: {self.performer}\nTitle: {self.title}\nAlbum: {self.album}\nYear: {self.year}\n'

# object creation
song1 = Song("Ed Sheeran", "Shape of You", "Divide", 2017 )
song2 = Song("Queen", "Killer Queen", "Sheer Heart Attack", 1974)

## object usage
print(song1)
print(song2)