from models.genres_model import genres
from thirdparty.spotify import SpotifyGetOneArtist
genre = ''
spotifyArtistGenres = SpotifyGetOneArtist('28hJdGN1Awf7u3ifk2lVkg').createList().get('genres')

if spotifyArtistGenres:
    for genreName, value in genres.items():
        for i in spotifyArtistGenres:
            if i in value:
                genre = genreName
            break
print(genre)

# pop - 3MHaV05u0io8fQbZ2XPtlC
# testament - 28hJdGN1Awf7u3ifk2lVkg
# metallica -