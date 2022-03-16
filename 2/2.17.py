# Handling HTML and XML Entities in Text
# 2.17.1

s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))

# Disable escaping of quotes
print(html.escape(s, quote=False))

# 2.17.2
s = 'Spicy Jalapeno'
s.encode('ascii', errors='xmlcharrefreplace')

# 2.17.3
s = 'Spicy &quot;Jalpeno&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
p.unescape(s)

# --
t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
unescape(t)
