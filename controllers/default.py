# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a default web2py_mediafront controller
# -------------------------------------------------------------------------
import client
import data_helper
import vlc_file_if

# TODO: kein Bild, dark mode, Volume, Stop mit/ohne Bookmark, Bookmark löschen, Play

# _book_path= '/home/kellerk/Musik/Audiobook/'
# _song_path= '/home/kellerk/Musik/Song/'
# _sound_path = '/home/kellerk/Musik/Sound/'
_book_path = configuration.get('media.audiobooks')
_song_path = configuration.get('media.songs')
_sound_path = configuration.get('media.sounds')


# ---- example index page ----
def index():
    return dict(message=T('Welcome to web2py!'))


def sounds():
    selected_artist = ('Sound', _sound_path)
    if selected_artist[1]:
        media_list = data_helper.get_media_files(selected_artist[1])

    return dict(sliste=media_list, selected_artist=selected_artist)


def songs():
    selected_artist = request.vars.get('artist', '')
    selected_album = request.vars.get('album', '')
    media_list = []
    song_list = []
    if selected_artist:
        media_list = data_helper.subfolders(selected_artist[1])
    if selected_album:
        print('SA: ',selected_album)
        song_list = data_helper.get_media_files(selected_album)

    artist_list = data_helper.subfolders(_song_path)
    return dict(sliste=media_list, aliste=artist_list, bliste=song_list,
                selected_artist=selected_artist, selected_album=selected_album)


def audiobooks():
    selected_artist = request.vars.get('selected_artist', ('', ''))
    media_list = []
    if selected_artist[1]:
        media_list = data_helper.subfolders(selected_artist[1])
    # artist_list = string_list(12, 12)

    artist_list = data_helper.subfolders(_book_path)

    return dict(sliste=media_list, aliste=artist_list, selected_artist=selected_artist)


def play():
    if request.vars.get('error'):
        response.flash = T(str(request.vars.get('error')))

    vlcdata = vlc_file_if.VlCDataProvider()
    data = vlcdata.get_data('showfile')
    if data.get('file_path') and not data.get('album'):
        # print(data.get('file_path'))
        data['album'] = data['file_path'].rsplit('/', 1)[1]
    return dict(data=data)


def vlc_play():
    ret_value = client.sender('start_play')
    if ret_value.get('error'):
        print(ret_value.get('error'))
    else:
        redirect(URL('default', 'play', vars=request.vars))


def vlc_stop():
    client.sender('stop')
    redirect(URL('default', 'play', vars=request.vars))


def vlc_pause():
    client.sender('pause')
    redirect(URL('default', 'play', vars=request.vars))


def vlc_forward():
    client.sender('next_file')
    redirect(URL('default', 'play', vars=request.vars))


def vlc_delta_plus():
    client.sender('delta_volume', 10)
    redirect(URL('default', 'play', vars=request.vars))


def vlc_delta_minus():
    client.sender('delta_volume', -10)
    redirect(URL('default', 'play', vars=request.vars))


def do_something():
    redirect(URL('default', 'audiobooks'))


def do_play():
    if request.vars.get('type') == 'folder':
        ret = client.sender('set_folder', request.vars.get('album', ''))
    if request.vars.get('type') == 'file':
        ret = client.sender('set_file', request.vars.get('title', ''))
    if ret.get('error'):
        redirect(URL('default', 'play', vars=ret))
    redirect(URL('default', 'play'))


def change_artist():
    redirect(URL('default', 'sounds', vars=dict(artist=request.vars.get('artist'))))


def change_author():

    redirect(URL('default', request.vars.get('page'), vars=dict(artist=request.vars.get('artist'))))


def change_album():
    print('album= ', request.vars.get('album'))
    redirect(URL('default', 'songs', vars=request.vars))

