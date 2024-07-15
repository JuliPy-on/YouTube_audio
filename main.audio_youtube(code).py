import yt_dlp as youtube_dl
import moviepy.editor as mp
import os


def download_youtube_video():
    youtube_url = input('Enter the YouTube video URL: ')

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloaded_video.%(ext)s',
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        local_video_path = 'downloaded_video.mp4'
        video = mp.VideoFileClip(local_video_path)
        try:
            video.preview()
        except ImportError:
            print('clip.preview requires Pygame installed')

        audio = video.audio
        audio.write_audiofile('my_audio.mp3')

        os.remove(local_video_path)

    except Exception as e:
        print('An error occurred: {}'.format(e))


download_youtube_video()
