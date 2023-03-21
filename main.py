from moviepy.editor import AudioFileClip, concatenate_audioclips
from PIL import Image
from yandex_music import Client
import os
import sys
import requests
import subprocess
import re

def main():
    print("1-Видео с картинкой")
    print("2-Клип")
    print("3-Подборка")
    print("9-Удаление кеша")
    print("0-Выйти")
    global navigate
    navigate = int(input("Пункт: "))
    if navigate == 1:
        audioclip()
    elif navigate == 2:
        comp()
    elif navigate == 3:
        podborka()
    elif navigate == 7:
        pass
    elif navigate == 9:
        try:
            print("Удаление кеша...")
            os.remove("a0.mp3")
            os.remove("a1.mp3")
            os.remove("a2.mp3")
            os.remove("image0.jpg")
            os.remove("image1.jpg")
            os.remove("image2.jpg")
            os.remove("in0.mp4")
            os.remove("in1.mp4")
            os.remove("in2.mp4")
            os.remove("in3.mp4")
            os.remove("final_concatenation.mp3")
            os.remove("output.mp4")
            print("Кеш удалён!")
            main()
        except:
            print("Не найден файл! Возможно он был уже удален.")
            main()
    elif navigate == 0:
        sys.exit()
    else:
        print("Введите правильный пункт!")
        main()

def audioclip():
    track = int(input("Трек: "))
    client.users_likes_tracks()[track - 1].fetch_track().download(f'track.mp3')
    img_index = input("Встать путь до изображения: ")
    img = Image.open(img_index)
    width = 1500
    height = 1500
    resized_img = img.resize((width, height), Image.ANTIALIAS)
    resized_img.save("image.jpg")
    os.system(f"ffmpeg -y -loop 1 -i image.jpg -i track.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest phonk.mp4")
    print("Видео готово!")

