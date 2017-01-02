try :
    import pyaudio
    import socket
    import threading
    import time
    import pydub
    import sys
    import os
except ImportError as e:
    print "unable to import modules"
    print e
    sys.exit(1)
    
#global variablles
CLIENT_LIST = []
CHUNK = (441 * 6 + 150)
AUDIO_FORMAT = ['mp3','flv','ogg','wav']
SERVER_ADDR = ('127.0.0.1',35000)
PLAY_SONG = 1
PLAYLIST = 1


def multiclientsHandler():

    global CLIENT_LIST
    while True:

        try:
            data, addr = SOCKET.recvfrom(1024)
            if data == "my secret key":
                print str(addr) + " connected"
                CLIENT_LIST.append(addr)
        except socket.error as e:
            CLIENT_LIST.remove(addr)

    
def int_to_string(integer):
    string = str(integer) + '\n'
    return string


def get_song_data(file_name,extension):
    song_file = pydub.AudioSegment.from_file(file_name,
                                             extension)
                                             #frame_rate=22000)       
    song_data = song_file.raw_data
    return song_data

def get_songslist(_dir_):
    list_songs = []
    list_files_dir = os.listdir(_dir_)

    for files in list_files_dir:
        temp = files.split('.')
        if temp[-1] == "mp3":
            list_songs.append([files,'mp3'])
        elif temp[-1] == 'flv':
            list_songs.append([files,'flv'])
        elif temp[-1] == 'ogg':
            list_songs.append([files,'ogg'])
        elif temp[-1] == 'wav':
            list_songs.append([files,'wav'])

    return list_songs

def print_songslist(list_songs):

    for i in range(len(list_songs)):
        print str(i+1) + ') ' + list_songs[i][0]

#def print_nd_get_playlist():
#    pass

def serverHandler():

    global PLAY_SONG
    
    while True:
        list_songs = get_songslist(os.getcwd())
        print_songslist(list_songs)

        print "\nSelect the songs in order u wanna play\n"
        selected_songs = raw_input()
        selected_songs = selected_songs.split(' ')

        song_data = []
        j = 0 #temp
        for i in selected_songs:
            song_data.append(get_song_data(list_songs[int(i)-1][0],
                                           list_songs[int(i)-1][1]))
            print len(song_data[j])
            j += 1

        playlist_thread = threading.Thread(target=playSong,
                                           args=(song_data,))
        playlist_thread.start()
        playlist_thread.join()

      

def playSong(song_data_):

    global PLAYLIST
    print "server sending song"
    for song_data in song_data_:
        
        i = 0
        frame = song_data[i*CHUNK:(i+1)*CHUNK]
        while True:
            while(frame and PLAY_SONG):
                for client_addr in CLIENT_LIST:
                    try:
                        SOCKET.sendto(frame,client_addr)
                    except IOError as e:
                        print e
                        
                i += 1
                frame = song_data[i*CHUNK:(i+1)*CHUNK]
                time.sleep(0.015)
            if(frame):
                pass
            else:
                break




try:
    SOCKET = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error as e:
    print "unable to create socket"
    print e
    sys.exit(1)

try:    
    SOCKET.bind(SERVER_ADDR)
except socket.error as e:
    print "unable to bind addr"
    print e
    sys.exit(1)
    
SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

multiclients_thread = threading.Thread(target=multiclientsHandler)
multiclients_thread.setDeamon = True
multiclients_thread.daemon = True

multiclients_thread.start()

serverHandler()


SOCKET.close()
