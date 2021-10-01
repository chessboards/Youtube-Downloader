# Notes:
    # notetoself: https://code.visualstudio.com/docs/python/environments
    #             https://pytube.io/en/latest/user/streams.html#downloading-streams
    
from pytube import YouTube


index = 0

def progressCallback(_stream, _chunk, bytes_remaining):
    global index
    animationReel = ["/", ".", "\\"]
    
    # 3 - 1 = 0,1,2
    if index > len(animationReel) - 1:
        index = 0
        
    print(f"{animationReel[index]} | {bytes_remaining} bytes remaining...")
    
    index += 1
    
    
if __name__ == "__main__":
    # vars
    link = input("Enter youtube url: ")
    destin = input("Full path destination: ")
    filename = input("File name (leave blank to use video title): ")

    video = YouTube(link, progressCallback)
    stream = (
                video.streams
                             .filter(file_extension='mp4')
                             .get_highest_resolution()
             )

    # default filename to title
    if (filename == "" or filename == " "):
        filename = video.title
        
    print(f"\nDownloading {video.title} by {video.author}")

    stream.download(destin, filename + ".mp4") # extension not automatically added
    print("Done!")
