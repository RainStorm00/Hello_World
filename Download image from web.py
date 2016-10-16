import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,100)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image('http://66.media.tumblr.com/2a37d1b8b1f66986c7dccf6600dcc1c7/tumblr_of31exELjR1u5a24ho1_1280.jpg')