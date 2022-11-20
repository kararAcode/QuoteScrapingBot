from instabot import Bot
from designQuote import designQuotePost
from text import fetchImg, organizeInfo, textRecognizer

def post(imgPath):
    bot = Bot()
    bot.login(username="", password="")

    bot.upload_photo(imgPath, "")

if __name__ == "__main__":
    fetchImg()
    quoteData = organizeInfo(textRecognizer("img.jpg"))
    designQuotePost(quoteData)
    post("quotePost.jpg")