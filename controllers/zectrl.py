def index():
    return dict(message=T('Welcome to web2py!'))


import random
import string
import data_helper


def random_string_generator(str_size=10, allowed_chars=string.ascii_letters):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


def string_list(size, length=24):
    l = []
    for i in range(size):
        d = random_string_generator(str_size=length)
        l.append((d, d))
    return l


def audiobook():
    selected_artist = request.vars.get('selected_artist', ('', ''))
    artist_list = list(data_helper.subfolders('/home/peterl/Comco/'))
    media_list = []

    if artist_list:
        if selected_artist == ('', ''):
            selected_artist = artist_list[0]
        media_list = data_helper.subfolders(selected_artist[1], get_count=False)

    return dict(media_list=media_list, artist_list=artist_list, selected_artist=selected_artist, sub_name1='Books')


def sound():
    selected_artist = request.vars.get('selected_artist', ('', ''))
    artist_list = list(data_helper.subfolders('/home/peterl/Oldes/Musik/bosshoss', sub_sel='files'))
    media_list = []
    if artist_list:
        if selected_artist == ('', ''):
            selected_artist = artist_list[0]
        media_list = data_helper.get_media_files(selected_artist[1])

    return dict(media_list=media_list, artist_list=artist_list, selected_artist=selected_artist, sub_name1='Files')


def song():
    selected_artist = request.vars.get('selected_artist', ('', ''))
    artist_list = list(data_helper.subfolders('/home/peterl/Comco/'))
    media_list = []
    if artist_list:
        if selected_artist == ('', ''):
            selected_artist = artist_list[0]
        media_list = data_helper.subfolders(selected_artist[1], get_count=False)

    return dict(media_list=media_list, artist_list=artist_list, selected_artist=selected_artist, sub_name1='Albums')
