# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a default web2py_mediafront controller
# -------------------------------------------------------------------------
import client
# TODO: kein Bild, dark mode, Volume, Stop mit/ohne Bookmark, Bookmark löschen, Play


# ---- example index page ----
def index():
    return dict(message=T('Welcome to web2py!'))


def sounds():
    selected_artist = request.vars.get('artist', '')
    if selected_artist:
        print("neue Buchliste von %s", selected_artist)

    artist_list = ["Arist 1", "Artist 2", "Artist 3"]
    media_list = ["Book1", "Book2", "Book3", "Book4", "Book5"]
    return dict(sliste=media_list, aliste=artist_list, selected_artist=selected_artist)


def myvlc():
    mylist = request.vars.get('file_list', [])
    if request.vars:
        print(request.vars)
        response.flash = str(request.vars)
    else:
        response.flash = T("VLC")
    # mylist=["Song 1", "Song 2"]
    form = SQLFORM.factory(Field('song', requires=IS_IN_SET(mylist, zero='- choose -')),
                           submit_button='Play')
    media_dict = dict(title='Albumtitel', artist='Autor', album='Buchtitel',  cover='Cover.jpg', form=form)

    if form.process().accepted:
        response.flash = 'play: '+str(form.vars.song)
        # print(form.vars)
        # redirect(URL('myvlc'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'

    return media_dict


def songs():
    media_list = ["Song1", "Song2", "Song3"]
    return dict(message=T('Welcome to web2py!'))


def audiobooks():
    artist_list = ["Arist 1", "Artist 2", "Artist 3"]
    media_list = ["Book1", "Book2", "Book3", "Book4", "Book5"]
    return dict(message=T('Welcome to web2py!'), sliste=media_list, aliste=artist_list)


def play():
    media_dict = dict(title=request.vars.get('title', ''),
                      artist=request.vars.get('artist', ''),
                      album=request.vars.get('album', ''))
    return dict(message=T('Welcome to web2py!'), mdict=media_dict)


def do_something():
    print('do_something')
    print(request.vars.get('medium'))
    redirect(URL('default', 'audiobooks'))


def do_play():
    print('do_something')
    print(request.vars.get('medium'))
    redirect(URL('default', 'play', vars=dict(artist=request.vars.get('artist'), album=request.vars.get('album'))))


def change_artist():
    print('change_artist')
    print(request.vars.get('artist'))
    redirect(URL('default', 'sounds', vars=dict(artist=request.vars.get('artist'))))



def vlc_client():
    print('CMD:', request.vars.get('cmd'))
    # print('PATH:', request.vars.get('arg'))
    # print('vlc_client')
    # vlc = client.make_vlc('set_path', '/home/peterl/Oldes/Musik/bosshoss/liberty/')
    vlc = client.make_vlc(request.vars.get('cmd'), request.vars.get('arg', None))
    print(vlc)
    data = client.sender(vlc)
    redirect(URL('default', 'myvlc.html',
                 vars=data))
    # URL('a', 'c', 'f', args=['x', 'y'], vars=dict(z='t'))

