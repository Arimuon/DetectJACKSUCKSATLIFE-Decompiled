# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.6

import urllib
import time
import winsound
import random
import urllib.request as urllib
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
url = 'https://bans.skycade.net/bans.php'

def Beepsong():
    for i in range(2):
        for i in range(14):
            winsound.Beep(random.randint(100, 400), 180)
        
        winsound.Beep(700, 1000)
        for i in range(14):
            winsound.Beep(random.randint(100, 400), 180)
        
        winsound.Beep(700, 1000)
    

Beepsong()
nope = 0
while None:
    request = urllib.request.Request(url, {
        'User-Agent': user_agent }, **('headers',))
    response = urllib.request.urlopen(request)
    html = response.read()
    if b'<br>JackSucksAtMC</p>' in html:
        print('Found JACK!')
        Beepsong()
    else:
        nope = nope + 1
        if nope == 3:
            print('Nope...')
            nope = 0
    time.sleep(70)
print('error')