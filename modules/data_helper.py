import json
import os

_media_extensions = ['.mp3', '.flac', '.wma', '.webm', '.m4a']


def subfolderlist(path):
    """ get subfolders as a list instad of tuples """
    if os.path.isdir(path):
        return sorted([[f.name, f.path] for f in os.scandir(path) if f.is_dir() and f.name[0] != '.'])
    return[]


def subfolders(path, get_count=True, sub_sel='folder'):
    """ return sorted tupels of subfolders """
    if os.path.isdir(path):
        if get_count:
            if sub_sel == 'folder':
                data = sorted([(f.name, f.path, len(subfolderlist(f.path))) for f in os.scandir(path) if f.is_dir() and f.name[0] != '.'])
            else:
                data = sorted([(f.name, f.path, len(get_media_files(f.path))) for f in os.scandir(path) if f.is_dir() and f.name[0] != '.'])
            data = filter(lambda item: item[2] > 0, data)
            return data
        return sorted([(f.name, f.path) for f in os.scandir(path) if f.is_dir() and f.name[0] != '.'])
    return[]


def subfolderdict(path, get_count=True, sub_sel='folder'):
    """ return dicts instead of tuples"""
    if os.path.isdir(path):
        data = [{'name': f[0], 'path': f[1]} for f in subfolders(path)]
        if get_count:
            for item in data:
                if sub_sel == 'folder':
                    item['subs'] = len(subfolders(item['path']))
                else:
                    item['subs'] = len(get_media_files(item['path']))
                data = filter(lambda item: item['subs'] > 0, data)
            return data
    return []


def get_media_files(path):
    """ get a list of mediafiles in a folder"""
    if os.path.isdir(path):
        return sorted([(f.name, f.path) for f in os.scandir(path)
                       if f.is_file() and f.name[0] != '.' and os.path.splitext(f.name)[1].lower() in _media_extensions])
    return []


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
    try:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        if h == 0:
            return f'{m:02d}:{s:02d}'
        return f'{h:02d}:{m:02d}:{s:02d}'
    except Exception as exc:
        print('time_string: ', str(exc))
        print('data', str(seconds), type(seconds))
        return ''


def time_string_ms(millis):
    try:
        return time_string(int(round((millis/1000))))
    except Exception as exc:
        print('time_string_ms: ', str(exc))
        print('data', str(millis), type(millis))
        return ''



if __name__ == '__main__':
    # d = read('/tmp/pyvlc_data', 'player.json')
    # print(type(d))
    # for item in d:
    #     print(item, d.get(item))
    # d.get('data_path')
    #song_list = get_media_files("/home/kellerk/Musik/Song/Nier/Album1")
    #print(song_list)
    res = (subfolders('/home/peterl/Comco'))
    for item in res:
        print(item)

