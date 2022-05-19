class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        album = [a for a in self.albums if a.name == album_name]
        if not album:
            return f"Album {album_name} is not found."
        if album[0].published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(album[0])
        return f"Album {album_name} has been removed."

    def details(self):
        data = ""
        data += f"Band {self.name}\n"
        data += ''.join([f"{a.details()}" for a in self.albums])
        return data
