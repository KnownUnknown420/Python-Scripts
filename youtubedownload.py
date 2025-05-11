import yt_dlp as youtube_dl
import os
import subprocess

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        return False

def download_youtube_video(video_url, save_path):
    if not check_ffmpeg():
        print("ERROR: ffmpeg is not installed. Please install ffmpeg and try again.")
        print("On Linux, you can install it with: sudo apt install ffmpeg")
        return
    
    try:
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        }

        print("Downloading video...")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {e}")
