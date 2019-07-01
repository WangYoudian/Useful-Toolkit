import html.parser

parser = html.parser.HTMLParser()
print(parser.unescape("&amp;"))