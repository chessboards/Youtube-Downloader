from pytube import YouTube
import re

# note to self: https://code.visualstudio.com/docs/python/environments
#               use debugger to avoid execution policy shenanigans

videoChoices = ["v", "video", "0", "vid", "mp4"]
audioChoices = ["a", "audio", "1", "aud", "sound", "mp3"]

index = 0

def progressCallback(_stream, _chunk, bytes_remaining):
    """Display to the user the bytes remaining along with an animation while they wait"""
    global index
    animationReel = ["/", ".", "\\"]
    
    # 3 - 1 = 0,1,2
    if index > len(animationReel) - 1:
        index = 0
        
    print(f"{animationReel[index]} | {bytes_remaining} bytes remaining...")
    
    index += 1
   
def sanitizeTitle(title):
    """Sanitizes the passed title string to allow the file to be saved on windows without introducing illegal characters"""
    matches = re.findall(r"[^/\\:*?\"<>|]+", title) 

    fullstring = ""
    for match in matches:
        fullstring += match
        
    return fullstring
    
    
def main():
    """Main function of the program called by the entry point."""
    ## User input entries ##
    
    link = input("Enter youtube url: ")
    filetype = input("Video or audio?: ")
    
    extension = ""
    if filetype.lower() in videoChoices: extension = "mp4"
    if filetype.lower() in audioChoices: extension = "webm" # lib only allows webm
    else:
        print("Error: Invalid filetype.")
        return # exit program
        
    filename = input("File name (leave blank to use video title): ")
    destin = input("Full path destination: ")

    video = YouTube(link, progressCallback)
    stream = "" # empty for scope
    
    if extension == "webm":
        stream = video.streams.filter(only_audio = True, subtype="webm").first() # best with supplied params
    else:
        stream = video.streams.filter(file_extension = extension).get_highest_resolution() # best video resolution
        
    # default filename to title
    if (filename == "" or filename == " "):
        filename = sanitizeTitle(video.title) # sanitize the youtube title for windows
        
    ## Begin downloading... ##
    
    print(f"\nDownloading {video.title} by {video.author}")

    stream.download(destin, f"{filename}.{extension}") # extension not automatically added
    print("Done!")


# entry point
if __name__ == "__main__":
    main()
