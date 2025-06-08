import subprocess
import os
import sys
from yt_dlp import YoutubeDL

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        return False

def get_next_index():
    index = 1
    while True:
        if not os.path.exists(f"video{index}.avi") and not os.path.exists(f"video{index}sound.ogg"):
            return index
        index += 1

def download_youtube_video(url, output_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(output_path, 'temp_download.%(ext)s'),
        'quiet': False,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    downloaded_file = os.path.join(output_path, 'temp_download.mp4')
    return downloaded_file

def convert_to_blitz_format(input_file, index):
    avi_file = f"video{index}.avi"
    ogg_file = f"video{index}sound.ogg"

    print(f"\nConverting to AVI (1280x720): {avi_file}")
    subprocess.run([
        "ffmpeg", "-i", input_file,
        "-vf", "scale='min(1920,iw)':-2",
        "-c:v", "libxvid", "-qscale:v", "5",
        "-an",
        avi_file
    ], check=True)

    print(f"Extracting audio to OGG: {ogg_file}")
    subprocess.run([
        "ffmpeg", "-i", input_file,
        "-vn",
        "-c:a", "libvorbis",
        ogg_file
    ], check=True)

    print("Conversion complete.")

def handle_dragged_files(file_list):
    for file_path in file_list:
        if os.path.isfile(file_path):
            print(f"\nProcessing: {file_path}")
            index = get_next_index()
            try:
                convert_to_blitz_format(file_path, index)
            except subprocess.CalledProcessError as e:
                print(f"Conversion failed for {file_path}: {e}")
        else:
            print(f"Skipped invalid file: {file_path}")

def main():
    if not check_ffmpeg():
        print("ERROR: ffmpeg is not installed or not in PATH.")
        input("Press Enter to exit...")
        return

    # Handle drag-and-drop files
    dragged_files = [arg for arg in sys.argv[1:] if os.path.isfile(arg)]
    if dragged_files:
        handle_dragged_files(dragged_files)
        input("\nPress Enter to exit...")
        return

    # Fallback to YouTube download
    url = input("Enter YouTube video URL: ").strip()
    if not url:
        print("No URL provided.")
        return

    output_dir = os.getcwd()
    print("Downloading from YouTube...")
    try:
        downloaded_file = download_youtube_video(url, output_dir)
    except Exception as e:
        print(f"Download failed: {e}")
        input("Press Enter to exit...")
        return

    index = get_next_index()
    try:
        convert_to_blitz_format(downloaded_file, index)
        os.remove(downloaded_file)
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed: {e}")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
