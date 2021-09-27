import os
import json
from pathlib import Path

_DEFAULT_PATH = '/tmp/pyvlc_data'
_VLC_FILES = ['media_file', 'media_folder', 'player', 'playing']

_SELECTOR = {
    'showfile': ['playing.artist', 'playing.album',
                 'playing.playing', 'playing.length', 'playing.play_time',
                 'player.status', 'player.volume', 'player_mode',
                 'media_folder.bookmark.bookmark.last_file', 'media_folder.bookmark.bookmark.playtime',
                 'media_file.file_path'],
    'alias': ['media_file.tags.audio_offset', 'media_folder.bookmark.bookmark.playtime']
}


class VlcFileInterface(object):
    def __init__(self, file_name, path=_DEFAULT_PATH):
        self.file_path = os.path.join(path, file_name)

        self.data = dict(file_name=file_name)
        if os.path.isfile(self.file_path):
            self.read()
        else:
            self.data['error'] = 'file not found: ' + file_name

    def get(self):
        return self.data

    def read(self):
        try:
            with open(self.file_path, 'r') as r_file:
                self.data = json.load(r_file)
        except Exception as exc:
            self.data['error'] = str(exc)
        return self.get()


class VlCDataProvider(object):
    def __init__(self):
        self.data = dict()
        self.load_all()

    def load_all(self):
        for file_name in _VLC_FILES:
            self.data.update({file_name: VlcFileInterface(file_name + '.json').get()})

    def get_data(self, info):

        def getter(d, i):
            return d.get(i, {})

        ret = {}
        get_list = _SELECTOR.get(info, [])

        for item in get_list:
            dat = self.data
            for thing in item.split('.'):
                dat = getter(dat, thing)
            ret[thing] = dat
        return ret


if __name__ == '__main__':
    d = VlCDataProvider()

    data = d.get_data('alias')
    for item in data:
        print(item, data.get(item))

    print(d.data.get('media_folder').get('bookmark'))