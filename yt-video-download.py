import os
from yt_dlp import YoutubeDL

def download_video(video_url, save_path=".", video_quality="best", file_format="mp4"):
    """
    Advanced YouTube Video Downloader.

    :param video_url: URL of the YouTube video to download.
    :param save_path: Directory to save the downloaded video. Default is current directory.
    :param video_quality: Quality of the video ('best', 'worst', '1080p', etc.).
    :param file_format: File format for the output (e.g., 'mp4', 'mkv').
    """
    try:
        # Configure options
        ydl_opts = {
            'format': f'{video_quality}+bestaudio/best',  # Video quality + best audio
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),  # Save file with title
            'merge_output_format': file_format,  # Merge into desired file format
            'quiet': False,  # Show download progress
            'noplaylist': True,  # Download only the video (not the playlist)
            'progress_hooks': [progress_hook],  # Attach progress hook
        }

        # Download video
        with YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download for: {video_url}")
            ydl.download([video_url])

    except Exception as e:
        print(f"Error: {e}")

def progress_hook(d):
    """
    Hook to display progress during download.

    :param d: Dictionary with progress data.
    """
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} - {d['_eta_str']} remaining.")
    elif d['status'] == 'finished':
        print(f"Download complete! File saved to {d['filename']}")

if __name__ == "__main__":
    # Input from user
    video_url = input("Enter YouTube video URL: ").strip()
    save_path = input("Enter save directory (leave blank for current directory): ").strip() or "."
    video_quality = input("Enter video quality (default 'best'): ").strip() or "best"
    file_format = input("Enter file format (default 'mp4'): ").strip() or "mp4"

    # Validate save directory
    if not os.path.exists(save_path):
        print(f"Creating directory: {save_path}")
        os.makedirs(save_path)

    # Download video
    download_video(video_url, save_path, video_quality, file_format)
