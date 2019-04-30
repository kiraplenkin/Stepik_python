import re
import urllib.request

URL_1 = input()
URL_2 = input()


def get_links(url):
    try:
        res = urllib.request.urlopen(url)
        mybytes = res.read()
        mystr = mybytes.decode('utf8')
        res.close()
        links = re.findall(r'<a.*href="([^"]*)"', mystr)
    except:
        return []
    else:
        return links


def two_steps():
    links1 = get_links(URL_1)

    for link in links1:
        links2 = get_links(link)
        if URL_2 in links2:
            return True
    return False


if two_steps():
    print('Yes')
else:
    print('No')
