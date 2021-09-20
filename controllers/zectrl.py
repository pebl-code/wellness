def index():
    return dict(message=T('Welcome to web2py!'))


import random
import string
import data_helper


def random_string_generator(str_size=10, allowed_chars=string.ascii_letters):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

# TODO :filenot found error!!!

def string_list(size, length=24):
    l = []
    for i in range(size):
        d = random_string_generator(str_size=length)
        l.append((d, d))
    return l


def audiobooks():
    selected_artist = request.vars.get('selected_artist', ('', ''))
    media_list = []
    print(selected_artist)
    print(request.vars)
    if selected_artist[1]:
        print("neue Buchliste von %s", selected_artist)
        # media_list = string_list(39, 39)
        media_list = data_helper.subfolders(selected_artist[1])
    # artist_list = string_list(12, 12)
    artist_list = data_helper.subfolders('/home/kellerk/Musik/Audiobook/')

    return dict(sliste=media_list, aliste=artist_list, selected_artist=selected_artist)


