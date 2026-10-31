import yt_dlp

while True:
    url = input("enter the url: ")

    if url.lower() == "exit":
        break
    yt_dlp.YoutubeDL({
        "format": "bestvideo+bestaudio/best",
        "ffmpeg_location": r"C:\Users\omars\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin",
        "paths": {"home": r"E:\dowloaded youtube videos"}
    }).download([url])
