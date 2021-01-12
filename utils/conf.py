import json

config = {}
with open("./conf.json") as file:
    config = json.loads(file.read())


class Configuration:
    def __init__(self):
        # mp3
        self.XbuttonMP3 = 0
        self.YbuttonMP3 = 0
        self.padxButtonMP3 = 0

        # mp4
        self.XbuttonMP4 = 0
        self.YbuttonMP4 = 0
        self.padxButtonMP4 = 0

        # clear
        self.XbuttonClear = 0
        self.YbuttonClear = 0
        self.padxButtonClear = 0

        # paste
        self.XbuttonPaste = 0
        self.YbuttonPaste = 0
        self.padxButtonPaste = 0

        # Download Progress
        self.Xdownloaded = 0
        self.Xdownloading = 0

        # browse
        self.XbuttonBrowse = 0
        self.YbuttonBrowse = 0
        self.padxButtonBrowse = 0

    def EN(self):
        language = "EN"

        # mp3
        self.XbuttonMP3 = config[language]["buttonMP3"].get("x")
        self.YbuttonMP3 = config[language]["buttonMP3"].get("y")
        self.padxButtonMP3 = config[language]["buttonMP4"].get("padx")

        # mp4
        self.XbuttonMP4 = config[language]["buttonMP4"].get("x")
        self.YbuttonMP4 = config[language]["buttonMP4"].get("y")
        self.padxButtonMP4 = config[language]["buttonMP4"].get("padx")

        # clear
        self.XbuttonClear = config[language]["buttonClear"].get("x")
        self.YbuttonClear = config[language]["buttonClear"].get("y")
        self.padxButtonClear = config[language]["buttonClear"].get("padx")

        # paste
        self.XbuttonPaste = config[language]["buttonPaste"].get("x")
        self.YbuttonPaste = config[language]["buttonPaste"].get("y")
        self.padxButtonClear = config[language]["buttonPaste"].get("padx")
        self.padxButtonPaste = config[language]["buttonClear"].get("padx")

        # Download Progress
        self.Xdownloaded = config[language]["Downloaded"].get("x")
        self.Xdownloading = config[language]["Downloading"].get("x")

        # browse
        self.XbuttonBrowse = config[language]["buttonBrowse"].get("x")
        self.YbuttonBrowse = config[language]["buttonBrowse"].get("y")
        self.padxButtonBrowse = config[language]["buttonBrowse"].get("padx")

    def FR(self):
        language = "FR"

        # mp3
        self.XbuttonMP3 = config[language]["buttonMP3"].get("x")
        self.YbuttonMP3 = config[language]["buttonMP3"].get("y")
        self.padxButtonMP3 = config[language]["buttonMP4"].get("padx")

        # mp4
        self.XbuttonMP4 = config[language]["buttonMP4"].get("x")
        self.YbuttonMP4 = config[language]["buttonMP4"].get("y")
        self.padxButtonMP4 = config[language]["buttonMP4"].get("padx")

        # clear
        self.XbuttonClear = config[language]["buttonClear"].get("x")
        self.YbuttonClear = config[language]["buttonClear"].get("y")
        self.padxButtonClear = config[language]["buttonClear"].get("padx")

        # paste
        self.XbuttonPaste = config[language]["buttonPaste"].get("x")
        self.YbuttonPaste = config[language]["buttonPaste"].get("y")
        self.padxButtonPaste = config[language]["buttonPaste"].get("padx")

        # Download Progress
        self.Xdownloaded = config[language]["Downloaded"].get("x")
        self.Xdownloading = config[language]["Downloading"].get("x")

        # browse
        self.XbuttonBrowse = config[language]["buttonBrowse"].get("x")
        self.YbuttonBrowse = config[language]["buttonBrowse"].get("y")
        self.padxButtonBrowse = config[language]["buttonBrowse"].get("padx")
