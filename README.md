# Torrent Tracker Scrapper
A python program that fetches a lot of trackers from a lot of websites on the internet and puts them in a single text file which you can copy the list from and enter into uTorrent/BitTorrent to try and boost your downloads.

# How is it happening?
It's a pretty <b>non-intelligent</b> piece of code. It fetches the search result of <b>"torrent tracker list"</b> from <a href="https://startpage.com">StartPage</a>, fetches the list of URLs that are expected to lead to a website containing a list of torrent trackers and picks up all the words that matches one of the following expressions:
> http://*/announce

> https://*/announce

> udp://*/announce

# Language
Python 3.x

# Supported platforms
The source file can be run on any platform that supports <a href="https://python.org">Python 3</a>+. Windows binary in available in the <b>bin</b> folder (because Windows users are stupid and they can't do shit themselves).

# Libraries/Dependencies
<ul>
<li> <a href="https://www.crummy.com/software/BeautifulSoup/bs4">BeautifulSoup 4</a> - for parsing HTML</li>
<li> <a href="https://pypi.org/project/requests/">requests</a> - to fetch the HTML response after querying</li>
<li> <a href="https://pypi.org/project/PyInstaller/">PyInstaller</a> <b>(optional)</b> - to build windows binary</li>
</ul>
