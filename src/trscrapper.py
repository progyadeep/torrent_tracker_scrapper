import requests
from bs4 import BeautifulSoup
import os

trackers = []
wct = 0

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
p = int(input("How many search result pages do you want me to dig? "))
q = "https://google.com/search?q=torrent+tracker+list&start="
pi = 0

while pi < p:
    print("\nQuering @ https://google.com ... (Page "+str(pi+1)+")...")
    r = requests.get(q+str(pi*10)).text
    pi = pi + 1
    print("Results fetched.\nParsing URLs and scrapping trackers (this can take some time depending on your internet speed. BE PATIENT)...", end='')

    soup = BeautifulSoup(r, 'html.parser')
    arr = soup.find_all('a')

    for a in range(16, len(arr)):
        print(".", end='')
        t = str(arr[a]).lower()
        if "torrent" in t and "tracker" in t and "list" in t:
            try:
                i = t.index("http")
                j = t[i:].index("\"")
                t = t[i:i+j]
                collectTrackers(t[0:t.index("&amp;")])
                wct = wct + 1
            except:
                continue
    print()
        
print("\n\nCollected "+str(len(trackers))+" trackers from "+str(wct)+" websites.")

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