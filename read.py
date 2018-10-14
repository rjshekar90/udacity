import urllib

def read_text():
    quotes = open("/home/rjshekar90/Desktop/python/Udacity/movie_quotes.txt")
    contents = quotes.read()
    print contents
    quotes.close()


def check_pro(text_check):
    conn = urllib.urlopen("http://www.wdylike.appspot.com/?q=ger")


read_text()
