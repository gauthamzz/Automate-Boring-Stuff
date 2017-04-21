#!/usr/bin/env python3

import requests,sys
if len(sys.argv)>1:
    url = ' '.join(sys.argv[1:])
else:
    url = 'https://raw.githubusercontent.com/gauthamzz/ecop/master/readme.md'
res = requests.get(url)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
print(res.text)