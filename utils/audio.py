import youtube_dl

# fix filename bugs
def fixName(filename):
    loop = False
    word = ""
    notValid = "<>:\"/\\|?*%"
    for char in filename:
        for forbidden in notValid:
           if char == forbidden:
                word += " "
                loop = True
                break
        if loop is True:
            loop = False
            continue
        word += char
    return word


class Audio:
    def __init__(self, link=None):
        self.link = [link]
        self.infos = youtube_dl.YoutubeDL().extract_info(link, download=False)



    def set_filename(self, title):
        word = ""
        loop = 0
        for i in title:
            loop += 1
            if loop == 50:
                break
            word += i

        word = fixName(word)
        return word + ".mp3"


    def getFilename(self):
        return self.set_filename(self.infos["title"])

    def download(self, path):
        filename = self.set_filename(self.infos["title"])
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": path + "\\" + filename
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(self.link)
