# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a default web2py_mediafront controller
# -------------------------------------------------------------------------
import client
import data_helper
import vlc_file_if

# TODO: Auswertung Rückgabewert sender(), Start bei Aufruf play, Bookmark löschen/Play ohne Bookmark, Fehlerbehandlung

# ---- example index page ----
def index():
    return dict(message=T('Welcome to web2py!'))


def audiobook():
    selected_artist = request.vars.get('selected_artist', ('', ''))
    artist_list = list(data_helper.subfolders(configuration.get('media.audiobooks')))
    media_list = []
    if artist_list:
        if selected_artist == ('', ''):
            selected_artist = artist_list[0]
        media_list = data_helper.subfolders(selected_artist[1], get_count=False)
    return dict(media_list=media_list, artist_list=artist_list, selected_artist=selected_artist, sub_name1='Books')


def sound():
    selected_artist = request.vars.get('selected_artist', ('', ''))
    artist_list = list(data_helper.subfolders(configuration.get('media.sounds'), sub_sel='files'))
    media_list = []
    if artist_list:
        if selected_artist == ('', ''):
            selected_artist = artist_list[0]
        media_list = data_helper.get_media_files(selected_artist[1])
    return dict(media_list=media_list, artist_list=artist_list, selected_artist=selected_artist, sub_name1='Files')


def song():
    selected_artist = request.vars.get('selected_artist', ('', ''))
    artist_list = list(data_helper.subfolders(configuration.get('media.songs')))
    media_list = []
    if artist_list:
        if selected_artist == ('', ''):
            selected_artist = artist_list[0]
        media_list = data_helper.subfolders(selected_artist[1], get_count=False)
    return dict(media_list=media_list, artist_list=artist_list, selected_artist=selected_artist, sub_name1='Albums')


def play():
    if request.vars.get('error'):
        response.flash = T(str(request.vars.get('error')))

    vlcdata = vlc_file_if.VlCDataProvider()
    data = vlcdata.get_data('showfile')
    print(data['file_path'])
    if data.get('file_path') and not data.get('album'):
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

