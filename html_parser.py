import sys
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for attr in attrs:
                print "->", attr[0],">", attr[1]
    #def get_starttag_text(self, data):
    #    print "-> ", data
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for attr in attrs:
                print "->", attr[0],">", attr[1]
    #def handle_data(self, data):
    #    print "->", data

# instantiate the parser and fed it some HTML
ciag = sys.stdin 
parser = MyHTMLParser()
for linia in ciag:
    parser.feed(linia)