def comp():
    i = 0
    j = 0
    audio_list = []
    r_list = []
    name = []
    time_list = []
    print("Введите нужные треки!")
    while i < 10:
        track = int(input("Трек: "))
        client.users_likes_tracks()[track - 1].fetch_track().download(f'a{i}.mp3')
        audio_list.append(track - 1)
        i = i + 1
        time_list.append(int(input("Введите начало трека (в секундах): ")))
    clip1 = AudioFileClip("a0.mp3").subclip(time_list[0], time_list[0] + 10)
    clip2 = AudioFileClip("a1.mp3").subclip(time_list[1] + 3, time_list[1] + 9.4)
    clip3 = AudioFileClip("a2.mp3").subclip(time_list[2] + 3, time_list[2] + 9.4)
    clip4 = AudioFileClip("a3.mp3").subclip(time_list[3] + 3, time_list[3] + 9.4)
    clip5 = AudioFileClip("a4.mp3").subclip(time_list[4] + 3, time_list[4] + 9.4)
    clip6 = AudioFileClip("a5.mp3").subclip(time_list[5] + 3, time_list[5] + 9.4)
    clip7 = AudioFileClip("a6.mp3").subclip(time_list[6] + 3, time_list[6] + 9.4)
    clip8 = AudioFileClip("a7.mp3").subclip(time_list[7] + 3, time_list[7] + 9.4)
    clip9 = AudioFileClip("a8.mp3").subclip(time_list[8] + 3, time_list[8] + 9.4)
    clip10 = AudioFileClip("a9.mp3").subclip(time_list[9] + 3, time_list[9] + 9.4)
    final_clip = concatenate_audioclips([clip1, clip2, clip3, clip4, clip5, clip6, clip7, clip8, clip9, clip10])
    final_clip.write_audiofile("final_concatenation.mp3")
    i = 0
    while i < 10:
        r = requests.get(f'''http://{client.users_likes_tracks()[audio_list[i]].fetch_track().cover_uri.replace("%%", "400x400")}''')
        with open(f'image{i}.jpg', 'wb') as f:
            f.write(r.content)
        img = Image.open(f'image{i}.jpg')
        width = 200
        height = 200
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        resized_img.save(f'image{i}.jpg')
        i = i + 1
    i = 0
    os.system('''ffmpeg -y -i input.mp4 -loop 1 -i image0.jpg -ss 00:00:00 -filter_complex "[1]fade=in:st=3.4:d=0.5:alpha=1[i]; [0][i]overlay=main_w/2-overlay_w/2-0+0:main_h/2-overlay_h/2-0+0:shortest=1"  in0.mp4''')
    os.system('''ffmpeg -y -i in0.mp4 -loop 1 -i image1.jpg -ss 00:00:00 -filter_complex "[1]fade=in:st=9.9:d=0.5:alpha=1[i]; [0][i]overlay=main_w/2-overlay_w/2-0+0:main_h/2-overlay_h/2-0+0:shortest=1"  in1.mp4''')
    os.system('''ffmpeg -y -i in1.mp4 -loop 1 -i image2.jpg -ss 00:00:00 -filter_complex "[1]fade=in:st=16.3:d=0.5:alpha=1[i]; [0][i]overlay=main_w/2-overlay_w/2-0+0:main_h/2-overlay_h/2-0+0:shortest=1"  in2.mp4''')
    os.system('''ffmpeg -y -i in2.mp4 -loop 1 -i image3.jpg -ss 00:00:00 -filter_complex "[1]fade=in:st=22.7:d=0.5:alpha=1[i]; [0][i]overlay=main_w/2-overlay_w/2-0+0:main_h/2-overlay_h/2-0+0:shortest=1"  in3.mp4''')
    os.system('''ffmpeg -y -i in3.mp4 -loop 1 -i image4.jpg -ss 00:00:00 -filter_complex "[1]fade=in:st=29.1:d=0.5:alpha=1[i]; [0][i]overlay=main_w/2-overlay_w/2-0+0:main_h/2-overlay_h/2-0+0:shortest=1"  in4.mp4''')
    os.system('''ffmpeg -y -i in4.mp4 -loop 1 -i image5.jpg -ss 00:00:00 -filter_complex "[1]fade=in:st=35.5:d=0.5:alpha=1[i]; [0][i]overlay=main_w/2-overlay_w/2-0+0:main_h/2-overlay_h/2-0+0:shortest=1"  in5.mp4''')
    os.system('''ffmpeg -y -i in5.mp4 -loop 1 -i image6.jpg -ss 00:00:00 -filter_complex "[1]fade=in:st=42.0:d=0.5:alpha=1[i]; [0][i]overlay=main_w/2-overlay_w/2-0+0:main_h/2-overlay_h/2-0+0:shortest=1"  in6.mp4''')
    os.system('''ffmpeg -y -i in6.mp4 -loop 1 -i image7.jpg -ss 00:00:00 -filter_complex "[1]fade=in:st=48.3:d=0.5:alpha=1[i]; [0][i]overlay=main_w/2-overlay_w/2-0+0:main_h/2-overlay_h/2-0+0:shortest=1"  in7.mp4''')
    os.system('''ffmpeg -y -i in7.mp4 -loop 1 -i image8.jpg -ss 00:00:00 -filter_complex "[1]fade=in:st=54.8:d=0.5:alpha=1[i]; [0][i]overlay=main_w/2-overlay_w/2-0+0:main_h/2-overlay_h/2-0+0:shortest=1"  in8.mp4''')
    os.system('''ffmpeg -y -i in8.mp4 -loop 1 -i image9.jpg -ss 00:00:00 -filter_complex "[1]fade=in:st=61.2:d=0.5:alpha=1[i]; [0][i]overlay=main_w/2-overlay_w/2-0+0:main_h/2-overlay_h/2-0+0:shortest=1"  in9.mp4''')
    while i < 10:
        while j < len(client.users_likes_tracks()[audio_list[i]].fetch_track().artists):
            name.append(client.users_likes_tracks()[audio_list[i]].fetch_track().artists[j].name)
            j = j + 1
        r_list.append(f'''{",".join(map(str, name))} - {client.users_likes_tracks()[audio_list[i]].fetch_track().title}''')
        name.clear()
        i = i + 1
        j = 0
    with open(f'send.cmd', 'at') as f:
        f.write(f'''3.5 drawtext reinit 'text={r_list[0]}';
10.0 drawtext reinit 'text={r_list[1]}';
16.4 drawtext reinit 'text={r_list[2]}';
22.8 drawtext reinit 'text={r_list[3]}';
29.2 drawtext reinit 'text={r_list[4]}';
35.6 drawtext reinit 'text={r_list[5]}';
42.0 drawtext reinit 'text={r_list[6]}';
48.4 drawtext reinit 'text={r_list[7]}';
54.8 drawtext reinit 'text={r_list[8]}';
61.2 drawtext reinit 'text={r_list[9]}';
''')
    os.system('''ffmpeg -y -i in9.mp4 -vf "sendcmd=f=send.cmd,drawtext=fontfile=arial.ttf:text="anxnas":fontsize=20:fontcolor=black:x=(w-text_w)/2:y=h-th-200" in10.mp4''')
    os.system('''ffmpeg -i in10.mp4 -filter_complex "amovie=final_concatenation.mp3:loop=0,asetpts=N/SR/TB[over]; [0][over]amix=duration=shortest" -c:v copy output.mp4''')
    #f = open('send.cmd', 'w')
    #f.close()
    print("Видео готово!")

