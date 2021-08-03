import youtube_dl

# Notes:
    # notetoself: https://code.visualstudio.com/docs/python/environments
    # clearer docs: https://youtube-dl.readthedocs.io/en/latest/
    # the github youtube-dl documentation needs to be written better

class MediaDownloader():
    def __init__(self):
        """Initializes an empty option dictionary for youtube-dl"""
        self.ydl_opts = {}
        
    def downloadContent(self, url):
        """Asks youtube-dl to download the media based on the options defined in self.ydl_opts.
           Returns void."""
        print("\n")     # formatting
        
        # If the user has selected an available content type, 
        if len( self.ydl_opts.keys() ) != 0:
            try:
                with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                    ydl.download([rf"{url}"])       # escapes url
                    ydl.cache.remove()              # finally, clear the cache for privacy (and incorrect video downloads for certain errors)
                    
                print("\nFile has been downloaded!")
            except Exception as e:
                print(e.args[0])
            
    def setContentType(self, string_code):
        """Sets the content type to either video format or audio format based on the user's input.
           Returns bool based on whether user input matches the available content types."""
        # Video
        if string_code == "0":
            self.ydl_opts = {
                #'format': 'bestvideo[ext=mp4]+bestaudio/best[ext=mp4]/best[ext=mp3]', # why doesn't this work?
                'format': '137+140',
                'video-format': 'mp4',
                "outtmpl": rf"{dir}" + "/%(title)s.%(ext)s",    # escape dir. what is the %(key)s thing? (probably a tag handled by ytdl)
            }
            
        # Music
        elif string_code == "1":
            self.ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }],
                'audio-format': 'mp3',
                "outtmpl": rf"{dir}" + "/%(title)s.%(ext)s",
            }
            
        # Unkown content type. Error
        else:
            print("Error: Invalid content type.")
            return False    # return an error code
            
        # otherwise if no error occured, return with success.
        return True
    
### Main ###
if __name__ == "__main__":
    print("Welcome to the simple youtube video downloader.")
    print("\nIf you recieve errors related to ffmpeg, try running ffmpeg.exe from https://www.gyan.dev/ffmpeg/builds/.")

    dir = input ("\nEnter a full-path directory: ")
    url = input("Enter the whole video URL: ")
    ctype = input("Video (0) or music file (1)?: ")
    
    downloader = MediaDownloader()
    success = downloader.setContentType(ctype)
    
    if success:
        downloader.downloadContent(url)
