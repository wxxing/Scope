# coding=utf8

import re,string

scopes = 'aeg啊让噶啊我俄方 5115VWe fwv '
add = '!,;:?"\'、**...；;:,【】（）()...〓'
scopes = re.sub("[{}]+".format(string.punctuation + add + string.digits), "", scopes)
print(scopes)
