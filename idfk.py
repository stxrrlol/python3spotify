a = 0
if a == a:
    import os
    from os.path import exists
    import math
    import spotipy
    from spotipy import SpotifyOAuth
    from spotipy import util
    import random
    from os import listdir
    from os.path import isfile, join
    cd = os.getcwd()
    import spotipy
    import json
    def cc():
        os.system('clear || cls')
    def login():
        global sp
        os.environ["SPOTIPY_CLIENT_ID"] = "3699e4071c3246d0acac94350e047749"
        os.environ["SPOTIPY_CLIENT_SECRET"] = "5419afd473554878914d3af50fa39a47"
        os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1/callback/"
        scope = "user-library-read user-library-modify user-read-private user-read-email streaming app-remote-control playlist-modify-private playlist-read-private playlist-modify-public playlist-read-collaborative user-top-read user-read-playback-position user-read-recently-played user-follow-read user-follow-modify user-read-currently-playing user-read-playback-state user-modify-playback-state ugc-image-upload"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        np()
def np():
    global cd
    global dfd
    global sp
    cc()
    ovnm = input('How many songs would you like in this playlist?\n')
    if (os.path.exists(cd + '/mp.json')) == True:
        f = json.loads(open(cd + '/mp.json').read())
        npn = len(f)+1
    if (os.path.exists(cd + '/mp.json')) == False:
        npn = 1
    if (os.path.exists(cd + '/usn.json')) == True:
        usn = json.loads(open(cd + '/usn.json').read())['usn']
    if (os.path.exists(cd + '/usn.json')) == False:
        usn = sp.current_user()['id']
        f = open(cd + '/usn.json', 'w+')
        f.write(json.dumps({'usn': usn}, indent='   '))
        f.close()
    cc()
    direc = input('Would you like to select a custom name for the playlist?\n1. Yes\n2. No\n')
    if direc == '1':
        cc()
        plnm = input('What would you like to name the playlist?\n')
    if direc == '2':
        plnm = 'Programmed Mix #' + str(npn)
    cc()
    pbtnf = input('Would you like the playlist to be public?\n1. Yes\n2. No\n')
    if pbtnf == '1':
        pbtnfv = True
    if pbtnf == '2':
        pbtnfv = False
    asngsid = []
    asngsnm = []
    pls = sp.current_user_playlists()['items']
    a = 0
    cc()
    while a < len(pls):
        p = sp.playlist(pls[a]['id'])['tracks']['items']
        b = 0
        while b < len(p):
            if p[b]['track'] != None:
                asngsid.append(p[b]['track']['id'])
                asngsnm.append(p[b]['track']['name'] + ' - ' + p[b]['track']['artists'][0]['name'])
            b = b + 1
        a = a + 1
    a = 0
    while a < 10000:
        ulb = sp.current_user_saved_tracks(limit=50, offset=50*a)['items']
        if len(ulb) < 50:
            b = 0
            while b < len(ulb):
                if ulb[b]['track'] != None:
                    if ulb[b]['track']['name'] + ' - ' + ulb[b]['track']['artists'][0]['name'] not in asngsnm:
                        asngsnm.append(ulb[b]['track']['name'] + ' - ' + ulb[b]['track']['artists'][0]['name'])
                    if ulb[b]['track']['id'] not in asngsid:
                        asngsid.append(ulb[b]['track']['id'])
                b = b + 1
            break
        if len(ulb) >= 50:
            b = 0
            while b < len(ulb):
                if ulb[b]['track'] != None:
                    if ulb[b]['track']['name'] + ' - ' + ulb[b]['track']['artists'][0]['name'] not in asngsnm:
                        asngsnm.append(ulb[b]['track']['name'] + ' - ' + ulb[b]['track']['artists'][0]['name'])
                    if ulb[b]['track']['id'] not in asngsid:
                        asngsid.append(ulb[b]['track']['id'])
                b = b + 1
        a = a + 1
    atlst = []
    atdct = {}
    sglst = []
    a = 0
    tt = sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')['items']
    while a < len(tt):
        tr = tt[a]
        if a in [0, 1, 2, 3, 4]:
            sglst.append(tr['id'])
        ats = tr['artists']
        b = 0
        while b < len(ats):
            if ats[b]['id'] in atlst:
                atdct[ats[b]['id']].append(1)
            if ats[b]['id'] not in atlst:
                atlst.append(ats[b]['id'])
                atdct[ats[b]['id']] = [1]
            b = b + 1
        a = a + 1
    a = 0
    natlst = []
    natdct = {}
    while a < len(atlst):
        at = atlst[a]
        atn = sum(atdct[at])
        if atn in natlst:
            natdct[atn].append(at)
        if atn not in natlst:
            natlst.append(atn)
            natdct[atn] = [at]
        a = a + 1
    natlst.sort(reverse=True)
    a = 0
    nnatlst = []
    while a < len(natlst):
        nat = natlst[a]
        natd = natdct[nat]
        cl = len(nnatlst)
        if (cl + len(natd)) >= 5:
            b = 0
            while b < len(natd):
                nnatlst.append(natd[b])
                b = b + 1
            break
        if (cl + len(natd)) < 5:
            b = 0
            while b < len(natd):
                nnatlst.append(natd[b])
                b = b + 1
        a = a + 1
    atlst = nnatlst[0:5]
    gnlst = []
    gndct = {}
    a = 0
    while a < len(tt):
        tr = tt[a]
        ats = tr['artists']
        b = 0
        while b < len(ats):
            gns = sp.artist(ats[b]['id'])['genres']
            c = 0
            while c < len(gns):
                if gns[c] in gnlst:
                    gndct[gns[c]].append(1)
                if gns[c] not in gnlst:
                    gnlst.append(gns[c])
                    gndct[gns[c]] = [1]
                c = c + 1
            b = b + 1
        a = a + 1
    a = 0
    ngnlst = []
    ngndct = {}
    while a < len(gnlst):
        at = gnlst[a]
        atn = sum(gndct[at])
        if atn in ngnlst:
            ngndct[atn].append(at)
        if atn not in ngnlst:
            ngnlst.append(atn)
            ngndct[atn] = [at]
        a = a + 1
    ngnlst.sort(reverse=True)
    a = 0
    nngnlst = []
    while a < len(ngnlst):
        nat = ngnlst[a]
        natd = ngndct[nat]
        cl = len(nngnlst)
        if (cl + len(natd)) >= 5:
            b = 0
            while b < len(natd):
                nngnlst.append(natd[b])
                b = b + 1
            break
        if (cl + len(natd)) < 5:
            b = 0
            while b < len(natd):
                nngnlst.append(natd[b])
                b = b + 1
        a = a + 1
    gnlst = nngnlst[0:5]
    gnlst2 = []
    a = 0
    while a < len(gnlst):
        if ' ' in gnlst[a]:
            gnlst2.append(gnlst[a].replace(' ', '-'))
        if gnlst[a] == 'r&b':
            gnlst2.append('r-n-b')
        if (' ' not in gnlst[a]) and (gnlst[a] != 'r&b'):
            gnlst2.append(gnlst[a])
        a = a + 1
    gnlst = gnlst2
    sglst = sglst[0:1]
    atlst = atlst[2:4]
    gnlst = gnlst[3:]
    ovp = []
    ovpnm = []
    a = 0
    while a < 1000000:
        if len(ovp) >= int(ovnm):
            break
        trs = sp.recommendations(seed_artists=atlst, seed_genres=gnlst, seed_tracks=sglst, limit=100, country='US', offset=100*a)['tracks']
        b = 0
        while b < len(trs):
            if len(ovp) >= int(ovnm):
                break
            tr = trs[b]
            if (tr['id'] not in asngsid) and (tr['name'] + ' - ' + tr['artists'][0]['name'] not in asngsnm):
                if tr['id'] not in ovp:
                    if tr['name'] + ' - ' + tr['artists'][0]['name'] not in ovpnm:
                        ovp.append(tr['id'])
                        ovpnm.append(tr['name'] + ' - ' + tr['artists'][0]['name'])
            b = b + 1
        a = a + 1
    nsp = sp.user_playlist_create(user=usn, name=plnm, public=pbtnfv)
    npid = nsp['id']
    a = 0
    while a < 10000000:
        clovp = len(ovp)
        if clovp <= 100:
            sp.user_playlist_add_tracks(user=usn, playlist_id=npid, tracks=ovp)
            break
        if clovp > 100:
            sp.user_playlist_add_tracks(user=usn, playlist_id=npid, tracks=ovp[0:100])
            del ovp[0:100]
        a = a + 1
    sp.user_playlist_add_tracks(user=usn, playlist_id=npid, tracks=ovp)
    if (os.path.exists(cd + '/mp.json')) == True:
        f = json.loads(open(cd + '/mp.json').read())
        f[npid] = plnm
        s = open(cd + '/mp.json', 'w+')
        s.truncate(0)
        s.write(json.dumps(f, inednt='    '))
    if (os.path.exists(cd + '/mp.json')) == False:
        f = open(cd + '/mp.json', 'w+')
        f.write(json.dumps({npid: plnm}, indent='    '))
        f.close()
login()
