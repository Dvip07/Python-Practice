# Sanitizing and Cleaning Up Text
# 2.12.1

s = 'pýtĥöñ\fis\tawesome\r\n'
s

# 2.12.2
remap = {
    ord('\t') : ' ',
    ord('\t') : ' ',
    ord('\t') : None     #Deleted
}
a = s.translate(remap)
a

# 2.12.3
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                        if unicodedata.combining(chr(c))
b = unicodedata.normalize('NFD', a)
b
b.translate(cmb_chrs)

# 2.12.4
digitmap = { c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(char(c)) == 'Nd'}
len(digitmap)
# Arabic digits
x = '\u0661\u0662\u0663'
x.translate(digitmap)


# 2.12.5
a
b = unicodedata.normalize('NFD', a)
b.encode('ascii', 'ignore').decode('ascii')

# Discussion
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', '')
    s = s.replace('\f', '')
    return s

