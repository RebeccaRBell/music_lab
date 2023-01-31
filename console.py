import pdb
from models.album import Album
import repositories.album_repository as album_repository
from models.artist import Artist
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Lady Gaga")
results = artist_repository.save(artist_1)
artist_2 = Artist("Adele")
results = artist_repository.save(artist_2)

album_1 = Album("Artpop", "pop", artist_1)
results = album_repository.save(album_1)


pdb.set_trace()
