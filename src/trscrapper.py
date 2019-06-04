import requests
from bs4 import BeautifulSoup
import os

trackers = []

def collectTrackers(urlstr):
    global trackers
    d = str(requests.get(urlstr).text.encode('utf8'))
    s = BeautifulSoup(d, 'html.parser')
    a = s.get_text().split("/announce")
    l = len(a)
    del(a[l-1])
    l = len(a)

    for i in range(0,l):
        t = a[i]
        j = len(t) - 3
        while t[j] != '/':
            j = j -1
        t = (t[j-5:]+"/announce").replace(" ", "").split("://")
        if "t" in t[0]:
            if "s" in t[0]:
                a[i] = "https://"+t[1]
            else:
                a[i] = "http://"+t[1]
        else:
            a[i] = "udp://"+t[1]
        
        if a[i] not in trackers:
            trackers.append(a[i])

#-----------------------------------------------------------------------------------
print("Quering @ https://startpage.com ...")
r = requests.get("https://www.startpage.com/do/asearch?q=torrent+tracker+list").text
print("Results fetched.")

soup = BeautifulSoup(r, 'html.parser')
print("Collecting trackers (this can take some time depending on your internet speed. BE PATIENT) ...", end='')
arr = soup.find_all('h3', 'search-item__title')

wct = 0
for a in arr:
    print(".", end='')
    t = str(a).lower()
    if "torrent" in t and "tracker" in t and "list" in t:
        i = t.index("<a href=\"") + 9
        j = t[i:].index("\"")
        collectTrackers(t[i:i+j])
        wct = wct + 1
        
print("\nCollected "+str(len(trackers))+" trackers from "+str(wct)+" websites.")

print("Writing to file ...")
c = ""
for t in trackers:
    c = c + t + "\n"
f = open('trackers.txt', 'w')
f.write(c.strip())
f.close()

print("DONE. SCRAPPING COMPLETE. >>> Press ENTER key to continue <<<")
x = input()
os.system("trackers.txt")
exit()