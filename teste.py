
from spotify import SpotifyLink, SpotifyImage
#Client ID 458d767d30034a44828d668093119d4f
#Client Secret 94362b7769f64dd298ae57852647527b
r = 'spotify:album:1DFixLWuPkv3KT3TnV35m3'
s = 'https://open.spotify.com/embed/track/3tqv7xESjYRUjnBoJvfLhN'
t = 'spotify:track:1VxYLGqZJCxIQyEQFJJnPe'
z = 'spotify:playlist:7op06LFKBa3VXfGSbopbEU'

print('s')
print(SpotifyLink(s))
print(SpotifyImage(s))
print()

