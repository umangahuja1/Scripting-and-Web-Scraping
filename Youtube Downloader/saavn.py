#download saavn songs and video songs 

from subprocess import call
from bs4 import BeautifulSoup
import requests
from colorclass import Color


def songs_info(res):

    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.find('ol', {'class': 'content-list'})
    return data


def song_print(data, limit='20'):
    song_list = []

    for i, count in zip(data.find_all('div', {'class': 'details'}), range(1, int(limit) + 1)):
        song = i.find('p', {'class': 'song-name'}).text
        album = i.find('p', {'class': 'album-name'}).text

        print("{:>2}.".format(count), end='')
        count += 1
        print(song, end='')
        if song != album:
            print(" (" + album + ")")
        else:
            print()
        item = song
        if album != song:
            item = item + " (" + album + ")"
        song_list.append(item)

    return song_list



def download_menu():
    print('1.Song')
    print('2.Video Song')
    print()
    choice = input('Enter your choice:')
    print()
    while choice not in ['1', '2']:
        print(Color('{autored}Wrong Choice{/autored}'))
        choice = input('\nEnter choice: ')
        print()
    return choice


def subtitles():
    subtitles_list = ['hi', 'en']
    lang = input('Enter subtitles language ( hindi -> hi , english -> en ): ')
    while lang not in subtitles_list:
        print('\n Wrong choice:')
        lang = input('Enter subtitles language ( hindi -> hi , english -> en ): ')
    return ["--write-sub", "--sub-lang", lang]


def song_download_by_name(name, sub, sub_data, url=''):
    extras = ["--embed-thumbnail"]
    search = ["ytsearch:" + name]

    if url != '':
        search = [url]

    if sub == 'y' or sub == 'Y':
        extras.extend(sub_data)

    print("\nDownloading {}\n".format(name))

    command = ['youtube-dl', '-o', '/home/umang/Music/%(title)s.%(ext)s+']
    audio_format = "-x --audio-format mp3".split()
    search.extend(audio_format)
    command.extend(search)
    command.extend(extras)
    call(command, shell=False)


def video_song_download_by_name(name, sub, sub_data, url=''):
    extras = ['--embed-subs']
    search = ["ytsearch:" + name]

    if url != '':
        search = [url]

    if sub == 'y' or sub == 'Y':
        extras.extend(sub_data)

    print("\nDownloading {}\n".format(name))

    command = ['youtube-dl', '-o', '/home/umang/Videos/%(title)s.%(ext)s+']
    command.extend(search)
    command.extend(extras)
    call(command, shell=False)


def mix_song_download_by_name(name, sub, sub_data, url=''):
    print("\nSelect options for {}".format(name))
    print()
    choice = download_menu()

    if choice == '1':
        song_download_by_name(name, sub, sub_data, url)

    if choice == '2':
        video_song_download_by_name(name, sub, sub_data, url)


def menu():
    print()
    print('1. Display Saavn Weekly Top')
    print('2. Display Hindi Chartbusters')
    print('3. Display English Chartbusters')
    print('4. Download Weekly Top Mix (video/song )')
    print('5. Download Weekly Top Songs')
    print('6. Download Weekly Top Video Songs')
    print('7. Download by Search')
    print('8. Download by Ranking in table')
    print('9. Download by URL', end='\n\n')
    choice = input('Enter choice: ')
    print()
    while choice not in ['1', '2', '3', '4', '5', '6', '7','8','9']:
        print(Color('{autored}Wrong Choice{/autored}'))
        choice = input('\nEnter choice: ')
        print()

    return choice


def song_list_menu():
    print('Select from the above lists\n')
    print('1. Saavn Weekly Top')
    print('2. Hindi Chartbusters')
    print('3. English Chartbusters')
    print()
    choice = input('Enter choice: ')
    print()
    while choice not in ['1', '2', '3']:
        print(Color('{autored}Wrong Choice{/autored}'))
        choice = input('\nEnter choice: ')
        print()

    return choice


def song_list_options(choice):
    
    if choice == '1':
        lang = input("Enter songs' lanuguage (hindi/english) : ")
        print()
        res = requests.get("https://www.saavn.com/s/featured/" + lang + "/Weekly+Top+Songs")
    
    if choice == '2':
        res = requests.get("https://www.saavn.com/s/charts/Hindi-Chartbusters/u-75xwHI4ks_?&utm_content=wap%3Ahome%3Atop_charts%3Aplay%3Aclick&utm_page=home&utm_button=top_charts")
    
    if choice == '3':
        res = requests.get("https://www.saavn.com/s/charts/English-Chartbusters/9J4ePDXBp8k_?utm_content=wap%3Aall_top_charts%3Atop_charts%3Aplay%3Aclick&utm_page=all_top_charts&utm_button=top_charts&")

    return res


def main():
    choice = menu()

    if choice == '1':
        limit = input('Enter the number of songs: ')
        print()
        res=song_list_options(choice)
        song_print(songs_info(res), limit)

    if choice == '2':
        limit = input('Enter the number of songs: ')
        print()
        res=song_list_options(choice)
        song_print(songs_info(res), limit)

    if choice == '3':
        limit = input('Enter the number of songs: ')
        print()
        res=song_list_options(choice)
        song_print(songs_info(res), limit)


    if choice in ['4', '5', '6']:
        ch=song_list_menu()
        res=song_list_options(ch)
        limit = input('Enter the number of songs or videos: ')
        print()
        song_list = song_print(songs_info(res), limit)
        print()
        sub = input('Want to download external subtitles file (y/n): ')
        sub_data = []
        if sub == 'y' or sub == 'Y':
            sub_data = subtitles()
        print()
        for song in song_list:

            if choice == '4':
                mix_song_download_by_name(song, sub, sub_data)
            if choice == '5':
                song_download_by_name(song, sub, sub_data)
            if choice == '6':
                video_song_download_by_name(song, sub, sub_data)
            print()

    if choice == '7':
        name = input('Enter the name of song or videos: ')
        print()
        sub = input('Want to download external subtitles file (y/n): ')
        sub_data = []
        if sub == 'y' or sub == 'Y':
            sub_data = subtitles()
        mix_song_download_by_name(name, sub, sub_data)

    if choice == '8':
        ch=song_list_menu()
        res=song_list_options(ch)
        song_list = song_print(songs_info(res))
        print()
        rank = input('Enter the number from the table: ')
        print()
        sub = input('Want to download external subtitles file (y/n): ')
        sub_data = []
        if sub == 'y' or sub == 'Y':
            sub_data = subtitles()
        mix_song_download_by_name(song_list[int(rank) - 1], sub, sub_data)

    if choice == '9':
        song_url = input('Enter the url: ')
        name = ''
        print()
        sub = input('Want to download external subtitles file (y/n): ')
        sub_data = []
        if sub == 'y' or sub == 'Y':
            sub_data = subtitles()
        mix_song_download_by_name(name, sub, sub_data, song_url)
    print()

if __name__ == '__main__':
    main()


