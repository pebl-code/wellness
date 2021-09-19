import json
import os

_media_extensions = ['.mp3', '.flac', '.wma', '.webm', '.m4a']


def subfolders(path):
    return sorted([(f.name, f.path) for f in os.scandir(path) if f.is_dir() and f.name[0] != '.'])


def subfolderdict(path):
    return [{'name': f[0], 'path': f[1]} for f in subfolders(path)]


def get_media_files(path):
    # return sorted([file for file in os.listdir(path)
    #                if os.path.splitext(file)[1].lower() in _media_extensions])
    return sorted([(f.name, f.path) for f in os.scandir(path)
                   if f.is_file() and f.name[0] != '.' and os.path.splitext(f.name)[1].lower() in _media_extensions])
    #return sorted([(f.name, f.path) for f in os.scandir(path)
    #               if f.is_file()])


def write_json_file(self, data, path, filename):
    try:
        wdata = json.dumps(data)
    except Exception as exc:
        return 'error'
    with open(os.path.join(path, filename), 'w') as w_file:
        w_file.write(wdata)
    return None


def read_json_file(path, filename):
    try:
        with open(os.path.join(path, filename), 'r') as bm_file:
            data = json.load(bm_file)
    except FileNotFoundError:
        data = dict(error='file not found')
    return data


def time_string(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h == 0:
        return f'{m:02d}:{s:02d}'
    return f'{h:02d}:{m:02d}:{s:02d}'


def time_string_ms(millis):
    return time_string(int(round((millis/1000))))

if __name__ == '__main__':
    # d = read('/tmp/pyvlc_data', 'player.json')
    # print(type(d))
    # for item in d:
    #     print(item, d.get(item))
    # d.get('data_path')
    song_list = get_media_files("/home/kellerk/Musik/Song/Nier/Album1")
    print(song_list)
