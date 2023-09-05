from config import CONN, CURSOR

class Song:

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)  # Create a new Song instance
        song.save()  # Save the new instance to the database
        return song  # Return the created instance

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
# Example usage:
new_song = Song.create("New Song", "New Album")
print(new_song.name)  # Should print "New Song"
print(new_song.album)  # Should print "New Album"