def podborka():
    i = 0
    h = 0
    m = 0
    s = 0
    j = 0
    audio_list = []
    r_list = []
    name = []
    time_list = []
    print("Выберите нужные треки для ролика")
    while i < 27:
        track = int(input("Трек: "))
        client.users_likes_tracks()[track - 1].fetch_track().download(f'podborka/a{i}.mp3')
        audio_list.append(track - 1)
        i = i + 1
    i = 0
    while i < 27:
        while j < len(client.users_likes_tracks()[audio_list[i]].fetch_track().artists):
            name.append(client.users_likes_tracks()[audio_list[i]].fetch_track().artists[j].name)
            j = j + 1
        j = 0
        name.clear()
        process = subprocess.Popen(['ffmpeg', '-i', f'podborka/a{i}.mp3'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        stdout, stderr = process.communicate()
        matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout.decode(),
                            re.DOTALL).groupdict()
        h = h + int(matches['hours'])
        m = m + int(matches['minutes'])
        s = s + round(float(matches['seconds']))
        print(f'''{",".join(map(str, name))} - {client.users_likes_tracks()[audio_list[i]].fetch_track().title} - {h}:{m}:{s}''')
        i = i + 1
    clip1 = AudioFileClip("podborka/a0.mp3")
    clip2 = AudioFileClip("podborka/a1.mp3")
    clip3 = AudioFileClip("podborka/a2.mp3")
    clip4 = AudioFileClip("podborka/a3.mp3")
    clip5 = AudioFileClip("podborka/a4.mp3")
    clip6 = AudioFileClip("podborka/a5.mp3")
    clip7 = AudioFileClip("podborka/a6.mp3")
    clip8 = AudioFileClip("podborka/a7.mp3")
    clip9 = AudioFileClip("podborka/a8.mp3")
    clip10 = AudioFileClip("podborka/a9.mp3")
    clip11 = AudioFileClip("podborka/a10.mp3")
    clip12 = AudioFileClip("podborka/a11.mp3")
    clip13 = AudioFileClip("podborka/a12.mp3")
    clip14 = AudioFileClip("podborka/a13.mp3")
    clip15 = AudioFileClip("podborka/a14.mp3")
    clip16 = AudioFileClip("podborka/a15.mp3")
    clip17 = AudioFileClip("podborka/a16.mp3")
    clip18 = AudioFileClip("podborka/a17.mp3")
    clip19 = AudioFileClip("podborka/a18.mp3")
    clip20 = AudioFileClip("podborka/a19.mp3")
    clip21 = AudioFileClip("podborka/a20.mp3")
    clip22 = AudioFileClip("podborka/a21.mp3")
    clip23 = AudioFileClip("podborka/a22.mp3")
    clip24 = AudioFileClip("podborka/a23.mp3")
    clip25 = AudioFileClip("podborka/a24.mp3")
    clip26 = AudioFileClip("podborka/a25.mp3")
    clip27 = AudioFileClip("podborka/a26.mp3")
    final_clip = concatenate_audioclips([clip1, clip2, clip3, clip4, clip5, clip6, clip7, clip8, clip9, clip10, clip11, clip12, clip13, clip14, clip15, clip16, clip17, clip18, clip19, clip20, clip21, clip22, clip23, clip24, clip25, clip26, clip27])
    final_clip.write_audiofile("podborka_music.mp3")
    img_index = int(input("Введите номер изображения: "))
    img = Image.open(f'imagecoll/imgcl{img_index}.jpg')
    width = 1500
    height = 1500
    resized_img = img.resize((width, height), Image.ANTIALIAS)
    resized_img.save("image.jpg")
    os.system(f"ffmpeg -y -loop 1 -i image.jpg -i podborka_music.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest output.mp4")



if __name__ == "__main__":
    print('''
__________.__                   __      ___________           .__                ____   ____.__    .___                _____  .__                     
\______   \  |__   ____   ____ |  | __  \_   _____/_ __  _____|__| ____   ____   \   \ /   /|__| __| _/____  ____     /     \ |__|__  ___ ___________ 
 |     ___/  |  \ /  _ \ /    \|  |/ /   |    __)|  |  \/  ___/  |/  _ \ /    \   \   Y   / |  |/ __ |/ __ \/  _ \   /  \ /  \|  \  \/  // __ \_  __ \
 |    |   |   Y  (  <_> )   |  \    <    |     \ |  |  /\___ \|  (  <_> )   |  \   \     /  |  / /_/ \  ___(  <_> ) /    Y    \  |>    <\  ___/|  | \/
 |____|   |___|  /\____/|___|  /__|_ \   \___  / |____//____  >__|\____/|___|  /    \___/   |__\____ |\___  >____/  \____|__  /__/__/\_ \\___  >__|   
               \/            \/     \/       \/             \/               \/                     \/    \/                \/         \/    \/       
''')
    print("neirozxc v.1.5")
    client = Client('token').init()
    main()