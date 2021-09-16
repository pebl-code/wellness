# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a default web2py_mediafront controller
# -------------------------------------------------------------------------
import client
# TODO: kein Bild, dark mode, Volume, Stop mit/ohne Bookmark, Bookmark löschen, Play


# ---- example index page ----
def index():
    response.flash = T("Sweet home")

    return dict(message=T('Welcome to web2py!'))


def sounds():
    media_list = ["Sound1", "Sound2", "Sound3"]
    return dict(message=T('Welcome to web2py!'))


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
    media_list = ["Book1", "Book2", "Book3"]
    media_dict = dict(title='Kapitel', artist='Autor', album='Buchtitel')
    return dict(message=T('Welcome to web2py!'), mliste=media_list, mdict=media_dict)


def do_something():
    print('do_something')
    print(request.vars.get('medium'))
    redirect(URL('default', 'audiobooks'))


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



# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})


# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
