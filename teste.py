import re

r = 'spotify:album:1DFixLWuPkv3KT3TnV35m3'
s = 'https://open.spotify.com/album/4RuzGKLG99XctuBMBkFFOC'
t = 'spotify:track:1VxYLGqZJCxIQyEQFJJnPe'
z = 'spotify:playlist:7op06LFKBa3VXfGSbopbEU'

# https://open.spotify.com/embed/album/4RuzGKLG99XctuBMBkFFOC
# (For example, spotify:album:1DFixLWuPkv3KT3TnV35m3 or https://open.spotify.com/album/4RuzGKLG99XctuBMBkFFOC.)
#standard = 'https://open.spotify.com/embed/'


class Spotify:
    def __init__(self, address):
        self.address = address

        if 'album:' in self.address:
            self.segment = 'album'
            self.link = re.search(r'(?<=album:)\w+', self.address)
        elif 'album/' in self.address:
            self.segment = 'album'
            self.link = re.search(r'(?<=album/)\w+', self.address)
        elif 'track:' in self.address:
            self.segment = 'track'
            self.link = re.search(r'(?<=track:)\w+', self.address)
        elif 'track/' in self.address:
            self.segment = 'track'
            self.link = re.search(r'(?<=track/)\w+', self.address)
        elif 'playlist:' in self.address:
            self.segment = 'playlist'
            self.link = re.search(r'(?<=playlist:)\w+', self.address)
        elif 'playlist/' in self.address:
            self.segment = 'playlist'
            self.link = re.search(r'(?<=playlist/)\w+', self.address)

    def __str__(self):
        return f'https://open.spotify.com/embed/{self.segment}/{self.link.group(0)}'


print(Spotify(r))
print(Spotify(s))
print(Spotify(t))
print(Spotify(z))


#m = re.search(r'(?<=album)\w+', 'https://open.spotify.com/album/4RuzGKLG99XctuBMBkFFOC')
#print(m.group(0))